import pandas as pd

def validate_csv(file_path):
    try:
        pd.read_csv(file_path)
        return True
    except Exception:
        return False

def validate_excel(file_path):
    try:
        pd.read_excel(file_path)
        return True
    except Exception:
        return False

def check_data_integrity(data_frame, required_columns):
    return all(col in data_frame.columns for col in required_columns)
