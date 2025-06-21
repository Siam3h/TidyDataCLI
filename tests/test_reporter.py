import unittest
import pandas as pd
import os
from src.reporter.reporter import create_combined_summary_report, generate_pdf_report, generate_txt_report

class TestReporter(unittest.TestCase):

    def setUp(self):
        """Set up test data and output paths."""
        self.df = pd.DataFrame({
            'Category': ['A', 'B', 'C', 'A'],
            'Values': [10, 25, 40, 17],
            'Missing': [None, 25, None, 17],
        })
        self.pdf_file = 'test_report.pdf'
        self.txt_file = 'test_report.txt'
    
    def tearDown(self):
        """Clean up generated files after tests."""
        for file in [self.pdf_file, self.txt_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_generate_txt_report(self):
        """Test generating a TXT report and ensuring file is created with correct content."""
        report = create_combined_summary_report(self.df)
        generate_txt_report(report, self.txt_file)

        self.assertTrue(os.path.exists(self.txt_file))

        with open(self.txt_file, 'r') as f:
            lines = f.readlines()
            self.assertGreater(len(lines), 0, "The TXT report should contain content.")

if __name__ == '__main__':
    unittest.main()
