import io
import os
from typing import Optional
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from file_utils import read_file
from exceptions import FileNotFoundError, UnsupportedFileFormatError

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
        raise FileNotFoundError(input_file)

    try:
        data_frame = read_file(input_file)
    except ValueError as e:
        raise UnsupportedFileFormatError(file_format=input_file.split('.')[-1]) from e
    except Exception as e:
        return f"An unexpected error occurred: {e}"

    report_content = create_report(data_frame)

    if output_format == 'pdf':
        pdf_file = input_file.rsplit('.', 1)[0] + '.pdf'
        try:
            generate_pdf_report(report_content, pdf_file)
        except Exception as e:
            return f"Failed to generate PDF: {e}"
        return f"PDF report generated: {pdf_file}"

    return report_content

def create_report(data_frame) -> str:
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
    try:
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        content = []

        content.append(Paragraph("Summary Report", styles['Title']))
        content.append(Spacer(1, 12))
        content.append(Paragraph(report_content, styles['BodyText']))

        doc.build(content)
    except Exception as e:
        raise RuntimeError(f"Failed to generate PDF report: {e}")
