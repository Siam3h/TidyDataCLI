import re
import pandas as pd

class DataCleaner:
    """Main class that orchestrates the overall cleaning process."""
    def __init__(self, data):
        self.data = data.copy()
        self.basic_cleaner = BasicCleaner(self.data)
        self.error_handler = ErrorHandler(self.data)
        self.text_operations = TextOperations(self.data)
        self.format_standardizer = FormatStandardizer(self.data)
        self.data_splitter = DataSplitter(self.data)

    def clean_all(self):
        """Apply all cleaning methods."""
        self.data = self.basic_cleaner.clean_column_names().data
        self.data = self.basic_cleaner.basic_cleaning().data
        self.data = self.error_handler.clean_duplicates().data
        self.data = self.error_handler.validate_data().data
        return self

class BasicCleaner:
    """Handles basic cleaning tasks like trimming spaces."""
    def __init__(self, data):
        self.data = data

    def basic_cleaning(self):
        """Trim extra spaces in all string columns."""
        self.data = self.data.apply(lambda col: col.strip() if isinstance(col,str) else col)
        return self

    def clean_column_names(self):
        """Standardize column names by stripping whitespace, converting to lowercase, and removing spaces."""
        self.data.columns = self.data.columns.str.strip().str.lower().str.replace(' ', '')
        return self

class ErrorHandler:
    """Manages error handling, validation, and duplicate removal."""
    def __init__(self, data):
        self.data = data.copy()

    def clean_duplicates(self, subset=None):
        """Remove duplicate rows from the data."""
        self.data = self.data.drop_duplicates(subset=subset)
        return self

    def validate_data(self):
        """Identify and correct errors, ensuring data integrity."""
        for col in self.data.columns:
            if col == 'age':
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
        self.data = self.data.dropna()
        return self

class TextOperations:
    """Performs text manipulation tasks like changing case and applying text formulas."""
    def __init__(self, data):
        self.data = data.copy()

    def change_case(self, operation='lower', columns=None):
        """Manipulate and format text data by changing the case."""
        if columns is None:
            columns = self.data.select_dtypes(include=['object']).columns

        operations = {
            'lower': str.lower,
            'upper': str.upper,
            'title': str.title,
            'capitalize': str.capitalize
        }

        func = operations.get(operation)
        if func:
            for col in columns:
                self.data[col] = self.data[col].astype(str).apply(func)
        return self

class FormatStandardizer:
    """Standardizes formats for dates, currency, and other data types."""
    def __init__(self, data):
        self.data = data.copy()

    def standardize_date(self, column, date_format='%Y-%m-%d'):
        """Standardize date formats."""
        self.data[column] = pd.to_datetime(self.data[column], errors='coerce').dt.strftime(date_format)
        return self

    def standardize_currency(self, column):
        """Standardize currency formats by removing symbols and converting to float."""
        self.data[column] = self.data[column].replace('[\\$,]', '', regex=True).astype(float)
        return self

class DataSplitter:
	def __init__(self, data):
		self.data = data

"""
Commented out code block
class DataSplitter:
    Splits delimited data into multiple columns.
    def __init__(self, data):
        self.data = data.copy()

    def split_delimited_data(self, column, delimiter=',', new_columns=None):
        Split a column containing delimited data into multiple columns.
        split_data = self.data[column].str.split(delimiter, expand=True)
        if new_columns and len(new_columns) == split_data.shape[0]:
            split_data.columns = new_columns
        else:
            split_data.columns = [f'{column}_part_{i+1}' for i in range(split_data.shape[1])]
        self.data = pd.concat([self.data, split_data], axis=1).drop(columns=[column])
        return self
"""
