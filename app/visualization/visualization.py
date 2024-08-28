import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud

class DataVisualizer:
    """Class to handle various data visualizations."""
    
    def __init__(self, data):
        self.data = data

    def bar_chart(self, x, y, title="Bar Chart"):
        """Generate a bar chart."""
        plt.figure(figsize=(10, 6))
        sns.barplot(x=x, y=y, data=self.data)
        plt.title(title)
        plt.show()

    def pie_chart(self, labels, values, title="Pie Chart"):
        """Generate a pie chart."""
        fig = px.pie(self.data, names=labels, values=values, title=title)
        fig.show()

    def wordcloud(self, text_column, title="Word Cloud"):
        """Generate a word cloud."""
        text = " ".join(self.data[text_column].dropna().values)
        wordcloud = WordCloud(width=800, height=400).generate(text)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title(title)
        plt.show()

    def table(self):
        """Generate a simple table."""
        fig = go.Figure(data=[go.Table(
            header=dict(values=list(self.data.columns),
                        fill_color='paleturquoise',
                        align='left'),
            cells=dict(values=[self.data[col] for col in self.data.columns],
                       fill_color='lavender',
                       align='left'))
        ])
        fig.show()

    def line_chart(self, x, y, title="Line Chart"):
        """Generate a line chart."""
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=x, y=y, data=self.data)
        plt.title(title)
        plt.show()

    def box_and_whisker_plot(self, x, y, title="Box-and-Whisker Plot"):
        """Generate a box-and-whisker plot."""
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=x, y=y, data=self.data)
        plt.title(title)
        plt.show()

    def gantt_chart(self, task_column, start_column, end_column, title="Gantt Chart"):
        """Generate a Gantt chart."""
        df = self.data[[task_column, start_column, end_column]]
        df.columns = ["Task", "Start", "Finish"]
        fig = ff.create_gantt(df, index_col='Task', show_colorbar=True, title=title)
        fig.show()

    def heat_map(self, title="Heat Map"):
        """Generate a heat map."""
        plt.figure(figsize=(10, 6))
        sns.heatmap(self.data.corr(), annot=True, cmap='coolwarm')
        plt.title(title)
        plt.show()

    def histogram(self, column, bins=10, title="Histogram"):
        """Generate a histogram."""
        plt.figure(figsize=(10, 6))
        plt.hist(self.data[column], bins=bins, edgecolor='black')
        plt.title(title)
        plt.show()

    def treemap(self, path, values, title="Treemap"):
        """Generate a treemap."""
        fig = px.treemap(self.data, path=path, values=values, title=title)
        fig.show()
