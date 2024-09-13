import argparse
from reporter import generate_report
from exceptions import FileNotFoundError, UnsupportedFileFormatError
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
        for _ in track(range(1), description="Generating report..."):
            report = generate_report(args.input, output_format=args.format)

        if args.format == 'txt':
            with open(args.output, 'w') as f:
                f.write(report)
            console.print(f"[bold green]Report successfully saved to {args.output}[/bold green]")

        elif args.format == 'pdf':
            console.print(f"[bold green]PDF report successfully saved to {args.output}[/bold green]")

    except FileNotFoundError as e:
        console.print(f"[bold red]Error: Input file not found - {e.file_path}[/bold red]")
    except UnsupportedFileFormatError as e:
        console.print(f"[bold red]Error: {e.message}[/bold red]")
    except IOError as e:
        console.print(f"[bold red]Error: File operation failed - {e}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")
