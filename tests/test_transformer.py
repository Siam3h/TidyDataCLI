import unittest
import pandas as pd
from app.transformer.transformer import DataTransformer

class TestDataTransformer(unittest.TestCase):
    """Test suite for the DataTransformer class."""

    @classmethod
    def setUpClass(cls):
        """Set up sample data for the test cases."""
        data = {
            'Category': ['A', 'B', 'C', 'A', 'B'],
            'Values': [10, 20, 30, 40, 50],
            'Score': [5.1, 3.4, 8.7, 1.1, 7.2],
        }
        cls.df = pd.DataFrame(data)
        cls.transformer = DataTransformer()

    def test_sort_data_single_column(self):
        """Test sorting by a single column."""
        sorted_df = self.transformer.sort_data(self.df, by='Values', ascending=True)
        self.assertTrue(sorted_df['Values'].is_monotonic_increasing)

    def test_sort_data_multiple_columns(self):
        """Test sorting by multiple columns."""
        sorted_df = self.transformer.sort_data(self.df, by=['Category', 'Score'], ascending=True)
        self.assertEqual(sorted_df.iloc[0]['Category'], 'A')

    def test_sort_data_invalid_column(self):
        """Test sorting by an invalid column."""
        with self.assertRaises(ValueError):
            self.transformer.sort_data(self.df, by='NonExistentColumn')

    def test_filter_data_valid_condition(self):
        """Test filtering data with a valid condition."""
        filtered_df = self.transformer.filter_data(self.df, 'Values > 20')
        self.assertEqual(len(filtered_df), 3)

    def test_filter_data_invalid_condition(self):
        """Test filtering with an invalid condition."""
        with self.assertRaises(ValueError):
            self.transformer.filter_data(self.df, 'InvalidQuery > 20')

    def test_apply_custom_transformation(self):
        """Test applying a custom transformation function."""
        def custom_func(row):
            return row * 2

        transformed_df = self.transformer.apply_custom_transformation(self.df[['Values']], custom_func)
        self.assertTrue((transformed_df['Values'] == [20, 40, 60, 80, 100]).all())

    def test_apply_invalid_custom_function(self):
        """Test applying an invalid custom function."""
        with self.assertRaises(ValueError):
            self.transformer.apply_custom_transformation(self.df, "not_a_function")

if __name__ == '__main__':
    unittest.main()
