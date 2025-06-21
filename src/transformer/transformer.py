import pandas as pd
from src.utils.exceptions import ColumnNotFoundError, DataValidationError

class DataTransformer:
    """Class to handle various data transformations on Pandas DataFrames."""
    
    def __init__(self, data):
        self.data = data.copy()

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

