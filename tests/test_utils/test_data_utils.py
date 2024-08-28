import unittest
import pandas as pd
from cli_tool.utils.data_utils import filter_data, clean_data

class TestDataUtils(unittest.TestCase):

    def setUp(self):
        """Set up test data."""
        # Sample DataFrame for testing
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5, None],
            'B': [5, 4, 3, 2, 1, 1],
            'C': [None, 'foo', 'bar', 'foo', 'bar', 'baz']
        })
        
        # DataFrame with some duplicates and missing values
        self.df_cleaned = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1],
            'C': ['foo', 'bar', 'foo', 'bar', 'baz']
        })

    def test_filter_data(self):
        """Test filtering of data based on a condition."""
        # Filter rows where column 'A' is greater than 2
        result = filter_data(self.df, 'A > 2')
        expected = pd.DataFrame({
            'A': [3, 4, 5, None],
            'B': [3, 2, 1, 1],
            'C': ['bar', 'foo', 'bar', 'baz']
        }).reset_index(drop=True)
        
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

    def test_clean_data(self):
        """Test cleaning of data by dropping NA and duplicates."""
        result = clean_data(self.df)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), self.df_cleaned.reset_index(drop=True))

    def test_filter_data_empty_result(self):
        """Test filtering when no rows match the condition."""
        result = filter_data(self.df, 'A > 10')
        expected = pd.DataFrame(columns=self.df.columns)
        pd.testing.assert_frame_equal(result, expected)

    def test_clean_data_no_changes(self):
        """Test cleaning data that is already clean."""
        result = clean_data(self.df_cleaned)
        pd.testing.assert_frame_equal(result.reset_index(drop=True), self.df_cleaned.reset_index(drop=True))

    def test_filter_data_invalid_condition(self):
        """Test filtering with an invalid condition."""
        with self.assertRaises(SyntaxError):
            filter_data(self.df, 'A >')

if __name__ == '__main__':
    unittest.main()
