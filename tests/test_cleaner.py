import unittest
import subprocess
import os
import pandas as pd

class TestTINYDATACLI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input_csv = 'tests/input.csv'
        cls.cleaned_csv = 'tests/cleaned_data.csv'
        cls.output_plot = 'tests/column_name_frequency.png'
        
        df = pd.DataFrame({
            'column_name': ['a', 'b', 'a', 'c', 'b', 'a'],
            'other_column': ['1', '2', '3', '4', '5', '6']
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
        self.assertEqual(df.shape[0], 3)
    
    def test_regex_clean(self):
        returncode, stdout, stderr = self.run_cli(
            'tests/input.csv', 'tests/cleaned_data.csv', '--regex_clean', '[1-9]'
        )
        self.assertEqual(returncode, 0)
        df = pd.read_csv('tests/cleaned_data.csv')
        self.assertTrue(df['other_column'].str.contains(r'\D').all())
    
    def test_plot_frequency(self):
        returncode, stdout, stderr = self.run_cli(
            'tests/input.csv', 'tests/cleaned_data.csv', '--plot_freq', 'column_name', '--output_dir', 'tests'
        )
        self.assertEqual(returncode, 0)
        self.assertTrue(os.path.exists(self.output_plot))

if __name__ == '__main__':
    unittest.main()
