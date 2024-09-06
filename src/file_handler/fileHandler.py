import pandas as pd

class DataHandler:
    """Base class for data import and export."""

    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        """Method to load data, to be implemented by subclasses."""
        raise NotImplementedError("Subclasses should implement this method")

    def save_data(self, data, output_filepath=None):
        """Method to save data, to be implemented by subclasses."""
        raise NotImplementedError("Subclasses should implement this method")

    def _validate_data(self, data):
        """Basic validation for data."""
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame")

class CSVHandler(DataHandler):
    """Handles importing and exporting CSV files."""

    def load_data(self):
        """Load data from a CSV file."""
        try:
            data = pd.read_csv(self.filepath)
            return data
        except Exception as e:
            raise IOError(f"Failed to load CSV file: {e}")

    def save_data(self, data, output_filepath=None):
        """Save data to a CSV file."""
        self._validate_data(data)
        output_filepath = output_filepath or self.filepath
        try:
            data.to_csv(output_filepath, index=False)
        except Exception as e:
            raise IOError(f"Failed to save CSV file: {e}")

class ExcelHandler(DataHandler):
    """Handles importing and exporting Excel files."""

    def load_data(self, sheet_name=0):
        """Load data from an Excel file."""
        try:
            data = pd.read_excel(self.filepath, sheet_name=sheet_name)
            return data
        except Exception as e:
            raise IOError(f"Failed to load Excel file: {e}")

    def save_data(self, data, output_filepath=None):
        """Save data to an Excel file."""
        self._validate_data(data)
        output_filepath = output_filepath or self.filepath
        try:
            data.to_excel(output_filepath, index=False)
        except Exception as e:
            raise IOError(f"Failed to save Excel file: {e}")

class JSONHandler(DataHandler):
    """Handles importing and exporting JSON files."""

    def load_data(self):
        """Load data from a JSON file."""
        try:
            data = pd.read_json(self.filepath)
            return data
        except Exception as e:
            raise IOError(f"Failed to load JSON file: {e}")

    def save_data(self, data, output_filepath=None):
        """Save data to a JSON file."""
        self._validate_data(data)
        output_filepath = output_filepath or self.filepath
        try:
            data.to_json(output_filepath)
        except Exception as e:
            raise IOError(f"Failed to save JSON file: {e}")

def get_handler(file_format, file_path):
    """Return the appropriate DataHandler based on the file format."""
    if file_format == 'csv':
        return CSVHandler(file_path)
    elif file_format == 'excel':
        return ExcelHandler(file_path)
    elif file_format == 'json':
        return JSONHandler(file_path)
    else:
        raise ValueError("Unsupported file format")

def import_data(source, destination, file_format):
    """Import data from source to destination based on the file format."""
    handler = get_handler(file_format, source)
    data = handler.load_data()

    export_handler = get_handler(file_format, destination)
    export_handler.save_data(data)

def export_data(data, destination, file_format):
    """Export data to the destination based on the file format."""
    handler = get_handler(file_format, destination)
    handler.save_data(data)
