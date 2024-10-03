from io import BytesIO
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
from src.utils.exceptions import ColumnNotFoundError, DataMismatchError, UnsupportedFormatError, render_error_message

class DataVisualizer:
    """Class to handle various data visualizations."""

    def __init__(self, data):
        """
        Initialize the DataVisualizer with data.

        Parameters:
        - data (pd.DataFrame): The input data for visualization.
        """
        self.data = data

    def basic_bar_chart(self, x_column, y_column=None, percentage=False, title="Basic Bar Chart",
                        x_label=None, y_label='Count', output_path=None):
        """
        Generate a basic bar chart. Supports optional percentage values and grouped mean values.

        Parameters:
        - x_column (str): The column for the x-axis.
        - y_column (str, optional): The column for the y-axis (if grouped bar).
        - percentage (bool, optional): Whether to display percentages instead of counts.
        - title (str, optional): Title of the chart.
        - x_label (str, optional): Label for the x-axis.
        - y_label (str, optional): Label for the y-axis (default is 'Count').
        - output_path (str, optional): Path to save the chart image (if None, will display).
        """
        try:
            plt.figure(figsize=(10, 6))
            if x_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{x_column}' not found in the data.")
            if y_column is not None and y_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{y_column}' not found in the data.")

            if y_column is None:
                value_counts = (self.data[x_column].value_counts(normalize=percentage) * (100 if percentage else 1))
                sns.barplot(x=value_counts.index, y=value_counts.values)
            else:
                grouped_data = self.data.groupby(x_column)[y_column].mean()
                sns.barplot(x=grouped_data.index, y=grouped_data.values)

            plt.title(title)
            plt.xlabel(x_label if x_label else x_column)
            plt.ylabel(y_label)
            if output_path:
                plt.savefig(output_path)
                plt.close()
            else:
                plt.show()

        except ColumnNotFoundError as e:
            render_error_message(e)
        except Exception as e:
            render_error_message(e)

    def horizontal_bar_chart(self, x_column, y_column=None, percentage=False, title="Horizontal Bar Chart",
                             x_label='Count', y_label=None, output_path=None):
        """
        Generate a horizontal bar chart. Supports optional percentage values and grouped mean values.

        Parameters:
        - x_column (str): The column for the x-axis.
        - y_column (str, optional): The column for the y-axis (if grouped bar).
        - percentage (bool, optional): Whether to display percentages instead of counts.
        - title (str, optional): Title of the chart.
        - x_label (str, optional): Label for the x-axis (default is 'Count').
        - y_label (str, optional): Label for the y-axis.
        - output_path (str, optional): Path to save the chart image (if None, will display).
            """
        try:
            plt.figure(figsize=(10, 6))
            if x_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{x_column}' not found in the data.")
            if y_column is not None and y_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{y_column}' not found in the data.")

            if y_column is None:
                value_counts = (self.data[x_column].value_counts(normalize=percentage) * (100 if percentage else 1))
                sns.barplot(x=value_counts.values, y=value_counts.index)
            else:
                grouped_data = self.data.groupby(x_column)[y_column].mean()
                sns.barplot(x=grouped_data.values, y=grouped_data.index)

            plt.title(title)
            plt.xlabel(x_label)
            plt.ylabel(y_label if y_label else x_column)
            if output_path:
                plt.savefig(output_path)
                plt.close()
            else:
                plt.show()

        except ColumnNotFoundError as e:
            render_error_message(e)
        except Exception as e:
            render_error_message(e)

    def wordcloud(self, text_column, title="Word Cloud", output_path=None):
        """
        Generate a word cloud from the given text column.

        Parameters:
        - text_column (str): The column containing text data.
        - title (str, optional): Title of the word cloud.
        - output_path (str, optional): Path to save the word cloud image (if None, will display).
        """
        try:
            if text_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{text_column}' not found in the data.")

            text = " ".join(self.data[text_column].dropna().values)
            wordcloud = WordCloud(width=800, height=400).generate(text)
            plt.figure(figsize=(10, 6))
            plt.imshow(wordcloud, interpolation="bilinear")
            plt.axis("off")
            plt.title(title)
            if output_path:
                plt.savefig(output_path)
                plt.close()
            else:
                plt.show()

        except ColumnNotFoundError as e:
            render_error_message(e)
        except Exception as e:
            render_error_message(e)

    def table(self, output_path=None, output_format="html"):
        """
        Generate a simple table visualization of the dataset.

        Parameters:
        - output_path (str or BytesIO, optional): Path to save the table as an HTML file (if None, will display).
        - output_format (str, optional): The format to save the table ('html', 'png', 'jpeg', etc.).
        """
        try:
            fig = go.Figure(data=[go.Table(
                header=dict(values=list(self.data.columns), fill_color='paleturquoise', align='left'),
                cells=dict(values=[self.data[col] for col in self.data.columns], fill_color='lavender', align='left'))
            ])
            if output_path:
                if output_format == 'html':
                    
                    if isinstance(output_path, BytesIO):
                       
                        html_str = fig.to_html(full_html=False)
                        output_path.write(html_str.encode('utf-8'))
                    else:
                        fig.write_html(output_path)
                elif output_format in ['png', 'jpeg', 'jpg', 'webp', 'svg', 'pdf', 'eps']:
                    fig.write_image(output_path, format=output_format)
                else:
                    raise UnsupportedFormatError(f"Unsupported format: {output_format}.")
            else:
                fig.show()

        except UnsupportedFormatError as e:
            render_error_message(e)
        except Exception as e:
            render_error_message(e)


    def line_chart(self, x_column, y_column, title="Line Chart", x_label=None, y_label=None, output_path=None):
        """
	    Generate a line chart. Supports optional percentage values and grouped mean values.

	    Parameters:
	    - x (str): The column for the x-axis.
	    - y (str, optional): The column for the y-axis (if grouped line).
	    - percentage (bool, optional): Whether to display percentages instead of raw values.
	    - title (str, optional): Title of the line chart.
	    - x_label (str, optional): Label for the x-axis.
	    - y_label (str, optional): Label for the y-axis.
	    - output_path (str, optional): Path to save the chart image (if None, will display).
	    """
        try:
            if x_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{x_column}' not found in the data.")
            if y_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{y_column}' not found in the data.")

            plt.figure(figsize=(10, 6))
            sns.lineplot(data=self.data, x=x_column, y=y_column)
            plt.title(title)
            plt.xlabel(x_label if x_label else x_column)
            plt.ylabel(y_label if y_label else y_column)
            if output_path:
                plt.savefig(output_path)
                plt.close()
            else:
                plt.show()

        except ColumnNotFoundError as e:
            render_error_message(e)
        except Exception as e:
            render_error_message(e)

    def histogram(self, column, bins=10, title="Histogram", x_label=None, y_label='Frequency', output_path=None):
        """
        Generate a histogram for a specific column.

        Parameters:
        - column (str): The column for which the histogram is generated.
        - bins (int, optional): Number of bins in the histogram (default is 10).
        - title (str, optional): Title of the histogram (default is "Histogram").
        - output_path (str, optional): Path to save the histogram image (if None, will display).

        Raises:
        - ColumnNotFoundError: If the specified column is not found in the data.
        """
        try:
            if column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{column}' not found in the data.")

            plt.figure(figsize=(10, 6))
            sns.histplot(self.data[column], bins=bins)
            plt.title(title)
            plt.xlabel(x_label if x_label else column)
            plt.ylabel(y_label)
            if output_path:
                plt.savefig(output_path)
                plt.close()
            else:
                plt.show()

        except ColumnNotFoundError as e:
            render_error_message(e)
        except Exception as e:
            render_error_message(e)

    def scatter_plot(self, x_column, y_column, title="Scatter Plot", x_label=None, y_label=None, output_path=None):
        """
        Generate a scatter plot to visualize the relationship between two variables.

        Parameters:
        - x_column (str): The column for x-axis values.
        - y_column (str): The column for y-axis values.
        - title (str, optional): Title of the scatter plot (default is "Scatter Plot").
        - x_label (str, optional): Label for the x-axis (default is the name of the x_column).
        - y_label (str, optional): Label for the y-axis (default is the name of the y_column).
        - output_path (str, optional): Path to save the scatter plot image (if None, will display).

        Raises:
        - ColumnNotFoundError: If either the x_column or y_column is not found in the data.
        """
        try:
            if x_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{x_column}' not found in the data.")
            if y_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{y_column}' not found in the data.")

            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=self.data[x_column], y=self.data[y_column])
            plt.title(title)
            plt.xlabel(x_label if x_label else x_column)
            plt.ylabel(y_label if y_label else y_column)
            if output_path:
                plt.savefig(output_path)
                plt.close()
            else:
                plt.show()

        except ColumnNotFoundError as e:
            render_error_message(e)
        except Exception as e:
            render_error_message(e)

