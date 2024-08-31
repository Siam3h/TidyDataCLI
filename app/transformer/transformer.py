import pandas as pd

class DataTransformer:
    """Class to handle various data transformations."""
    
    def __init__(self, data):
        self.data = data
    
    def sort_data(self, by, ascending=True):
        """Sort the DataFrame by specified columns."""
        if isinstance(by, list):
            self.data = self.data.sort_values(by=by, ascending=ascending)
        else:
            self.data = self.data.sort_values(by=[by], ascending=ascending)
        return self.data
    
    def filter_data(self, condition):
        """Filter the DataFrame based on a condition."""
        self.data = self.data.query(condition)
        return self.data
    
    def apply_custom_transformation(self, func):
        """Apply a custom transformation function to the DataFrame."""
        self.data = self.data.apply(func)
        return self.data
