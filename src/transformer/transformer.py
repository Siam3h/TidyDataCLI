import pandas as pd

class DataTransformer:
    """Class to handle various data transformations."""

    def sort_data(self, data: pd.DataFrame, by: list, ascending=True) -> pd.DataFrame:
        """Sort the DataFrame by specified columns."""
        if not isinstance(by, list):
            by = [by]

        if not all(col in data.columns for col in by):
            raise ValueError("One or more columns to sort by are not present in the data.")

        return data.sort_values(by=by, ascending=ascending)

    def filter_data(self, data: pd.DataFrame, condition: str) -> pd.DataFrame:
        """Filter the DataFrame based on a condition."""
        try:
            return data.query(condition)
        except Exception as e:
            raise ValueError(f"Invalid query condition: {condition}. Error: {str(e)}")

    def apply_custom_transformation(self, data: pd.DataFrame, func) -> pd.DataFrame:
        """Apply a custom transformation function to the DataFrame."""
        if not callable(func):
            raise ValueError("Provided transformation function is not callable.")
        return data.apply(func)
