import unittest
import os
import pandas as pd
from app.reporter.reporter import generate_report, load_data, create_report, generate_pdf_report

class TestReporter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup test data."""
        cls.csv_file = "test_data.csv"
        cls.excel_file = "test_data.xlsx"
        data = {
            'Category': ['A', 'B', 'C', 'D'],
            'Values': [10, 20, 30, 40],
            'Text': ['foo', 'bar', 'baz', 'qux']
        }
        cls.df = pd.DataFrame(data)
        cls.df.to_csv(cls.csv_file, index=False)
        cls.df.to_excel(cls.excel_file, index=False)

    @classmethod
    def tearDownClass(cls):
        """Cleanup test files."""
        os.remove(cls.csv_file)
        os.remove(cls.excel_file)

    def test_load_data_csv(self):
        df = load_data(self.csv_file)
        self.assertEqual(len(df), 4)
        self.assertEqual(list(df.columns), ['Category', 'Values', 'Text'])

    def test_load_data_excel(self):
        df = load_data(self.excel_file)
        self.assertEqual(len(df), 4)
        self.assertEqual(list(df.columns), ['Category', 'Values', 'Text'])

    def test_create_report(self):
        report = create_report(self.df)
        self.assertIn("Number of Rows: 4", report)
        self.assertIn("Column: Values", report)

    def test_generate_report_txt(self):
        report = generate_report(self.csv_file, output_format='txt')
        self.assertIn("Summary Report", report)
        self.assertIn("Number of Rows: 4", report)

    def test_generate_report_pdf(self):
        output = generate_report(self.csv_file, output_format='pdf')
        self.assertTrue(os.path.exists("test_data.pdf"))
        self.assertIn("PDF report generated", output)
        os.remove("test_data.pdf")

    def test_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            generate_report("non_existent_file.csv")

    def test_unsupported_format(self):
        with self.assertRaises(ValueError):
            load_data("invalid_format.txt")

if __name__ == '__main__':
    unittest.main()
