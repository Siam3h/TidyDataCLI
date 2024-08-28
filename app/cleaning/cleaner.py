import pandas as pd
import re
import os

class DataCleaner:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.df = pd.read_csv(input_file) if input_file.endswith('.csv') else pd.read_excel(input_file)

    def remove_duplicates(self, subset=None):
        if subset:
            self.df = self.df.drop_duplicates(subset=subset)
        else:
            self.df = self.df.drop_duplicates()
        self.df.to_csv(self.output_file, index=False)

    def regex_clean(self, pattern):
        regex = re.compile(pattern)
        self.df = self.df.applymap(lambda x: regex.sub('', str(x)) if isinstance(x, str) else x)
        self.df.to_csv(self.output_file, index=False)

    
