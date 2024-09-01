import unittest
import os
import shutil
import pandas as pd
import subprocess
from app.cleaner.cleaner import DataCleaner, BasicCleaner, ErrorHandler, TextOperations, FormatStandardizer, DataSplitter

class TestDataCleaner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_dir = 'test'
        os.makedirs(cls.test_dir, exist_ok=True)

        cls.input_csv = os.path.join(cls.test_dir, 'input.csv')
        cls.cleaned_csv = os.path.join(cls.test_dir, 'cleaned_data.csv')

        cls.sample_data = pd.DataFrame({
            ' Name ': [' Alice', 'Bob', ' charlie', 'David', 'Eve', 'Frank', 'Alice'],
            'Age': ['25', 'thirty', '35', '40', '45', '50', '25'],
            'Salary': ['$5000', '$6000', '7000$', '8000', '$9000', '10000$', '5000'],
            'JoinDate': ['2021/01/05', '05-02-2021', 'March 3, 2021', '2021.04.04', '2021-05-05', '2021/06/06', '2021/01/05'],
            'Address': ['123, Main St, NY', '456; Elm St; CA', '789 Oak St, TX', '101 Maple St; FL', '202 Pine St, WA', '303 Birch St; OR', '123 , Main St, NY'],
            'Notes': ['Received teh package', 'Adress confirmed', 'Follow-up needed', 'recieved confirmation', 'All good', 'Pending response', 'received teh Package']
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
            ['python', 'app/cmd.py'] + list(args),
            capture_output=True,
            text=True
        )
        return result.returncode, result.stdout, result.stderr

    def test_clean_column_names(self):
        """Test standardization of column names."""
        cleaner = BasicCleaner(self.data)
        cleaned_data = cleaner.clean_column_names().data

        expected_columns = ['name', 'age', 'salary', 'joindate', 'address', 'notes']
        self.assertListEqual(list(cleaned_data.columns), expected_columns)

    def test_clean_duplicates(self):
        """Test removal of duplicate entries."""
        cleaner = BasicCleaner(self.data)
        cleaned_data = cleaner.clean_column_names().data
        cleaner = DataCleaner(self.data)
        cleaned_data = cleaner.error_handler.clean_duplicates().data
        self.assertEqual(len(cleaned_data), 6)

    def test_validate_data(self):
        """Test validation and correction of data."""
        cleaner = BasicCleaner(self.data)
        cleaned_data = cleaner.clean_column_names().data
        cleaner = DataCleaner(cleaned_data)
        cleaned_data = cleaner.error_handler.validate_data().data
        self.assertNotIn('thirty', cleaned_data['age'].values)
        self.assertTrue(pd.api.types.is_numeric_dtype(cleaned_data['age']))

    def test_change_case(self):
        """Test text case transformations."""
        cleaner = TextOperations(self.data)
        cleaned_data = cleaner.change_case(operation='upper', columns=['Notes']).data

        self.assertTrue(cleaned_data['Notes'].str.isupper().all())

    def test_standardize_date(self):
        """Test date format standardization."""
        cleaner = FormatStandardizer(self.data)
        cleaned_data = cleaner.standardize_date(column='JoinDate').data

        expected_format = '%Y-%m-%d'
        try:
            pd.to_datetime(cleaned_data['JoinDate'], format=expected_format)
            valid_format = True
        except ValueError:
            valid_format = False

        self.assertTrue(valid_format)

    def test_standardize_currency(self):
        """Test currency format standardization."""
        cleaner = FormatStandardizer(self.data)
        cleaned_data = cleaner.standardize_currency(column='Salary').data

        self.assertTrue(cleaned_data['Salary'].dtype == float)
        self.assertAlmostEqual(cleaned_data['Salary'].iloc[0], 5000.0)

    def test_split_delimited_data(self):
        """Test splitting of delimited address data."""
        cleaner = DataSplitter(self.data)
        cleaned_data = cleaner.split_delimited_data(
            column='Address',
            delimiter=r'[;,]',
            new_columns=['Street', 'City', 'State']
        ).data

        self.assertIn('Street', cleaned_data.columns)
        self.assertIn('City', cleaned_data.columns)
        self.assertIn('State', cleaned_data.columns)
        self.assertNotIn('Address', cleaned_data.columns)
        self.assertEqual(cleaned_data['State'].iloc[0].strip(), 'NY')

    def test_clean_all(self):
        """Test complete cleaning process."""
        cleaner = BasicCleaner(self.data)
        cleaned_data = cleaner.clean_column_names().data
        cleaner = DataCleaner(cleaned_data).clean_all()
        cleaned_data = cleaner.data
        expected_columns = ['name', 'age', 'salary', 'joindate', 'address', 'notes']
        self.assertListEqual(list(cleaned_data.columns), expected_columns)
        self.assertNotIn('thirty', cleaned_data['age'].values)
        self.assertEqual(len(cleaned_data), 6)

if __name__ == '__main__':
    unittest.main()