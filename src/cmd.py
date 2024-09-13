import argparse
from rich.console import Console
from rich.text import Text
from rich.table import Table
from .cleaner.cleaner_cmd import CleaningCommand
from .file_handler.fileHandler_cmd import import_export_command
from .transformer.transformer_cmd import transformation_command
from .reporter.reporter_cmd import reporting_command
from .visualiser.visualiser_cmd import VisualiserCommand

console = Console()

def print_help():
    """
    Prints help information in a rich format.
    """
	
    table = Table(title="Available Commands", caption="Use these commands to perform operations")

    table.add_column("Command", style="bold cyan", justify="left")
    table.add_column("Description", style="bold white", justify="left")

    commands = [
        ("clean", "Clean data: Remove duplicates, handle missing values, and more."),
        ("visualize", "Visualize data: Generate various types of charts."),
        ("import", "Import data: Load data from source files."),
        ("export", "Export data: Save data to destination files."),
        ("report", "Generate a report: Create text or PDF reports from data."),
        ("transform", "Transform data: Apply sorting, filtering, and other transformations."),
    ]

    for command, description in commands:
        table.add_row(f"[bold blue]{command}[/bold blue]", description)

    console.print(table)

    console.print("\nA CLI tool to automate cleaning, transformation, and visualization of Excel/CSV data.\n")

def main():
    parser = argparse.ArgumentParser(description="A CLI tool to automate cleaning, transformation, and visualization of Excel/CSV data.")
    subparsers = parser.add_subparsers(title="commands", description="Available commands")

    CleaningCommand.add_cleaning_subparser(subparsers)
    VisualiserCommand.add_visualising_subparser(subparsers)
    import_export_command(subparsers)
    reporting_command(subparsers)
    transformation_command(subparsers)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        print_help()

if __name__ == '__main__':
    main()
