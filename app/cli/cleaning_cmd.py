import argparse
from ..cleaning import clean_data

def cleaning_command(subparsers):
    parser = subparsers.add_parser('clean', help="Clean data")
    parser.add_argument('input', type=str, help="Input file path")
    parser.add_argument('output', type=str, help="Output file path")
    
    parser.set_defaults(func=clean_command)

def clean_command(args):
    data_frame = pd.read_csv(args.input)
    cleaned_data = clean_data(data_frame)
    cleaned_data.to_csv(args.output, index=False)
    print(f"Cleaned data saved to {args.output}")
