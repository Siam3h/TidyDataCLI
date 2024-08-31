import pandas as pd
import io
from typing import Optional

def generate_report(input_file: str, output_format: Optional[str] = 'txt') -> str:
    """
    Generates a report from the data in the input file.

    Args:
        input_file (str): Path to the input file (CSV or Excel).
        output_format (str, optional): Format of the output report ('txt' or 'pdf'). Defaults to 'txt'.

    Returns:
        str: The generated report content as a string.
    """
    data_frame = load_data(input_file)
    report_content = create_report(data_frame)

    if output_format == 'pdf':
        # Here, you would typically generate a PDF report
        # This is a placeholder for PDF generation
        raise NotImplementedError("PDF report generation is not implemented yet.")

    return report_content

def load_data(file_path: str) -> pd.DataFrame:
    """
    Loads data from a CSV or Excel file into a DataFrame.

    Args:
        file_path (str): Path to the data file.

    Returns:
        pd.DataFrame: Data loaded into a DataFrame.
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

def create_report(data_frame: pd.DataFrame) -> str:
    """
    Creates a textual report from the DataFrame.

    Args:
        data_frame (pd.DataFrame): Data to be included in the report.

    Returns:
        str: Report content.
    """
    # Generate a simple summary report
    report_buffer = io.StringIO()

    # Summary statistics
    report_buffer.write("Summary Report\n")
    report_buffer.write("====================\n")
    report_buffer.write(f"Number of Rows: {len(data_frame)}\n")
    report_buffer.write(f"Number of Columns: {len(data_frame.columns)}\n")
    report_buffer.write("\nColumn-wise Summary:\n")

    for column in data_frame.columns:
        report_buffer.write(f"\nColumn: {column}\n")
        report_buffer.write(f"  - Data Type: {data_frame[column].dtype}\n")
        report_buffer.write(f"  - Missing Values: {data_frame[column].isnull().sum()}\n")
        report_buffer.write(f"  - Unique Values: {data_frame[column].nunique()}\n")

    return report_buffer.getvalue()
