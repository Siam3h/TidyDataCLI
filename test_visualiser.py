import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
from src.utils.exceptions_utils import ColumnNotFoundError, DataMismatchError, UnsupportedFormatError, render_error_message

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

    def pie_chart(self, labels, values, title="Pie Chart", output_path=None):
        """
        Generate a pie chart.

        Parameters:
        - labels (str): The column for pie chart labels.
        - values (str): The column for pie chart values.
        - title (str, optional): Title of the pie chart.
        - output_path (str, optional): Path to save the pie chart image (if None, will display).
        """
        try:
            if labels not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{labels}' not found in the data.")
            if values not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{values}' not found in the data.")

            data_for_pie = self.data[[labels, values]].dropna()

            if len(data_for_pie[labels]) != len(data_for_pie[values]):
                raise DataMismatchError(f"Mismatch in lengths of 'labels' and 'values' columns.")

            fig = px.pie(data_for_pie, names=labels, values=values, title=title)
            if output_path:
                fig.write_image(output_path)
            else:
                fig.show()

        except (ColumnNotFoundError, DataMismatchError) as e:
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
        - output_path (str, optional): Path to save the table as an HTML file (if None, will display).
        """

        try:
            fig = go.Figure(data=[go.Table(
                header=dict(values=list(self.data.columns),
                            fill_color='paleturquoise',
                            align='left'),
                cells=dict(values=[self.data[col] for col in self.data.columns],
                           fill_color='lavender',
                           align='left'))
            ])

            if output_path:
                if output_format == 'html':
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

    def box_and_whisker_plot(self, x_column, y_column, title="Box and Whisker Plot", output_path=None):
        """
        Generate a box-and-whisker plot.

        Parameters:
        - x (str): The column for the x-axis.
        - y (str): The column for the y-axis.
        - title (str, optional): Title of the box-and-whisker plot.
        - output_path (str, optional): Path to save the chart image (if None, will display).
        """
        try:
            if x_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{x_column}' not found in the data.")
            if y_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{y_column}' not found in the data.")

            plt.figure(figsize=(10, 6))
            sns.boxplot(x=self.data[x_column], y=self.data[y_column])
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

    def heatmap(self, title="Heatmap", output_path=None):
        """
        Generate a heat map of correlations between numeric columns.

        Parameters:
        - title (str, optional): Title of the heat map.
        - output_path (str, optional): Path to save the heat map image (if None, will display).
        """
        try:
            plt.figure(figsize=(10, 6))
            sns.heatmap(self.data.corr(), annot=True, cmap="coolwarm")
            plt.title(title)
            if output_path:
                plt.savefig(output_path)
                plt.close()
            else:
                plt.show()

        except Exception as e:
            render_error_message(e)

    def gantt_chart(self, task_column, start_column, end_column, title="Gantt Chart", output_path=None):
        """
        Generate a Gantt chart.

        Parameters:
        - task_column (str): The column for task names.
        - start_column (str): The column for start dates.
        - end_column (str): The column for end dates.
        - title (str, optional): Title of the Gantt chart.
        - output_path (str, optional): Path to save the chart image (if None, will display).
        """
        try:
            if task_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{task_column}' not found in the data.")
            if start_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{start_column}' not found in the data.")
            if end_column not in self.data.columns:
                raise ColumnNotFoundError(f"Column '{end_column}' not found in the data.")

            fig = ff.create_gantt(self.data, index_col=task_column, show_colorbar=True,
                                  title=title, start=start_column, end=end_column)
            if output_path:
                fig.write_image(output_path)
            else:
                fig.show()

        except ColumnNotFoundError as e:
            render_error_message(e)
        except Exception as e:
            render_error_message(e)

    def correlation_matrix(self, title="Correlation Matrix", output_path=None):
        """
        Generate a correlation matrix heatmap for numerical columns.

        Parameters:
        - title (str, optional): Title of the correlation matrix heatmap (default is "Correlation Matrix").
        - output_path (str, optional): Path to save the heatmap image (if None, will display).

        Raises:
        - DataMismatchError: If there are no numeric columns to calculate correlations.
        """
        try:
            corr_matrix = self.data.corr()
            if corr_matrix.empty:
                raise DataMismatchError("No numeric columns available for correlation matrix.")

            plt.figure(figsize=(10, 6))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
            plt.title(title)
            if output_path:
                plt.savefig(output_path)
                plt.close()
            else:
                plt.show()

        except DataMismatchError as e:
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

    def histogram(self, column, bins=10, title="Histogram", output_path=None):
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
            plt.hist(self.data[column], bins=bins, edgecolor='black')
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

    def treemap(self, path, values, title="Treemap", output_path=None):
        """
        Generate a treemap.

        Parameters:
        - path (list of str): List of columns for hierarchical categories in the treemap.
        - values (str): The column for the treemap values.
        - title (str, optional): Title of the treemap (default is "Treemap").
        - output_path (str, optional): Path to save the treemap image (if None, will display).

        Raises:
        - ColumnNotFoundError: If any of the columns in `path` or `values` are not found in the data.
        """
        try:
            if any(col not in self.data.columns for col in path + [values]):
                raise ColumnNotFoundError(f"One or more columns in {path} or '{values}' not found in the data.")

            fig = px.treemap(self.data, path=path, values=values, title=title)
            if output_path:
                fig.write_image(output_path)
            else:
                fig.show()

        except ColumnNotFoundError as e:
            render_error_message(e)
        except Exception as e:
            render_error_message(e)
