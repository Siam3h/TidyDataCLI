import unittest
import pandas as pd
from matplotlib import pyplot as plt
from io import BytesIO
from src.visualiser.visualiser import DataVisualizer

class TestDataVisualizer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create a sample dataset for testing
        cls.data = pd.DataFrame({
            'Category': ['A', 'B', 'C', 'D', 'E'],
            'Value': [10, 20, 30, 40, 50],
            'Percentage': [0.1, 0.2, 0.3, 0.4, 0.5],
            'Date': pd.date_range(start='2023-01-01', periods=5),
            'Text': ['apple', 'banana', 'carrot', 'date', 'eggplant']
        })
        cls.visualizer = DataVisualizer(cls.data)

        # Use 'Agg' backend for matplotlib to prevent display during tests
        plt.switch_backend('Agg')

    def test_basic_bar_chart(self):
        """Test the basic bar chart generation."""
        buffer = BytesIO()
        self.visualizer.basic_bar_chart(x_column='Category', output_path=buffer)
        buffer.seek(0)
        result = buffer.read()
        self.assertGreater(len(result), 0, "The basic bar chart output should not be empty.")

    def test_horizontal_bar_chart(self):
        """Test horizontal bar chart generation."""
        buffer = BytesIO()
        self.visualizer.horizontal_bar_chart(x_column='Category', output_path=buffer)
        buffer.seek(0)
        result = buffer.read()
        self.assertGreater(len(result), 0, "The horizontal bar chart output should not be empty.")

    def test_wordcloud(self):
        """Test word cloud generation."""
        buffer = BytesIO()
        self.visualizer.wordcloud(text_column='Text', output_path=buffer)
        buffer.seek(0)
        result = buffer.read()
        self.assertGreater(len(result), 0, "The word cloud output should not be empty.")

    def test_table_html_output(self):
        """Test table generation with HTML format."""
        buffer = BytesIO()
        self.visualizer.table(output_path=buffer, output_format='html')
        buffer.seek(0)
        result = buffer.read()
        self.assertGreater(len(result), 0, "The table (HTML) output should not be empty.")

    def test_line_chart(self):
        """Test line chart generation."""
        buffer = BytesIO()
        self.visualizer.line_chart(x_column='Date', y_column='Value', output_path=buffer)
        buffer.seek(0)
        result = buffer.read()
        self.assertGreater(len(result), 0, "The line chart output should not be empty.")

    def test_histogram(self):
        """Test histogram generation."""
        buffer = BytesIO()
        self.visualizer.histogram(column='Value', bins=5, output_path=buffer)
        buffer.seek(0)
        result = buffer.read()
        self.assertGreater(len(result), 0, "The histogram output should not be empty.")

    def test_scatter_plot(self):
        """Test scatter plot generation."""
        buffer = BytesIO()
        self.visualizer.scatter_plot(x_column='Value', y_column='Percentage', output_path=buffer)
        buffer.seek(0)
        result = buffer.read()
        self.assertGreater(len(result), 0, "The scatter plot output should not be empty.")

if __name__ == '__main__':
    unittest.main()
