import unittest
import os
import pandas as pd
from app.visualiser.visualiser import DataVisualizer

class TestDataVisualizer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up test data and common parameters."""
        data = {
            'Category': ['A', 'B', 'C', 'D'],
            'Values': [23, 45, 56, 78],
            'Text': ['hello world', 'foo bar', 'baz qux', 'lorem ipsum'],
            'Start': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
            'End': ['2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08'],
            'Numeric1': [1, 2, 3, 4],
            'Numeric2': [4, 3, 2, 1]
        }
        cls.df = pd.DataFrame(data)
        cls.df['Start'] = pd.to_datetime(cls.df['Start'])
        cls.df['End'] = pd.to_datetime(cls.df['End'])
        cls.visualizer = DataVisualizer(cls.df)
        cls.output_dir = "test_outputs"
        os.makedirs(cls.output_dir, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        """Clean up test output files."""
        for file_name in os.listdir(cls.output_dir):
            os.remove(os.path.join(cls.output_dir, file_name))
        os.rmdir(cls.output_dir)

    def test_bar_chart(self):
        output_path = os.path.join(self.output_dir, "bar_chart.png")
        self.visualizer.bar_chart(x='Category', y='Values', output_path=output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_pie_chart(self):
        output_path = os.path.join(self.output_dir, "pie_chart.png")
        self.visualizer.pie_chart(labels='Category', values='Values', output_path=output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_wordcloud(self):
        output_path = os.path.join(self.output_dir, "wordcloud.png")
        self.visualizer.wordcloud(text_column='Text', output_path=output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_table(self):
        output_path = os.path.join(self.output_dir, "table.html")
        self.visualizer.table(output_path=output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_line_chart(self):
        output_path = os.path.join(self.output_dir, "line_chart.png")
        self.visualizer.line_chart(x='Category', y='Values', output_path=output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_box_and_whisker_plot(self):
        output_path = os.path.join(self.output_dir, "box_plot.png")
        self.visualizer.box_and_whisker_plot(x='Category', y='Values', output_path=output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_gantt_chart(self):
        output_path = os.path.join(self.output_dir, "gantt_chart.png")
        self.visualizer.gantt_chart(task_column='Category', start_column='Start', end_column='End', output_path=output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_heat_map(self):
        output_path = os.path.join(self.output_dir, "heat_map.png")
        self.visualizer.heat_map(output_path=output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_histogram(self):
        output_path = os.path.join(self.output_dir, "histogram.png")
        self.visualizer.histogram(column='Values', output_path=output_path)
        self.assertTrue(os.path.exists(output_path))

    def test_treemap(self):
        output_path = os.path.join(self.output_dir, "treemap.png")
        self.visualizer.treemap(path=['Category'], values='Values', output_path=output_path)
        self.assertTrue(os.path.exists(output_path))

if __name__ == '__main__':
    unittest.main()
