import argparse
from .fileHandler import import_data, export_data, get_handler
from .exceptions import FileNotFoundError, UnsupportedFileFormatError, DataProcessingError
from rich.console import Console
from rich.progress import track
from rich.traceback import install

console = Console()
install()

def import_export_command(subparsers):
    """
    Adds subcommands for importing and exporting data to the argument parser.

    Args:
        subparsers (argparse._SubParsersAction): The subparsers object from argparse.
    """
    import_parser = subparsers.add_parser('import', help="Import data from a source file to a destination")
    import_parser.add_argument('source', type=str, help="Source file path")
    import_parser.add_argument('destination', type=str, help="Destination file path")
    import_parser.add_argument('--format', type=str, choices=['csv', 'excel', 'json'], required=True, help="File format")
    import_parser.set_defaults(func=import_command)

    export_parser = subparsers.add_parser('export', help="Export data to a destination file")
    export_parser.add_argument('data_source', type=str, help="Data source file path")
    export_parser.add_argument('destination', type=str, help="Destination file path")
    export_parser.add_argument('--format', type=str, choices=['csv', 'excel', 'json'], required=True, help="File format")
    export_parser.set_defaults(func=export_command)

def import_command(args):
    """
    Handles the import functionality.

    Args:
        args (argparse.Namespace): Command-line arguments for the import operation.
    """
    try:
        for _ in track(range(1), description="Importing data..."):
            import_data(args.source, args.destination, file_format=args.format)
        console.print(f"[bold green]Data successfully imported from {args.source} to {args.destination}[/bold green]")
    except FileNotFoundError as e:
        console.print(f"[bold red]Error: Source file not found - {e.file_path}[/bold red]")
    except UnsupportedFileFormatError as e:
        console.print(f"[bold red]Error: {e.message}[/bold red]")
    except DataProcessingError as e:
        console.print(f"[bold red]Error during data processing: {e}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")

def export_command(args):
    """
    Handles the export functionality.

    Args:
        args (argparse.Namespace): Command-line arguments for the export operation.
    """
    try:
        for _ in track(range(1), description="Exporting data..."):
            import_handler = get_handler(args.format, args.data_source)
            data = import_handler.load_data()
            export_data(data, args.destination, file_format=args.format)
        console.print(f"[bold green]Data successfully exported from {args.data_source} to {args.destination}[/bold green]")
    except FileNotFoundError as e:
        console.print(f"[bold red]Error: Data source file not found - {e.file_path}[/bold red]")
    except UnsupportedFileFormatError as e:
        console.print(f"[bold red]Error: {e.message}[/bold red]")
    except DataProcessingError as e:
        console.print(f"[bold red]Error during data export: {e}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")
