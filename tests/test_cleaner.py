import unittest
import os
import shutil
import pandas as pd
import subprocess
from src.cleaner.cleaner import Basic_Cleaner, TextOperations, Standardizer

class TestDataCleaner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_dir = 'test'
        os.makedirs(cls.test_dir, exist_ok=True)

        cls.input_csv = os.path.join(cls.test_dir, 'input.csv')
        cls.cleaned_csv = os.path.join(cls.test_dir, 'cleaned_data.csv')

        cls.sample_data = pd.DataFrame({
            ' Name ': ['Alice ', 'Bob ', ' charlie', 'David', 'Eve', 'Frank', 'Alice', '', '',''],
            'Age': ['25', 'Thirty ', '35', '40', '45', '50', '25',  '', '',''],
            'Salary': ['$5,000', '6000$', ' $7,000', '8,000$', '9000', '$10,000', '$5,000',  '', '',''],
            'Join Date': ['2021/01/05', ' 02-05-2021', 'March 3, 2021', '04.04.2021', '2021-05-05', '2021/06/06', '2021/01/05  ', '', '',''],
            'Address': ['123,Main St,New York,NY   ', '456; Elm St; Los Angeles, CA', '789, Oak St, Dallas, TX', '101, Maple St; Miami; FL', '202, Pine St, Seattle, WA', '303, Birch St; Portland; OR', ' 123,Main St,New York,NY', '', '',''],
            'Notes': ['Received the package   ', 'Address confirmed ', ' Follow-up needed', ' Received confirmation', 'All good ', 'Pending response', 'Received the package',  '', '','']
        })

        cls.sample_data.to_csv(cls.input_csv, index=False)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def setUp(self):
        self.data = pd.read_csv(self.input_csv)

    def run_cli(self, *args):
        """Simulate running the CLI."""
        result = subprocess.run(
            ['python', 'src/cmd.py'] + list(args),
            capture_output=True,
            text=True
        )
        return result.returncode, result.stdout, result.stderr
    
    def test_trim_spaces(self):
        cleaner = Basic_Cleaner(self.data)
        cleaned_data = cleaner.trim_spaces().data

        # Ensure no leading or trailing spaces exist in the string columns
        def check_trimmed(value):
            return value == value.strip() if isinstance(value, str) else True

        # Use map for each column to avoid the applymap warning
        trimmed_check = all(
            cleaned_data[col].map(check_trimmed).all()
            for col in cleaned_data.select_dtypes(include='object').columns
        )

        self.assertTrue(trimmed_check)

    def test_handle_missing_values(self):
        cleaner = Basic_Cleaner(self.data)
        drop_data = cleaner.handle_missing_values(method='drop').data
        fill_data = cleaner.handle_missing_values(method='fill', fill_value='N/A').data

        # Check if rows with missing values are dropped
        self.assertEqual(len(drop_data), 7)
        # Check if missing values are filled correctly
        self.assertTrue((fill_data.isna().sum() == 0).all())
        

    def test_change_case(self):
        """Test text case transformations."""
        cleaner = TextOperations(self.data)
        cleaned_data = cleaner.change_case(operation='upper', columns=['Notes']).data

        self.assertTrue(cleaned_data['Notes'].str.isupper().all())

    def test_standardize_date(self):
        """Test date format standardization."""
        cleaner = Standardizer(self.data)
        cleaned_data = cleaner.standardize_date(column='Join Date').data

        expected_format = '%Y-%m-%d'
        try:
            pd.to_datetime(cleaned_data['Join Date'], format=expected_format)
            valid_format = True
        except ValueError:
            valid_format = False

        self.assertTrue(valid_format)

    def test_standardize_currency(self):
        """Test currency format standardization."""
        cleaner = Standardizer(self.data)
        cleaned_data = cleaner.standardize_currency(column='Salary').data

        self.assertTrue(cleaned_data['Salary'].dtype == float)
        self.assertAlmostEqual(cleaned_data['Salary'].iloc[0], 5000.0)

if __name__ == '__main__':
    unittest.main()
