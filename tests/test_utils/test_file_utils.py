import unittest
import pandas as pd
import os
import gzip
from io import BytesIO
from cli_tool.utils.file_utils import read_file, write_file, compress_file, decompress_file

class TestFileUtils(unittest.TestCase):

    def setUp(self):
        """Set up test data and files."""
        self.test_csv = 'test.csv'
        self.test_excel = 'test.xlsx'
        self.test_compressed = 'test.csv.gz'
        self.test_decompressed = 'test_decompressed.csv'
        
        # Create a sample DataFrame
        self.df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        
        # Write sample DataFrame to CSV and Excel files
        write_file(self.test_csv, self.df)
        write_file(self.test_excel, self.df)

        # Compress the CSV file
        compress_file(self.test_csv)

    def tearDown(self):
        """Clean up test files."""
        for file in [self.test_csv, self.test_excel, self.test_compressed, self.test_decompressed]:
            if os.path.exists(file):
                os.remove(file)

    def test_read_file_csv(self):
        """Test reading a CSV file."""
        df_read = read_file(self.test_csv)
        pd.testing.assert_frame_equal(self.df, df_read)

    def test_read_file_excel(self):
        """Test reading an Excel file."""
        df_read = read_file(self.test_excel)
        pd.testing.assert_frame_equal(self.df, df_read)

    def test_write_file_csv(self):
        """Test writing a CSV file."""
        new_csv = 'test_write.csv'
        write_file(new_csv, self.df)
        df_read = read_file(new_csv)
        pd.testing.assert_frame_equal(self.df, df_read)
        os.remove(new_csv)

    def test_write_file_excel(self):
        """Test writing an Excel file."""
        new_excel = 'test_write.xlsx'
        write_file(new_excel, self.df)
        df_read = read_file(new_excel)
        pd.testing.assert_frame_equal(self.df, df_read)
        os.remove(new_excel)

    def test_compress_file(self):
        """Test compressing a file."""
        self.assertTrue(os.path.exists(self.test_compressed))
    
    def test_decompress_file(self):
        """Test decompressing a file."""
        decompress_file(self.test_compressed)
        self.assertTrue(os.path.exists(self.test_csv))
        
        # Check if decompressed file matches the original
        with open(self.test_csv, 'rb') as original, open(self.test_csv, 'rb') as decompressed:
            self.assertEqual(original.read(), decompressed.read())
        
        os.remove(self.test_csv)

    def test_invalid_file_format(self):
        """Test invalid file format handling."""
        with self.assertRaises(ValueError):
            read_file('invalid_file.txt')
        
        with self.assertRaises(ValueError):
            write_file('invalid_file.txt', self.df)
        
        with self.assertRaises(ValueError):
            compress_file('invalid_file.txt')

        with self.assertRaises(ValueError):
            decompress_file('invalid_file.txt')

if __name__ == '__main__':
    unittest.main()
