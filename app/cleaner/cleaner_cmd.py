import argparse
import pandas as pd
from .cleaner import DataCleaner

class CleaningCommand:

    @staticmethod
    def add_cleaning_subparser(subparsers):
        parser = subparsers.add_parser('--clean', help="Clean data")
        parser.add_argument('input', type=str, help="Input file path")
        parser.add_argument('output', type=str, help="Output file path")
        parser.add_argument('--remove_duplicates', action='store_true', help="Remove duplicate rows")
        parser.add_argument('--regex_clean', type=str, help="Clean data with regex")
        parser.set_defaults(func=CleaningCommand.clean_command)

    @staticmethod
    def clean_command(args):
        data_frame = pd.read_csv(args.input)
        data_cleaner = DataCleaner(data_frame)

        if args.remove_duplicates:
            data_cleaner.clean_all().data = data_cleaner.clean_all().data.error_handler.clean_duplicates()

        if args.regex_clean:
            data_cleaner.data = data_cleaner.data.apply(
            lambda col: col.str.replace(args.regex_clean, '', regex=True)
            if col.dtype == 'object' else col)

        cleaned_data = data_cleaner.clean_all().data
        cleaned_data.to_csv(args.output, index=False)
        print(f"Cleaned data saved to {args.output}")
