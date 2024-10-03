import click
import pandas as pd
from .reporter import create_combined_summary_report, generate_pdf_report, generate_txt_report

@click.group(
    help="""
    **Report Generation Commands**

    This group provides commands for generating detailed summary reports from a dataset in various formats.

    ### Available Reports:

    - **PDF Report**: A comprehensive PDF report with sections like Descriptive Statistics, Correlation Matrices, Missing Values, and Outlier Analysis.
    - **TXT Report**: A simple text-based summary report with similar sections as the PDF.

    ### Examples:

    1. **Create a Summary Report in PDF**:
    \b
    python cmd.py report generate-pdf data.csv --output_pdf summary_report.pdf

    2. **Create a TXT Report**:
    \b
    python cmd.py report generate-txt data.csv --output_txt summary_report.txt
    """
)
def cli():
    """A command-line interface for generating summary reports and PDF/TXT files."""
    pass

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output_summary', default=None, type=click.Path(), help='Path to save the summary CSV file (optional).')
def create_summary(input_file, output_summary):
    """
    Create a combined summary report and display the results.

    Args:
        input_file (str): The input CSV file path.
        output_summary (str, optional): The output path for saving the summary CSV.
    """
    data = pd.read_csv(input_file)
    report_sections = create_combined_summary_report(data)

    # Display the generated summary
    for section, content in report_sections.items():
        print(f"Section: {section}")
        for row in content:
            print(" | ".join(map(str, row)))
        print("\n")

    # Save summary as CSV if specified
    if output_summary:
        summary_df = pd.DataFrame({section: pd.Series(content) for section, content in report_sections.items()})
        summary_df.to_csv(output_summary, index=False)
        print(f"Summary saved to {output_summary}")

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output_pdf', default='report.pdf', type=click.Path(), help='Path to save the PDF report.')
def generate_pdf(input_file, output_pdf):
    """
    Generate a PDF report from the input CSV file.

    Args:
        input_file (str): The input CSV file path.
        output_pdf (str): The output path for saving the PDF report.
    """
    data = pd.read_csv(input_file)
    report_sections = create_combined_summary_report(data)
    generate_pdf_report(report_sections, pdf_file=output_pdf, data_frame=data)
    print(f"PDF report generated and saved to {output_pdf}")

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output_txt', default='report.txt', type=click.Path(), help='Path to save the TXT report.')
def generate_txt(input_file, output_txt):
    """
    Generate a TXT report from the input CSV file.

    Args:
        input_file (str): The input CSV file path.
        output_txt (str): The output path for saving the TXT report.
    """
    data = pd.read_csv(input_file)
    report_sections = create_combined_summary_report(data)
    generate_txt_report(report_sections, txt_file=output_txt)
    print(f"TXT report generated and saved to {output_txt}")

# Adding commands to the main CLI group
cli.add_command(create_summary)
cli.add_command(generate_pdf)
cli.add_command(generate_txt)

if __name__ == '__main__':
    cli()
