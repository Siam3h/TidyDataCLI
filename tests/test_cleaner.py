import unittest
import subprocess
import os
import pandas as pd

class TestTINYDATACLI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.makedirs('tests', exist_ok=True)
        cls.input_csv = 'tests/input.csv'
        cls.cleaned_csv = 'tests/cleaned_data.csv'
        cls.output_plot = 'tests/column_name_frequency.png'
        
        df = pd.DataFrame({
            'column_name': ['a', 'b', 'a', 'b', 'd', 'a'],
            'column_name1': ['b,.', '2?..', 'a,.,', 'b', 'c', 'a'],
            'column_name2': ['c', '3', 'a', 'b', 'd', 'a'],
            'column_name3': ['d', 'b', 'a', '4', 'a', 'a'],
            'column_name4': ['e', 'b', 'a', '5', 'c', 'a'],
        })
        df.to_csv(cls.input_csv, index=False)
    
    @classmethod
    def tearDownClass(cls):
        for file in [cls.input_csv, cls.cleaned_csv, cls.output_plot]:
            if os.path.exists(file):
                os.remove(file)
    
    def run_cli(self, *args):
        command = 'tidydata'
        result = subprocess.run(
            [command] + list(args),
            text=True,
            capture_output=True
        )
        return result.returncode, result.stdout, result.stderr

    def test_clean_data(self):
        returncode, stdout, stderr = self.run_cli(
            'tests/input.csv', 'tests/cleaned_data.csv', '--remove_duplicates'
        )
        self.assertEqual(returncode, 0)
        df = pd.read_csv('tests/cleaned_data.csv')
        self.assertEqual(df.shape[0], 5)
    
    def test_regex_clean(self):
        returncode, stdout, stderr = self.run_cli(
            'tests/input.csv', 'tests/cleaned_data.csv', '--regex_clean', '[1-9]'
        )
        self.assertEqual(returncode, 0)
        df = pd.read_csv('tests/cleaned_data.csv')
        df['column_name1'] = df['column_name1'].astype(str)  
        self.assertTrue(df['column_name1'].str.contains(r'\D').all())

    
    def test_plot_frequency(self):
        returncode, stdout, stderr = self.run_cli(
            'tests/input.csv', 'tests/cleaned_data.csv', '--plot_freq', 'column_name', '--output_dir', 'tests'
        )
        self.assertEqual(returncode, 0)
        self.assertTrue(os.path.exists(self.output_plot))

if __name__ == '__main__':
    unittest.main()
