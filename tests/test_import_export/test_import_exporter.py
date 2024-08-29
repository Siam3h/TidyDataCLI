import os
import unittest
import pandas as pd
from io import StringIO
from tempfile import NamedTemporaryFile
from app.import_export import CSVHandler, ExcelHandler, JSONHandler

class TestDataHandlers(unittest.TestCase):
    
    def setUp(self):
        """Set up temporary files and data for testing."""
        self.csv_data = StringIO("""
        A,B,C
        1,2,3
        4,5,6
        """)
        self.df = pd.read_csv(self.csv_data)

        # Create temporary files
        self.temp_csv = NamedTemporaryFile(delete=False, suffix='.csv')
        self.temp_excel = NamedTemporaryFile(delete=False, suffix='.xlsx')
        self.temp_json = NamedTemporaryFile(delete=False, suffix='.json')
        
        # Save initial data to temporary files
        self.df.to_csv(self.temp_csv.name, index=False)
        self.df.to_excel(self.temp_excel.name, index=False)
        self.df.to_json(self.temp_json.name)

    def tearDown(self):
        """Clean up temporary files."""
        self.temp_csv.close()
        self.temp_excel.close()
        self.temp_json.close()
        
        os.remove(self.temp_csv.name)
        os.remove(self.temp_excel.name)
        os.remove(self.temp_json.name)

    def test_csv_handler(self):
        """Test CSVHandler functionality."""
        handler = CSVHandler(self.temp_csv.name)
        loaded_data = handler.load_data()
        pd.testing.assert_frame_equal(loaded_data, self.df)
        
        output_csv = NamedTemporaryFile(delete=False, suffix='.csv')
        handler.save_data(self.df, output_csv.name)
        output_csv.close()
        loaded_output_data = pd.read_csv(output_csv.name)
        pd.testing.assert_frame_equal(loaded_output_data, self.df)
        os.remove(output_csv.name)
    
    def test_excel_handler(self):
        """Test ExcelHandler functionality."""
        handler = ExcelHandler(self.temp_excel.name)
        loaded_data = handler.load_data()
        pd.testing.assert_frame_equal(loaded_data, self.df)
        
        output_excel = NamedTemporaryFile(delete=False, suffix='.xlsx')
        handler.save_data(self.df, output_excel.name)
        output_excel.close()
        loaded_output_data = pd.read_excel(output_excel.name)
        pd.testing.assert_frame_equal(loaded_output_data, self.df)
        os.remove(output_excel.name)

    def test_json_handler(self):
        """Test JSONHandler functionality."""
        handler = JSONHandler(self.temp_json.name)
        loaded_data = handler.load_data()
        pd.testing.assert_frame_equal(loaded_data, self.df)

        output_json = NamedTemporaryFile(delete=False, suffix='.json')
        handler.save_data(self.df, output_json.name)
        output_json.close()
        loaded_output_data = pd.read_json(output_json.name)
        pd.testing.assert_frame_equal(loaded_output_data, self.df)
        os.remove(output_json.name)

if __name__ == '__main__':
    unittest.main()
