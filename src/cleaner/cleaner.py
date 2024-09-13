import re
import pandas as pd

class DataCleaner:
    """
    Orchestrates the overall cleaning process by calling the appropriate cleaning methods from different classes.
    """

    def __init__(self, data):
        self.data = data.copy()
        self.basic_cleaner = BasicCleaner(self.data)
        self.error_handler = ErrorHandler(self.data)
        self.text_operations = TextOperations(self.data)
        self.format_standardizer = FormatStandardizer(self.data)
        self.outlier_handler = OutlierHandler(self.data)
        self.missing_value_handler = MissingValueHandler(self.data)

    def clean_all(self):
        """
        Apply all cleaning methods in sequence, including handling missing values, correcting text data, and standardizing formats.

        Returns:
            self: The cleaned data.
        """
        self.data = self.basic_cleaner.clean_column_names().data
        self.data = self.basic_cleaner.basic_cleaning().data
        self.data = self.error_handler.clean_duplicates().data
        self.data = self.error_handler.validate_data().data
        self.data = self.missing_value_handler.handle_missing_values().data
        self.data = self.outlier_handler.handle_outliers().data

        return self


class BasicCleaner:
    """
    Handles basic cleaning tasks such as trimming whitespace and normalizing column names.
    """

    def __init__(self, data):
        self.data = data

    def basic_cleaning(self):
        """
        Trim extra spaces in all string columns.

        Returns:
            self: Data with trimmed string values.
        """
        self.data = self.data.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)
        return self

    def clean_column_names(self):
        """
        Standardize column names by trimming whitespace, converting to lowercase, and replacing spaces with underscores.

        Returns:
            self: Data with cleaned column names.
        """
        self.data.columns = self.data.columns.str.strip().str.lower().str.replace(' ', '_')
        return self


class ErrorHandler:
    """
    Manages error handling tasks such as removing duplicates and validating data.
    """

    def __init__(self, data):
        self.data = data.copy()

    def clean_duplicates(self, subset=None):
        """
        Remove duplicate rows from the data.

        Args:
            subset (list, optional): Columns to consider when identifying duplicates. If None, all columns are used.

        Returns:
            self: Data with duplicates removed.
        """
        self.data = self.data.drop_duplicates(subset=subset)
        return self

    def validate_data(self):
        """
        Identify and correct errors, ensuring data integrity. For example, converts string-based numeric columns to numeric types.

        Returns:
            self: Data with validated types and errors corrected.
        """
        for col in self.data.columns:
            if self.data[col].dtype == 'object':
                try:
                    self.data[col] = pd.to_numeric(self.data[col], errors='ignore')
                except ValueError:
                    pass
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


class FormatStandardizer:
    """
    Standardizes formats for dates, currency, and other types of structured data.
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


class MissingValueHandler:
    """
    Handles missing values by either dropping or imputing them.
    """

    def __init__(self, data):
        self.data = data.copy()

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


class OutlierHandler:
    """
    Identifies and handles outliers in the data.
    """

    def __init__(self, data):
        self.data = data.copy()

    def handle_outliers(self, method='remove', columns=None, threshold=3):
        """
        Handle outliers in numeric columns using the Z-score method.

        Args:
            method (str, optional): The method to handle outliers ('remove' or 'cap'). Defaults to 'remove'.
            columns (list, optional): List of columns to check for outliers. If None, all numeric columns are used.
            threshold (int, optional): Z-score threshold to define outliers. Defaults to 3.

        Returns:
            self: Data with outliers handled.
        """
        if columns is None:
            columns = self.data.select_dtypes(include=[np.number]).columns

        for col in columns:
            z_scores = np.abs((self.data[col] - self.data[col].mean()) / self.data[col].std())
            if method == 'remove':
                self.data = self.data[z_scores < threshold]
            elif method == 'cap':
                self.data[col] = np.where(z_scores > threshold, self.data[col].mean(), self.data[col])
        return self
