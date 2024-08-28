import unittest
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
from cli_tool.modules.visualization import DataVisualizer

class TestDataVisualizer(unittest.TestCase):

    def setUp(self):
        """Set up test data."""
        self.test_csv = StringIO("""
        A,B,C
        1,5,9
        2,6,10
        3,7,11
        """)
        self.df = pd.read_csv(self.test_csv)
        self.visualizer = DataVisualizer(self.df)

    def test_bar_chart(self):
        """Test bar chart generation."""
        try:
            self.visualizer.bar_chart(x='A', y='B', title='Test Bar Chart')
        except Exception as e:
            self.fail(f"bar_chart method failed: {e}")

    def test_pie_chart(self):
        """Test pie chart generation."""
        try:
            self.visualizer.pie_chart(labels='A', values='B', title='Test Pie Chart')
        except Exception as e:
            self.fail(f"pie_chart method failed: {e}")

    def test_wordcloud(self):
        """Test word cloud generation."""
        # Create a text column for the word cloud
        self.df['text'] = ['word1 word2', 'word2 word3', 'word3 word1']
        try:
            self.visualizer.wordcloud(text_column='text', title='Test Word Cloud')
        except Exception as e:
            self.fail(f"wordcloud method failed: {e}")

    def test_table(self):
        """Test table generation."""
        try:
            self.visualizer.table()
        except Exception as e:
            self.fail(f"table method failed: {e}")

    def test_line_chart(self):
        """Test line chart generation."""
        try:
            self.visualizer.line_chart(x='A', y='B', title='Test Line Chart')
        except Exception as e:
            self.fail(f"line_chart method failed: {e}")

    def test_box_and_whisker_plot(self):
        """Test box-and-whisker plot generation."""
        try:
            self.visualizer.box_and_whisker_plot(x='A', y='B', title='Test Box-and-Whisker Plot')
        except Exception as e:
            self.fail(f"box_and_whisker_plot method failed: {e}")

    def test_gantt_chart(self):
        """Test Gantt chart generation."""
        # Create additional columns for the Gantt chart
        self.df['Start'] = pd.to_datetime('2024-01-01')
        self.df['End'] = pd.to_datetime('2024-01-02')
        try:
            self.visualizer.gantt_chart(task_column='A', start_column='Start', end_column='End', title='Test Gantt Chart')
        except Exception as e:
            self.fail(f"gantt_chart method failed: {e}")

    def test_heat_map(self):
        """Test heat map generation."""
        try:
            self.visualizer.heat_map(title='Test Heat Map')
        except Exception as e:
            self.fail(f"heat_map method failed: {e}")

    def test_histogram(self):
        """Test histogram generation."""
        try:
            self.visualizer.histogram(column='A', bins=5, title='Test Histogram')
        except Exception as e:
            self.fail(f"histogram method failed: {e}")

    def test_treemap(self):
        """Test treemap generation."""
        # Use a simple path for the treemap
        try:
            self.visualizer.treemap(path=['A'], values='B', title='Test Treemap')
        except Exception as e:
            self.fail(f"treemap method failed: {e}")

if __name__ == '__main__':
    unittest.main()
