import argparse
import pandas as pd
import numpy as np
from rich.console import Console
from rich.progress import track
from .cleaner import DataCleaner
from .exception_utils import (
    ColumnNotFoundError, DataMismatchError, UnsupportedFormatError, FileNotFoundError,
    UnsupportedFileFormatError, DataValidationError, render_error_message
)

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
        parser.add_argument('--validate_data', action='store_true', help="Validate and clean data")
        parser.add_argument('--change_case', type=str, choices=['lower', 'upper', 'title', 'capitalize'], help="Change case of string columns")
        parser.add_argument('--standardize_date', type=str, help="Standardize date format for a column")
        parser.add_argument('--regex_clean', type=str, nargs=2, metavar=('COLUMN', 'PATTERN'), help="Apply a regex pattern to clean a column")
        parser.add_argument('--handle_missing', type=str, choices=['drop', 'fill'], help="Handle missing values by dropping or filling")
        parser.add_argument('--fill_value', type=str, help="Specify fill value for missing values")
        parser.add_argument('--outlier_method', type=str, choices=['remove', 'cap'], help="Handle outliers in numeric data")
        parser.add_argument('--standardize_currency', type=str, help="Standardize currency format in a column")

        parser.set_defaults(func=CleaningCommand.clean_command)

    @staticmethod
    def clean_command(args):
        """Execute the clean command based on the provided arguments."""
        try:
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

                if args.validate_data:
                    console.print("[cyan]Validating and cleaning data...[/cyan]")
                    data_cleaner.error_handler.validate_data()

                if args.change_case:
                    console.print(f"[cyan]Changing text case to {args.change_case}...[/cyan]")
                    data_cleaner.text_operations.change_case(operation=args.change_case)

                if args.standardize_date:
                    console.print(f"[cyan]Standardizing date format for column {args.standardize_date}...[/cyan]")
                    data_cleaner.format_standardizer.standardize_date(column=args.standardize_date)

                if args.regex_clean:
                    column, pattern = args.regex_clean
                    console.print(f"[cyan]Cleaning column '{column}' with regex pattern: {pattern}...[/cyan]")
                    data_cleaner.text_operations.apply_regex_cleaning(column, pattern, '')

                if args.handle_missing == 'drop':
                    console.print("[cyan]Dropping rows with missing values...[/cyan]")
                    data_cleaner.missing_value_handler.handle_missing_values(method='drop')

                elif args.handle_missing == 'fill':
                    console.print(f"[cyan]Filling missing values with {args.fill_value if args.fill_value else 'default value'}...[/cyan]")
                    fill_value = args.fill_value if args.fill_value else 0
                    data_cleaner.missing_value_handler.handle_missing_values(method='fill', fill_value=fill_value)

                if args.outlier_method:
                    console.print(f"[cyan]Handling outliers using method: {args.outlier_method}...[/cyan]")
                    data_cleaner.outlier_handler.handle_outliers(method=args.outlier_method)

                if args.standardize_currency:
                    console.print(f"[cyan]Standardizing currency format in column {args.standardize_currency}...[/cyan]")
                    data_cleaner.format_standardizer.standardize_currency(column=args.standardize_currency)

            output_file = args.output
            console.print(f"[green]Saving cleaned data to {output_file}...[/green]")
            data_cleaner.data.to_csv(output_file, index=False)

            console.print(f"[bold green]Cleaned data successfully saved to {output_file}[/bold green]")

        except (FileNotFoundError, ColumnNotFoundError, UnsupportedFileFormatError, DataValidationError) as e:
            console.print(f"[bold red]{render_error_message(e)}[/bold red]")

        except Exception as e:
            console.print(f"[bold red]An unexpected error occurred: {str(e)}[/bold red]")
