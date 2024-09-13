import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from rich.console import Console
from rich.progress import track
from rich.traceback import install
from src.visualiser.visualiser import DataVisualizer
from src.file_handler.fileHandler import get_handler, determine_file_format
from src.utils.exceptions import ColumnNotFoundError, DataMismatchError, InvalidChartTypeError

console = Console()
install()

class VisualiserCommand:
    @staticmethod
    def add_visualising_subparser(subparsers):
        parser = subparsers.add_parser('visualize', help="Visualize data", description="Generate various types of charts from data.")
        parser.add_argument('input', type=str, help="Input file path (CSV, Excel, or JSON)")
        parser.add_argument('--chart_type', type=str, required=True, help="Type of visualization chart to generate",
                            choices=['bar', 'horizontal', 'pie', 'wordcloud', 'table', 'line',
                                     'box', 'gantt', 'heatmap', 'histogram', 'treemap', 'correlation', 'scatter'])
        parser.add_argument('--x', type=str, help="X-axis data for bar/line/box plots or column for histogram")
        parser.add_argument('--y', type=str, help="Y-axis data for bar/line/box plots")
        parser.add_argument('--percentage', action='store_true', help="Plot values as percentages")
        parser.add_argument('--labels', type=str, help="Labels for pie chart")
        parser.add_argument('--values', type=str, help="Values for pie chart or treemap")
        parser.add_argument('--text_column', type=str, help="Text column for word cloud")
        parser.add_argument('--task_column', type=str, help="Task column for Gantt chart")
        parser.add_argument('--start_column', type=str, help="Start date column for Gantt chart")
        parser.add_argument('--end_column', type=str, help="End date column for Gantt chart")
        parser.add_argument('--path', nargs='+', help="Path for treemap")
        parser.add_argument('--column', type=str, help="Column for histogram")
        parser.add_argument('--bins', type=int, default=10, help="Number of bins for histogram")
        parser.add_argument('--output_path', type=str, help="Path to save the output chart image", default=None)
        parser.add_argument('--title', default="Chart", help="Title of the chart")
        parser.add_argument('--x_label', help="Label for the x-axis")
        parser.add_argument('--y_label', help="Label for the y-axis")
        parser.set_defaults(func=VisualiserCommand.visualiser_command)

    @staticmethod
    def visualiser_command(args):
        file_format = determine_file_format(args.input)
        handler = get_handler(file_format, args.input)

        try:
            console.print(f"[green]Loading data from {args.input}...[/green]")
            data = handler.load_data()
        except Exception as e:
            console.print(f"[bold red]Error reading input file: {e}[/bold red]")
            return

        data_visualiser = DataVisualizer(data)

        try:
            for _ in track(range(1), description="Generating visualization..."):
                if args.chart_type == 'bar':
                    if not args.x or not args.y:
                        raise ColumnNotFoundError("Both --x and --y arguments are required for a bar chart")
                    data_visualiser.basic_bar_chart(x_column=args.x, y_column=args.y, percentage=args.percentage,
                                                    title=args.title, x_label=args.x_label, y_label=args.y_label,
                                                    output_path=args.output_path)

                elif args.chart_type == 'horizontal':
                    if not args.x or not args.y:
                        raise ColumnNotFoundError("Both --x and --y arguments are required for a horizontal bar chart")
                    data_visualiser.horizontal_bar_chart(x_column=args.x, y_column=args.y, percentage=args.percentage,
                                                         title=args.title, x_label=args.x_label, y_label=args.y_label,
                                                         output_path=args.output_path)

                elif args.chart_type == 'pie':
                    if not args.labels or not args.values:
                        raise DataMismatchError("Pie chart requires both --labels and --values arguments")
                    data_visualiser.pie_chart(labels=args.labels, values=args.values, title=args.title,
                                              output_path=args.output_path)

                elif args.chart_type == 'wordcloud':
                    if not args.text_column:
                        raise ColumnNotFoundError("Word cloud requires --text_column argument")
                    data_visualiser.wordcloud(text_column=args.text_column, title=args.title, output_path=args.output_path)

                elif args.chart_type == 'table':
                    data_visualiser.table(output_path=args.output_path)

                elif args.chart_type == 'line':
                    if not args.x or not args.y:
                        raise ColumnNotFoundError("Line chart requires both --x and --y arguments")
                    data_visualiser.line_chart(x=args.x, y=args.y, title=args.title, output_path=args.output_path)

                elif args.chart_type == 'box':
                    if not args.x or not args.y:
                        raise ColumnNotFoundError("Box-and-whisker plot requires both --x and --y arguments")
                    data_visualiser.box_and_whisker_plot(x=args.x, y=args.y, title=args.title, output_path=args.output_path)

                elif args.chart_type == 'gantt':
                    if not args.task_column or not args.start_column or not args.end_column:
                        raise ColumnNotFoundError("Gantt chart requires --task_column, --start_column, and --end_column arguments")
                    data_visualiser.gantt_chart(task_column=args.task_column, start_column=args.start_column,
                                                end_column=args.end_column, title=args.title, output_path=args.output_path)

                elif args.chart_type == 'heatmap':
                    data_visualiser.heat_map(title=args.title, output_path=args.output_path)

                elif args.chart_type == 'histogram':
                    if not args.column:
                        raise ColumnNotFoundError("Histogram requires --column argument")
                    data_visualiser.histogram(column=args.column, bins=args.bins, title=args.title, output_path=args.output_path)

                elif args.chart_type == 'treemap':
                    if not args.path or not args.values:
                        raise DataMismatchError("Treemap requires both --path and --values arguments")
                    data_visualiser.treemap(path=args.path, values=args.values, title=args.title, output_path=args.output_path)

                elif args.chart_type == 'correlation':
                    data_visualiser.correlation_matrix(title=args.title, output_path=args.output_path)

                elif args.chart_type == 'scatter':
                    if not args.x or not args.y:
                        raise ColumnNotFoundError("Scatter plot requires both --x and --y arguments")
                    data_visualiser.scatter_plot(x_column=args.x, y_column=args.y, title=args.title, x_label=args.x_label,
                                                 y_label=args.y_label, output_path=args.output_path)

                else:
                    raise InvalidChartTypeError(f"Unknown visualization type: {args.chart_type}")

            if args.output_path:
                console.print(f"[bold green]Visualization saved to {args.output_path}[/bold green]")
            else:
                console.print("[yellow]Visualization displayed but not saved (no output path provided).[/yellow]")

        except (ColumnNotFoundError, DataMismatchError, InvalidChartTypeError) as e:
            console.print(f"[bold red]Error generating visualization: {e}[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Unexpected error occurred: {e}[/bold red]")
