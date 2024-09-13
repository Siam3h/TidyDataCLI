class DataVisualizerError(Exception):
    """Base class for exceptions in the DataVisualizer class."""
    def __init__(self, message="An error occurred in DataVisualizer."):
        super().__init__(message)
        self.message = message

class ColumnNotFoundError(DataVisualizerError):
    """Exception raised when a required column is missing in the data."""
    def __init__(self, column_name, message=None):
        message = message or f"Column '{column_name}' not found in the dataset."
        super().__init__(message)
        self.column_name = column_name

class DataMismatchError(DataVisualizerError):
    """Exception raised when there is a mismatch between dataset columns."""
    def __init__(self, column_1, column_2, message=None):
        message = message or f"Mismatch between columns '{column_1}' and '{column_2}'."
        super().__init__(message)
        self.column_1 = column_1
        self.column_2 = column_2

class UnsupportedFormatError(DataVisualizerError):
    """Exception raised when an unsupported format is used for exporting charts or tables."""
    def __init__(self, format_type, supported_formats, message=None):
        message = message or f"Unsupported format: '{format_type}'. Supported formats are: {', '.join(supported_formats)}."
        super().__init__(message)
        self.format_type = format_type
        self.supported_formats = supported_formats

class DataFileError(Exception):
    """Base class for exceptions related to data files."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class FileNotFoundError(DataFileError):
    """Exception raised for file not found errors."""
    def __init__(self, file_path):
        super().__init__(f"File not found: {file_path}")
        self.file_path = file_path

class UnsupportedFileFormatError(DataFileError):
    """Exception raised for unsupported file format errors."""
    def __init__(self, file_format):
        super().__init__(f"Unsupported file format: {file_format}")
        self.file_format = file_format

class DataValidationError(DataFileError):
    """Exception raised for data validation errors."""
    def __init__(self, message):
        super().__init__(f"Data validation error: {message}")
        self.message = message

def render_error_message(exception):
    """
    Renders a user-friendly error message based on the provided exception.

    Parameters:
    - exception (Exception): The exception that was raised.

    Returns:
    - str: A formatted string that provides a more user-understandable explanation of the error.
    """
    if isinstance(exception, ColumnNotFoundError):
        return f"Error: {exception.message} Please check the column names in your dataset."
    elif isinstance(exception, DataMismatchError):
        return f"Error: {exception.message} Please ensure the columns are properly aligned."
    elif isinstance(exception, UnsupportedFormatError):
        return f"Error: {exception.message} Please choose a valid format."
    elif isinstance(exception, FileNotFoundError):
        return f"Error: {exception.message} Please check the file path."
    elif isinstance(exception, UnsupportedFileFormatError):
        return f"Error: {exception.message} Please provide a file with a supported format."
    elif isinstance(exception, DataValidationError):
        return f"Error: {exception.message} Please validate your data."
    else:
        return f"An unexpected error occurred: {str(exception)}"
