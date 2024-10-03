import re
import pandas as pd

class Standardizer:
    """
    Standardizes formats for dates and currency.
    """

    def __init__(self, data):
        self.data = data.copy()

    def standardize_date(self, column, date_format='%Y-%m-%d'):
        """
        Standardize the format of date columns.

        Args:
            column (str): The name of the date column.
            date_format (str, optional): The desired output format. Defaults to '%Y-%m-%d'.

        Returns:
            self: Data with standardized date formats.
        """
        self.data[column] = pd.to_datetime(self.data[column], errors='coerce').dt.strftime(date_format)
        return self

    def standardize_currency(self, column):
        """
        Standardize currency format by removing symbols and converting to float.

        Args:
            column (str): The name of the currency column.

        Returns:
            self: Data with currency values standardized.
        """
        self.data[column] = self.data[column].replace('[\\$,]', '', regex=True).astype(float)
        return self


class Basic_Cleaner:
    """
    Handles basic cleaning tasks such as trimming whitespace, handling missing values, and regex cleaning.
    """
    def __init__(self, data):
        self.data = data.copy()

    def trim_spaces(self):
        """
        Trim extra spaces in all string columns.

        Returns:
            self: Data with trimmed string values.
        """
        self.data = self.data.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)
        return self

    def handle_missing_values(self, method='drop', fill_value=None):
        """
        Handle missing values in the data.

        Args:
            method (str, optional): The method to handle missing values ('drop' or 'fill'). Defaults to 'drop'.
            fill_value (any, optional): The value to fill missing data with if 'fill' is chosen.

        Returns:
            self: Data with missing values handled.
        """
        if method == 'drop':
            self.data = self.data.dropna()
        elif method == 'fill' and fill_value is not None:
            self.data = self.data.fillna(fill_value)
        return self

    def apply_regex_cleaning(self, column, pattern, replacement):
        """
        Apply regex cleaning to a specified column.

        Args:
            column (str): The column to apply the regex to.
            pattern (str): The regex pattern to search for.
            replacement (str): The string to replace the pattern with.

        Returns:
            self: Data with the cleaned column.
        """
        self.data[column] = self.data[column].replace(pattern, replacement, regex=True)
        return self


class TextOperations:
    """
    Performs text manipulation tasks such as changing case, applying regex cleaning, and handling text formatting.
    """

    def __init__(self, data):
        self.data = data.copy()

    def change_case(self, operation='lower', columns=None):
        """
        Change the case of text in specified columns.

        Args:
            operation (str, optional): The case transformation to apply ('lower', 'upper', 'title', 'capitalize').
            columns (list, optional): List of columns to apply the transformation. If None, all text columns are used.

        Returns:
            self: Data with transformed text.
        """
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


