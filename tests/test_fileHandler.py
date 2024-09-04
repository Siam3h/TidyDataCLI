import unittest
from unittest.mock import patch, mock_open, MagicMock
import pandas as pd
from app.file_handler.fileHandler import CSVHandler, ExcelHandler, JSONHandler, get_handler, import_data, export_data

class TestCSVHandler(unittest.TestCase):

    @patch("app.file_handler.fileHandler.pd.read_csv")
    def test_load_data(self, mock_read_csv):
        mock_read_csv.return_value = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        handler = CSVHandler("test.csv")
        data = handler.load_data()
        mock_read_csv.assert_called_once_with("test.csv")
        pd.testing.assert_frame_equal(data, pd.DataFrame({"col1": [1, 2], "col2": [3, 4]}))

    @patch("app.file_handler.fileHandler.pd.DataFrame.to_csv")
    def test_save_data(self, mock_to_csv):
        handler = CSVHandler("test.csv")
        data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        handler.save_data(data)
        mock_to_csv.assert_called_once_with("test.csv", index=False)


class TestExcelHandler(unittest.TestCase):

    @patch("app.file_handler.fileHandler.pd.read_excel")
    def test_load_data(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        handler = ExcelHandler("test.xlsx")
        data = handler.load_data()
        mock_read_excel.assert_called_once_with("test.xlsx", sheet_name=0)
        pd.testing.assert_frame_equal(data, pd.DataFrame({"col1": [1, 2], "col2": [3, 4]}))

    @patch("app.file_handler.fileHandler.pd.DataFrame.to_excel")
    def test_save_data(self, mock_to_excel):
        handler = ExcelHandler("test.xlsx")
        data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        handler.save_data(data)
        mock_to_excel.assert_called_once_with("test.xlsx", index=False)


class TestJSONHandler(unittest.TestCase):

    @patch("app.file_handler.fileHandler.pd.read_json")
    def test_load_data(self, mock_read_json):
        mock_read_json.return_value = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        handler = JSONHandler("test.json")
        data = handler.load_data()
        mock_read_json.assert_called_once_with("test.json")
        pd.testing.assert_frame_equal(data, pd.DataFrame({"col1": [1, 2], "col2": [3, 4]}))

    @patch("app.file_handler.fileHandler.pd.DataFrame.to_json")
    def test_save_data(self, mock_to_json):
        handler = JSONHandler("test.json")
        data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        handler.save_data(data)
        mock_to_json.assert_called_once_with("test.json")


class TestFileHandlerFunctions(unittest.TestCase):

    @patch("app.file_handler.fileHandler.CSVHandler.load_data")
    @patch("app.file_handler.fileHandler.CSVHandler.save_data")
    def test_import_data(self, mock_save_data, mock_load_data):
        mock_load_data.return_value = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        import_data("source.csv", "destination.csv", "csv")
        mock_load_data.assert_called_once()
        mock_save_data.assert_called_once()

    @patch("app.file_handler.fileHandler.ExcelHandler.load_data")
    @patch("app.file_handler.fileHandler.ExcelHandler.save_data")
    def test_export_data(self, mock_save_data, mock_load_data):
        data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        export_data(data, "destination.xlsx", "excel")
        mock_save_data.assert_called_once()


class TestGetHandler(unittest.TestCase):

    def test_get_handler_csv(self):
        handler = get_handler("csv", "test.csv")
        self.assertIsInstance(handler, CSVHandler)

    def test_get_handler_excel(self):
        handler = get_handler("excel", "test.xlsx")
        self.assertIsInstance(handler, ExcelHandler)

    def test_get_handler_json(self):
        handler = get_handler("json", "test.json")
        self.assertIsInstance(handler, JSONHandler)

    def test_get_handler_invalid(self):
        with self.assertRaises(ValueError):
            get_handler("txt", "test.txt")


if __name__ == '__main__':
    unittest.main()
