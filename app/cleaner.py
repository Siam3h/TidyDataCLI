import pandas as pd
import re
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx files.")

def save_data(data, output_file):
    if output_file.endswith('.csv'):
        data.to_csv(output_file, index=False)
    elif output_file.endswith('.xlsx'):
        data.to_excel(output_file, index=False)
    else:
        raise ValueError("Unsupported file format for saving. Use .csv or .xlsx files.")

def clean_data(data, regex_pattern=None):
    data = data.drop_duplicates()
    if regex_pattern:
        data = data.applymap(lambda x: re.sub(regex_pattern, '', str(x)) if isinstance(x, str) else x)
    return data

def plot_column_frequency(data, column_name, output_dir): 
    if column_name not in data.columns:
        raise ValueError(f"Column '{column_name}' not found in data.")
    
    freq = data[column_name].value_counts()
    plt.figure(figsize=(10, 6))
    freq.plot(kind='bar')
    plt.title(f"Frequency of {column_name}")
    plt.ylabel("Frequency")
    plt.xlabel(column_name)
    
    output_file = os.path.join(output_dir, f"{column_name}_frequency.png")
    plt.savefig(output_file)
    plt.close()
    return output_file
