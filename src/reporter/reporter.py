import pandas as pd
import io
from typing import Optional
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_report(input_file: str, output_format: Optional[str] = 'txt') -> str:
    """
    Generates a report from the data in the input file.

    Args:
        input_file (str): Path to the input file (CSV or Excel).
        output_format (str, optional): Format of the output report ('txt' or 'pdf'). Defaults to 'txt'.

    Returns:
        str: The generated report content as a string (if 'txt') or a message indicating PDF creation.
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} not found.")

    data_frame = load_data(input_file)
    report_content = create_report(data_frame)

    if output_format == 'pdf':
        pdf_file = input_file.replace('.csv', '.pdf').replace('.xlsx', '.pdf')
        generate_pdf_report(report_content, pdf_file)
        return f"PDF report generated: {pdf_file}"

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
    report_buffer = io.StringIO()

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

        if pd.api.types.is_numeric_dtype(data_frame[column]):
            report_buffer.write(f"  - Mean: {data_frame[column].mean()}\n")
            report_buffer.write(f"  - Median: {data_frame[column].median()}\n")
            report_buffer.write(f"  - Min: {data_frame[column].min()}\n")
            report_buffer.write(f"  - Max: {data_frame[column].max()}\n")

    return report_buffer.getvalue()

def generate_pdf_report(report_content: str, pdf_file: str):
    """
    Generates a PDF report from the given report content.

    Args:
        report_content (str): The content to be included in the PDF report.
        pdf_file (str): The path where the PDF report will be saved.
    """
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 40, "Summary Report")

    c.setFont("Helvetica", 10)
    text = c.beginText(40, height - 60)
    text.setTextOrigin(40, height - 60)
    text.setLeading(14)

    for line in report_content.splitlines():
        if text.getY() < 50:  
            c.drawText(text)
            c.showPage()
            text = c.beginText(40, height - 60)
            text.setLeading(14)
        text.textLine(line)

    c.drawText(text)
    c.showPage()
    c.save()
