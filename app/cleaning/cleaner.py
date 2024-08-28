import pandas as pd
import re
import os

class DataCleaner:
    def __init__(self, data):
        self.data = data
    
    def clean_duplicates(self):
        """Remove duplicates from the data."""
        if subset:
            self.df = self.df.drop_duplicates(subset=subset)
        else:
            self.df = self.df.drop_duplicates()
        self.df.to_csv(self.output_file, index=False)

        self.data = self.data.drop_duplicates()
        return self.data
    
    def clean_missing_values(self):
        """Handle missing values by removing or filling them."""
        self.data = self.data.dropna()
        return self.data
    
    def clean_all(self):
        """Apply all cleaning methods."""
        self.clean_duplicates()
        self.clean_missing_values()
        return self.data
    
    def regex_clean(self, pattern):
        regex = re.compile(pattern)
        self.df = self.df.applymap(lambda x: regex.sub('', str(x)) if isinstance(x, str) else x)
        self.df.to_csv(self.output_file, index=False)