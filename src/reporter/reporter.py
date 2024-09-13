import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from src.utils.file_utils import read_file
from src.utils.exceptions import FileNotFoundError, UnsupportedFileFormatError

def create_combined_summary_report(data_frame: pd.DataFrame) -> dict:
    """
    Creates a comprehensive summary report from the DataFrame.

    Args:
        data_frame (pd.DataFrame): Data to be included in the report.

    Returns:
        dict: Report content organized by sections.
    """
    report_sections = {}

    desc_stats = data_frame.describe(include='all').T.round(2)

    desc_stats['Data Type'] = data_frame.dtypes
    desc_stats['Unique Values'] = data_frame.nunique()

    report_sections['Descriptive Statistics'] = desc_stats.reset_index().values.tolist()

    correlation_matrix = data_frame.corr().round(2)
    report_sections['Correlation Matrix'] = correlation_matrix.reset_index().values.tolist()

    missing_values = data_frame.isnull().sum()
    total_cells = data_frame.size
    total_missing = missing_values.sum()
    missing_summary = [[f"Total Missing Values: {total_missing}"],
                       [f"Percentage of Missing Values: {total_missing / total_cells * 100:.2f}%"]]

    for column, value in missing_values.items():
        if value > 0:
            missing_summary.append([f"Column: {column}", f"Missing Values: {value}", f"Percentage: {value / len(data_frame) * 100:.2f}%"])

    report_sections['Missing Values Summary'] = missing_summary if len(missing_summary) > 1 else [["No missing values"]]

    categorical_cols = data_frame.select_dtypes(include=['object', 'category']).columns
    value_counts_summary = []
    for column in categorical_cols:
        value_counts_summary.append([f"Column: {column}"])
        value_counts = data_frame[column].value_counts().reset_index().values.tolist()
        value_counts_summary.extend(value_counts)

    report_sections['Value Counts Summary'] = value_counts_summary if value_counts_summary else [["No categorical columns"]]

    outliers_summary = [['Column', 'Outliers Count', 'Outliers Percentage']]
    for column in data_frame.select_dtypes(include=[float, int]).columns:
        q1 = data_frame[column].quantile(0.25)
        q3 = data_frame[column].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = data_frame[(data_frame[column] < lower_bound) | (data_frame[column] > upper_bound)]
        outliers_summary.append([column, len(outliers), f"{len(outliers) / len(data_frame) * 100:.2f}%"])

    report_sections['Outliers Summary'] = outliers_summary if len(outliers_summary) > 1 else [["No outliers found"]]

    return report_sections


def generate_pdf_report(report_sections: dict, pdf_file: str, data_frame: pd.DataFrame):
    """
    Generates a PDF report from the given report sections.

    Args:
        report_sections (dict): The content to be included in the PDF report, organized by section.
        pdf_file (str): The path where the PDF report will be saved.
        data_frame (pd.DataFrame): The DataFrame used for adding column headers dynamically.
    """
    try:
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        content = []

        title_style = ParagraphStyle('Title', fontSize=18, alignment=TA_CENTER, spaceAfter=12, fontName='Helvetica-Bold')
        content.append(Paragraph("Summary Report", title_style))
        content.append(Spacer(1, 12))

        for section_title, section_content in report_sections.items():
            section_style = ParagraphStyle('Heading2', alignment=TA_CENTER, fontSize=12, spaceAfter=12, fontName='Helvetica-Bold')
            content.append(Paragraph(section_title, section_style))
            content.append(Spacer(1, 12))

            if not section_content:
                content.append(Paragraph("No data available.", styles['BodyText']))
                content.append(Spacer(1, 12))
                continue

            table_data = section_content

            if section_title == 'Descriptive Statistics':
                headers = ['Field', 'Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max', 'Data Type', 'Unique Values']
                table_data.insert(0, headers)
            elif section_title == 'Correlation Matrix':
                headers = ['Field'] + data_frame.columns.tolist()
                table_data.insert(0, headers)

            table = Table(table_data, repeatRows=1)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.white),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ]))

            content.append(KeepTogether(table))
            content.append(Spacer(1, 12))

        doc.build(content)
    except Exception as e:
        raise RuntimeError(f"Failed to generate PDF report: {e}")
