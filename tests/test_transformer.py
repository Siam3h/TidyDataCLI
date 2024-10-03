import unittest
import os
import shutil
import pandas as pd
import subprocess
from src.transformer.transformer import DataTransformer

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
    
    def test_add_column(self):
        new_column = DataTransformer(self.data)
        transformed_data = new_column.add_column(data=self.data, column_name="New Column", value="Nan")
        self.assertEqual(len(transformed_data["New Column"]), 10)
        self.assertTrue(len(transformed_data.columns== 7))
        

    def test_drop_column(self):
        dropped_column = DataTransformer(self.data)
        transformed_data = dropped_column.drop_column(data=self.data,column_name='Age')
        self.assertTrue(len(transformed_data.columns== 5))
        
    def test_rename_column(self):
        renamed_column = DataTransformer(self.data)
        transformed_data = renamed_column.rename_column(data=self.data,old_name='Age', new_name='Ages')
        self.assertTrue(len(transformed_data['Ages']), 10)
        

if __name__ == '__main__':
    unittest.main()
