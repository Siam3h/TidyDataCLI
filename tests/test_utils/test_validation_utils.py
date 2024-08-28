import unittest
import pandas as pd
import os
from cli_tool.utils.validation_utils import validate_csv, validate_excel, check_data_integrity

class TestUtils(unittest.TestCase):

    def setUp(self):
        """Set up test data and files."""
        self.valid_csv = 'test_valid.csv'
        self.invalid_csv = 'test_invalid.csv'
        self.valid_excel = 'test_valid.xlsx'
        self.invalid_excel = 'test_invalid.xlsx'
        
        # Create a valid CSV file
        df_valid_csv = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        df_valid_csv.to_csv(self.valid_csv, index=False)
        
        # Create a valid Excel file
        df_valid_excel = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        df_valid_excel.to_excel(self.valid_excel, index=False)

        # Create an invalid CSV file
        with open(self.invalid_csv, 'w') as f:
            f.write('this,is,not,a,csv\n')

        # Create an invalid Excel file (not a real Excel file)
        with open(self.invalid_excel, 'w') as f:
            f.write('this is not an excel file')

    def tearDown(self):
        """Clean up test files."""
        os.remove(self.valid_csv)
        os.remove(self.invalid_csv)
        os.remove(self.valid_excel)
        os.remove(self.invalid_excel)

    def test_validate_csv(self):
        """Test validation of CSV files."""
        self.assertTrue(validate_csv(self.valid_csv))
        self.assertFalse(validate_csv(self.invalid_csv))

    def test_validate_excel(self):
        """Test validation of Excel files."""
        self.assertTrue(validate_excel(self.valid_excel))
        self.assertFalse(validate_excel(self.invalid_excel))

    def test_check_data_integrity(self):
        """Test checking data integrity."""
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        required_columns = ['A', 'B']
        self.assertTrue(check_data_integrity(df, required_columns))
        
        missing_columns = ['A', 'C']
        self.assertFalse(check_data_integrity(df, missing_columns))

if __name__ == '__main__':
    unittest.main()
