import argparse
import os
import pandas as pd
from src.reporter.reporter import generate_pdf_report, create_combined_summary_report
from src.file_handler.fileHandler import get_handler, determine_file_format
from src.utils.exceptions import FileNotFoundError, UnsupportedFileFormatError
from rich.console import Console
from rich.progress import track
from rich.traceback import install

console = Console()
install()

def reporting_command(subparsers):
    """
    Adds a subcommand for generating a report to the argument parser.

    Args:
        subparsers (argparse._SubParsersAction): The subparsers object from argparse.

    This function sets up the 'report' subcommand for generating a report.
    It adds arguments for the input file path, output file path, and output format.
    """
    parser = subparsers.add_parser('report', help="Generate a report")
    parser.add_argument('input', type=str, help="Path to the input file (CSV or Excel).")
    parser.add_argument('output', type=str, help="Path to the output file where the report will be saved.")
    parser.add_argument('--format', type=str, choices=['txt', 'pdf'], default='txt',
                        help="Format of the output report ('txt' or 'pdf'). Defaults to 'txt'.")

    parser.set_defaults(func=report_command)

def report_command(args):
    """
    Handles the 'report' command to generate and save a report.

    Args:
        args (argparse.Namespace): The parsed command-line arguments.

    This function calls `generate_report` to create a report based on the input file and format.
    It then writes the report content to the specified output file.
    In case of errors, it provides appropriate messages to the user.

    Raises:
        FileNotFoundError: If the input file does not exist.
        UnsupportedFileFormatError: If the file format is unsupported.
        IOError: If there's an issue with file operations.
        Exception: For any other unexpected errors.
    """
    try:
        file_format = determine_file_format(args.input)
        handler = get_handler(file_format, args.input)
        data_frame = handler.load_data()

        report_sections = create_combined_summary_report(data_frame)

        if args.format == 'pdf':
            generate_pdf_report(report_sections, args.output, data_frame)
            console.print(f"[bold green]PDF report successfully saved to {args.output}[/bold green]")
        elif args.format == 'txt':
            raise NotImplementedError("Text report generation is not implemented.")

    except FileNotFoundError as e:
        console.print(f"[bold red]Error: Input file not found - {e.file_path}[/bold red]")
    except UnsupportedFileFormatError as e:
        console.print(f"[bold red]Error: {e.message}[/bold red]")
    except IOError as e:
        console.print(f"[bold red]Error: File operation failed - {e}[/bold red]")
    except NotImplementedError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")
