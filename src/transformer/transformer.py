import pandas as pd
from .exception_utils import ColumnNotFoundError, DataValidationError

class DataTransformer:
    """Class to handle various data transformations on Pandas DataFrames."""

    def sort_data(self, data: pd.DataFrame, by: list, ascending=True) -> pd.DataFrame:
        """
        Sort the DataFrame by specified columns.

        Args:
            data (pd.DataFrame): The DataFrame to be sorted.
            by (list): List of column names to sort by.
            ascending (bool, optional): Sort order. True for ascending, False for descending. Defaults to True.

        Returns:
            pd.DataFrame: The sorted DataFrame.

        Raises:
            ColumnNotFoundError: If one or more columns to sort by are not present in the DataFrame.
        """
        if not isinstance(by, list):
            by = [by]

        if not all(col in data.columns for col in by):
            raise ColumnNotFoundError(', '.join([col for col in by if col not in data.columns]))

        return data.sort_values(by=by, ascending=ascending)

    def filter_data(self, data: pd.DataFrame, condition: str) -> pd.DataFrame:
        """
        Filter the DataFrame based on a condition.

        Args:
            data (pd.DataFrame): The DataFrame to be filtered.
            condition (str): The condition for filtering, expressed as a query string.

        Returns:
            pd.DataFrame: The filtered DataFrame.

        Raises:
            DataValidationError: If the query condition is invalid or results in an error.
        """
        try:
            return data.query(condition)
        except Exception as e:
            raise DataValidationError(f"Invalid query condition: {condition}. Error: {str(e)}")

    def apply_custom_transformation(self, data: pd.DataFrame, func) -> pd.DataFrame:
        """
        Apply a custom transformation function to the DataFrame.

        Args:
            data (pd.DataFrame): The DataFrame to transform.
            func (callable): A function to apply to each element of the DataFrame.

        Returns:
            pd.DataFrame: The transformed DataFrame.

        Raises:
            DataValidationError: If the provided transformation function is not callable.
        """
        if not callable(func):
            raise DataValidationError("Provided transformation function is not callable.")
        return data.apply(func)

    def add_column(self, data: pd.DataFrame, column_name: str, value) -> pd.DataFrame:
        """
        Add a new column to the DataFrame with a specified value.

        Args:
            data (pd.DataFrame): The DataFrame to modify.
            column_name (str): The name of the new column.
            value: The value to be assigned to the new column. Can be a single value or a list/Series with length equal to the DataFrame.

        Returns:
            pd.DataFrame: The DataFrame with the new column added.

        Raises:
            ColumnNotFoundError: If the column already exists in the DataFrame.
        """
        if column_name in data.columns:
            raise ColumnNotFoundError(column_name)
        data[column_name] = value
        return data

    def drop_column(self, data: pd.DataFrame, column_name: str) -> pd.DataFrame:
        """
        Drop a column from the DataFrame.

        Args:
            data (pd.DataFrame): The DataFrame to modify.
            column_name (str): The name of the column to drop.

        Returns:
            pd.DataFrame: The DataFrame with the specified column dropped.

        Raises:
            ColumnNotFoundError: If the column to be dropped does not exist in the DataFrame.
        """
        if column_name not in data.columns:
            raise ColumnNotFoundError(column_name)
        return data.drop(columns=[column_name])

    def rename_column(self, data: pd.DataFrame, old_name: str, new_name: str) -> pd.DataFrame:
        """
        Rename a column in the DataFrame.

        Args:
            data (pd.DataFrame): The DataFrame to modify.
            old_name (str): The current name of the column to rename.
            new_name (str): The new name for the column.

        Returns:
            pd.DataFrame: The DataFrame with the column renamed.

        Raises:
            ColumnNotFoundError: If the column to be renamed does not exist in the DataFrame.
        """
        if old_name not in data.columns:
            raise ColumnNotFoundError(old_name)
        return data.rename(columns={old_name: new_name})

    def handle_missing_values(self, data: pd.DataFrame, method: str = 'drop', fill_value=None) -> pd.DataFrame:
        """
        Handle missing values in the DataFrame.

        Args:
            data (pd.DataFrame): The DataFrame to modify.
            method (str, optional): Method to handle missing values. 'drop' to remove rows with missing values,
                                    'fill' to fill missing values with a specified value. Defaults to 'drop'.
            fill_value: The value to fill missing values with, if method is 'fill'.

        Returns:
            pd.DataFrame: The DataFrame with missing values handled.

        Raises:
            DataValidationError: If an invalid method is specified or fill_value is not provided when method is 'fill'.
        """
        if method == 'drop':
            return data.dropna()
        elif method == 'fill':
            if fill_value is None:
                raise DataValidationError("fill_value must be provided if method is 'fill'.")
            return data.fillna(fill_value)
        else:
            raise DataValidationError("Invalid method. Use 'drop' or 'fill'.")

    def view_head(self, data: pd.DataFrame, n: int = 5) -> pd.DataFrame:
        """
        View the first `n` rows of the DataFrame.

        Args:
            data (pd.DataFrame): The DataFrame to view.
            n (int, optional): The number of rows to display. Defaults to 5.

        Returns:
            pd.DataFrame: The first `n` rows of the DataFrame.

        Raises:
            DataValidationError: If `n` is not a positive integer.
        """
        if not isinstance(n, int) or n <= 0:
            raise DataValidationError("Parameter 'n' must be a positive integer.")
        return data.head(n)

    def view_tail(self, data: pd.DataFrame, n: int = 5) -> pd.DataFrame:
        """
        View the last `n` rows of the DataFrame.

        Args:
            data (pd.DataFrame): The DataFrame to view.
            n (int, optional): The number of rows to display. Defaults to 5.

        Returns:
            pd.DataFrame: The last `n` rows of the DataFrame.

        Raises:
            DataValidationError: If `n` is not a positive integer.
        """
        if not isinstance(n, int) or n <= 0:
            raise DataValidationError("Parameter 'n' must be a positive integer.")
        return data.tail(n)
