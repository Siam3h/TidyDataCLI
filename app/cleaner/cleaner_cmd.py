import argparse
import pandas as pd
from rich.console import Console
from rich.progress import track
from .cleaner import DataCleaner

console = Console()

class CleaningCommand:

    @staticmethod
    def add_cleaning_subparser(subparsers):
        """Add subparser for the clean command with multiple options."""
        parser = subparsers.add_parser('clean', help="Clean data with various operations")
        parser.add_argument('input', type=str, help="Path to input CSV file")
        parser.add_argument('output', type=str, help="Path to output cleaned CSV file")
        parser.add_argument('--remove_duplicates', action='store_true', help="Remove duplicate rows")
        parser.add_argument('--clean_columns', action='store_true', help="Clean column names (strip spaces, lowercase)")
        parser.add_argument('--trim_spaces', action='store_true', help="Trim spaces in string columns")
        parser.add_argument('--validate_age', action='store_true', help="Validate and clean 'age' column")
        parser.add_argument('--change_case', type=str, choices=['lower', 'upper', 'title', 'capitalize'], help="Change case of string columns")
        parser.add_argument('--standardize_date', type=str, help="Standardize date format for a column")
        parser.add_argument('--regex_clean', type=str, help="Apply a regex pattern to clean data")

        parser.set_defaults(func=CleaningCommand.clean_command)

    @staticmethod
    def clean_command(args):
        """Execute the clean command based on the provided arguments."""
        console.print(f"[green]Reading data from {args.input}...[/green]")
        data_frame = pd.read_csv(args.input)
        data_cleaner = DataCleaner(data_frame)

        with console.status("[bold green]Cleaning data...[/bold green]") as status:
            if args.clean_columns:
                console.print("[cyan]Cleaning column names...[/cyan]")
                data_cleaner.basic_cleaner.clean_column_names()

            if args.trim_spaces:
                console.print("[cyan]Trimming spaces in string columns...[/cyan]")
                data_cleaner.basic_cleaner.basic_cleaning()

            if args.remove_duplicates:
                console.print("[cyan]Removing duplicate rows...[/cyan]")
                data_cleaner.error_handler.clean_duplicates()

            if args.validate_age:
                console.print("[cyan]Validating and cleaning 'age' column...[/cyan]")
                data_cleaner.error_handler.validate_data()

            if args.change_case:
                console.print(f"[cyan]Changing text case to {args.change_case}...[/cyan]")
                data_cleaner.text_operations.change_case(operation=args.change_case)

            if args.standardize_date:
                console.print(f"[cyan]Standardizing date format for column {args.standardize_date}...[/cyan]")
                data_cleaner.format_standardizer.standardize_date(column=args.standardize_date)

            if args.regex_clean:
                console.print(f"[cyan]Cleaning with regex pattern: {args.regex_clean}...[/cyan]")
                data_cleaner.data = data_cleaner.data.apply(
                    lambda col: col.str.replace(args.regex_clean, '', regex=True) if col.dtype == 'object' else col
                )

            output_file = args.output
            console.print(f"[green]Saving cleaned data to {output_file}...[/green]")
            data_cleaner.data.to_csv(output_file, index=False)

            console.print(f"[bold green]Cleaned data successfully saved to {output_file}[/bold green]")
