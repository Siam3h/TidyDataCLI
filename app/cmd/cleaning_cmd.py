import argparse
import pandas as pd
from app.cleaning.cleaner import DataCleaner


class CleaningCommand:
    @classmethod
    def add_cleaning_subparser(cls, subparsers):
        """Add the 'clean' command to the subparsers."""
        parser = subparsers.add_parser('clean', help="Clean data")
        parser.add_argument('input', type=str, help="Input file path")
        parser.add_argument('output', type=str, help="Output file path")
        parser.set_defaults(func=cls.execute_clean_command)
    
    @classmethod
    def execute_clean_command(cls, args):
        """Execute the 'clean' command."""
        data_frame = pd.read_csv(args.input)
        data_cleaner = DataCleaner(data_frame)
        cleaned_data = data_cleaner.clean_all().data
        cleaned_data.to_csv(args.output, index=False)
        print(f"Cleaned data saved to {args.output}")

