import argparse
import pandas as pd
from .visualiser import DataVisualizer
import matplotlib.pyplot as plt

class VisualiserCommand:

    @staticmethod
    def add_visualising_subparser(subparsers):
        parser = subparsers.add_parser('visualize', help="Visualize data")
        parser.add_argument('input', type=str, help="Input file path")
        parser.add_argument('--type', type=str, required=True, help="Type of visualization",
                            choices=['bar', 'pie', 'wordcloud', 'table', 'line',
                                     'box', 'gantt', 'heat', 'histogram', 'treemap'])
        parser.add_argument('--x', type=str, help="X-axis data for bar/line/box plots or column for histogram")
        parser.add_argument('--y', type=str, help="Y-axis data for bar/line/box plots")
        parser.add_argument('--labels', type=str, help="Labels for pie chart")
        parser.add_argument('--values', type=str, help="Values for pie chart or treemap")
        parser.add_argument('--text_column', type=str, help="Text column for word cloud")
        parser.add_argument('--task_column', type=str, help="Task column for Gantt chart")
        parser.add_argument('--start_column', type=str, help="Start date column for Gantt chart")
        parser.add_argument('--end_column', type=str, help="End date column for Gantt chart")
        parser.add_argument('--path', nargs='+', help="Path for treemap")
        parser.add_argument('--column', type=str, help="Column for histogram")
        parser.add_argument('--bins', type=int, default=10, help="Number of bins for histogram")
        parser.add_argument('--output', type=str, help="Output file path", default=None)
        parser.set_defaults(func=VisualiserCommand.visualiser_command)

    @staticmethod
    def visualiser_command(args):
        try:
            data_frame = pd.read_csv(args.input)
        except Exception as e:
            print(f"Error reading input file: {e}")
            return

        data_visualiser = DataVisualizer(data_frame)

        visualization_type = args.type
        output_path = args.output

        try:
            if visualization_type == 'bar':
                if not args.x or not args.y:
                    raise ValueError("Bar chart requires --x and --y arguments")
                data_visualiser.bar_chart(x=args.x, y=args.y, title="Bar Chart", output_path=output_path)
            elif visualization_type == 'pie':
                if not args.labels or not args.values:
                    raise ValueError("Pie chart requires --labels and --values arguments")
                data_visualiser.pie_chart(labels=args.labels, values=args.values, title="Pie Chart", output_path=output_path)
            elif visualization_type == 'wordcloud':
                if not args.text_column:
                    raise ValueError("Word cloud requires --text_column argument")
                data_visualiser.wordcloud(text_column=args.text_column, title="Word Cloud", output_path=output_path)
            elif visualization_type == 'table':
                data_visualiser.table(output_path=output_path)
            elif visualization_type == 'line':
                if not args.x or not args.y:
                    raise ValueError("Line chart requires --x and --y arguments")
                data_visualiser.line_chart(x=args.x, y=args.y, title="Line Chart", output_path=output_path)
            elif visualization_type == 'box':
                if not args.x or not args.y:
                    raise ValueError("Box-and-Whisker plot requires --x and --y arguments")
                data_visualiser.box_and_whisker_plot(x=args.x, y=args.y, title="Box-and-Whisker Plot", output_path=output_path)
            elif visualization_type == 'gantt':
                if not args.task_column or not args.start_column or not args.end_column:
                    raise ValueError("Gantt chart requires --task_column, --start_column, and --end_column arguments")
                data_visualiser.gantt_chart(task_column=args.task_column, start_column=args.start_column, end_column=args.end_column, title="Gantt Chart", output_path=output_path)
            elif visualization_type == 'heat':
                data_visualiser.heat_map(title="Heat Map", output_path=output_path)
            elif visualization_type == 'histogram':
                if not args.column:
                    raise ValueError("Histogram requires --column argument")
                data_visualiser.histogram(column=args.column, bins=args.bins, title="Histogram", output_path=output_path)
            elif visualization_type == 'treemap':
                if not args.path or not args.values:
                    raise ValueError("Treemap requires --path and --values arguments")
                data_visualiser.treemap(path=args.path, values=args.values, title="Treemap", output_path=output_path)
            else:
                raise ValueError(f"Unknown visualization type: {visualization_type}")

            # Inform the user about saving
            if output_path:
                print(f"Visualization saved to {output_path}")
            else:
                print("Visualization displayed but not saved, as no output path was provided.")
        except Exception as e:
            print(f"Error generating visualization: {e}")
