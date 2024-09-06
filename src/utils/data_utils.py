import pandas as pd

def filter_data(data_frame, condition):
    return data_frame.query(condition)

def clean_data(data_frame):
    return data_frame.dropna().drop_duplicates()
