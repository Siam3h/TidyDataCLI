import unittest
import pandas as pd
from io import StringIO
from cli_tool.modules.transformation import DataTransformer

class TestDataTransformer(unittest.TestCase):
    
    def setUp(self):
        """Set up test data."""
        self.test_csv = StringIO("""
        A,B,C
        1,2,3
        4,5,6
        3,6,9
        2,4,8
        """)
        self.df = pd.read_csv(self.test_csv)
        self.transformer = DataTransformer(self.df)
    
    def test_sort_data(self):
        """Test sorting functionality."""
        sorted_df = self.transformer.sort_data(by='A')
        expected_df = self.df.sort_values(by='A')
        pd.testing.assert_frame_equal(sorted_df, expected_df)

        sorted_df_desc = self.transformer.sort_data(by='B', ascending=False)
        expected_df_desc = self.df.sort_values(by='B', ascending=False)
        pd.testing.assert_frame_equal(sorted_df_desc, expected_df_desc)
    
    def test_filter_data(self):
        """Test filtering functionality."""
        filtered_df = self.transformer.filter_data('A > 2')
        expected_df = self.df.query('A > 2')
        pd.testing.assert_frame_equal(filtered_df, expected_df)
    
    def test_apply_custom_transformation(self):
        """Test applying a custom transformation."""
        def add_one(x):
            return x + 1
        
        transformed_df = self.transformer.apply_custom_transformation(add_one)
        expected_df = self.df.apply(add_one)
        pd.testing.assert_frame_equal(transformed_df, expected_df)

if __name__ == '__main__':
    unittest.main()
