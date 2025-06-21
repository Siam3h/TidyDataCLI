import click
import pandas as pd
from .visualiser import DataVisualizer

@click.group(
    help="""
    **Data Visualization Commands**

    This group provides commands for creating various types of visualizations from a dataset.

    ### Available Visualizations:

    - **basic-bar-chart**: Create a standard bar chart.\n
    - **horizontal-bar-chart**: Create a horizontal bar chart.\n
    - **line-chart**: Generate a line chart for time series data.\n
    - **wordcloud**: Generate a word cloud from a text column.\n
    - **scatter-plot**: Create a scatter plot to visualize relationships between variables.\n

    ### Examples:

    1. **Generate a Basic Bar Chart**:
    \b
    python cmd.py visualize basic-bar-chart input.csv --x_column 'Category' --output 'bar_chart.png'

    2. **Generate a Word Cloud**:
    \b
    python cmd.py visualize wordcloud input.csv --text_column 'Text' --output 'wordcloud.png'
    """
)
def cli():
    """A command-line interface for data visualization using DataVisualizer."""
    pass

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--x_column', help='The column for the x-axis.')
@click.option('--y_column', default=None, help='The column for the y-axis (optional).')
@click.option('--output', default=None, type=click.Path(), help='Path to save the chart image (optional).')
@click.option('--title', default='Basic Bar Chart', help='Title of the bar chart.')
@click.option('--percentage', is_flag=True, default=False, help='Display percentages instead of counts.')
def basic_bar_chart(input_file, x_column, y_column, output, title, percentage):
    """Generate a basic bar chart."""
    data = pd.read_csv(input_file)
    visualizer = DataVisualizer(data)
    visualizer.basic_bar_chart(x_column=x_column, y_column=y_column, percentage=percentage, title=title, output_path=output)

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--x_column', help='The column for the x-axis.')
@click.option('--y_column', default=None, help='The column for the y-axis (optional).')
@click.option('--output', default=None, type=click.Path(), help='Path to save the chart image (optional).')
@click.option('--title', default='Horizontal Bar Chart', help='Title of the horizontal bar chart.')
@click.option('--percentage', is_flag=True, default=False, help='Display percentages instead of counts.')
def horizontal_bar_chart(input_file, x_column, y_column, output, title, percentage):
    """Generate a horizontal bar chart."""
    data = pd.read_csv(input_file)
    visualizer = DataVisualizer(data)
    visualizer.horizontal_bar_chart(x_column=x_column, y_column=y_column, percentage=percentage, title=title, output_path=output)

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--text_column', help='The column containing text data.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the word cloud image (optional).')
@click.option('--title', default='Word Cloud', help='Title of the word cloud.')
def wordcloud(input_file, text_column, output, title):
    """Generate a word cloud from text data."""
    data = pd.read_csv(input_file)
    visualizer = DataVisualizer(data)
    visualizer.wordcloud(text_column=text_column, title=title, output_path=output)

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output', default=None, type=click.Path(), help='Path to save the table (optional).')
@click.option('--format', default='html', help='Output format for the table (html, png, etc.).')
def table(input_file, output, format):
    """Generate a table from the dataset."""
    data = pd.read_csv(input_file)
    visualizer = DataVisualizer(data)
    visualizer.table(output_path=output, output_format=format)

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--x_column', help='The column for the x-axis.')
@click.option('--y_column', help='The column for the y-axis.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the line chart (optional).')
@click.option('--title', default='Line Chart', help='Title of the line chart.')
def line_chart(input_file, x_column, y_column, output, title):
    """Generate a line chart from the dataset."""
    data = pd.read_csv(input_file)
    visualizer = DataVisualizer(data)
    visualizer.line_chart(x_column=x_column, y_column=y_column, title=title, output_path=output)

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--column', help='The column for which the histogram is generated.')
@click.option('--bins', default=10, type=int, help='Number of bins in the histogram.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the histogram image (optional).')
@click.option('--title', default='Histogram', help='Title of the histogram.')
def histogram(input_file, column, bins, output, title):
    """Generate a histogram for a specific column."""
    data = pd.read_csv(input_file)
    visualizer = DataVisualizer(data)
    visualizer.histogram(column=column, bins=bins, title=title, output_path=output)

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--x_column', help='The column for x-axis values.')
@click.option('--y_column', help='The column for y-axis values.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the scatter plot image (optional).')
@click.option('--title', default='Scatter Plot', help='Title of the scatter plot.')
def scatter_plot(input_file, x_column, y_column, output, title):
    """Generate a scatter plot to visualize the relationship between two variables."""
    data = pd.read_csv(input_file)
    visualizer = DataVisualizer(data)
    visualizer.scatter_plot(x_column=x_column, y_column=y_column, title=title, output_path=output)

# Adding commands to the main CLI group
cli.add_command(basic_bar_chart)
cli.add_command(horizontal_bar_chart)
cli.add_command(wordcloud)
cli.add_command(table)
cli.add_command(line_chart)
cli.add_command(histogram)
cli.add_command(scatter_plot)

if __name__ == '__main__':
    cli()
