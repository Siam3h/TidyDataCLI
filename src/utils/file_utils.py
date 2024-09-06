import os
import gzip
import pandas as pd

def read_file(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format")

def write_file(file_path, data_frame):
    if file_path.endswith('.csv'):
        data_frame.to_csv(file_path, index=False)
    elif file_path.endswith('.xlsx'):
        data_frame.to_excel(file_path, index=False)
    else:
        raise ValueError("Unsupported file format")

def compress_file(file_path):
    with open(file_path, 'rb') as f_in:
        with gzip.open(file_path + '.gz', 'wb') as f_out:
            f_out.writelines(f_in)

def decompress_file(file_path):
    if not file_path.endswith('.gz'):
        raise ValueError("File must be in .gz format")
    with gzip.open(file_path, 'rb') as f_in:
        with open(file_path[:-3], 'wb') as f_out:
            f_out.writelines(f_in)
