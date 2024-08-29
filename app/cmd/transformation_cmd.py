import argparse
from ..transformations import DataTransformer

transform_data = DataTransformer()

def transformation_command(subparsers):
    parser = subparsers.add_parser('transform', help="Transform data")
    parser.add_argument('input', type=str, help="Input file path")
    parser.add_argument('output', type=str, help="Output file path")
    parser.add_argument('--sort', type=str, help="Column to sort by")

    parser.set_defaults(func=transform_command)

def transform_command(args):
    data_frame = pd.read_csv(args.input)
    transformed_data = transform_data(data_frame, sort_column=args.sort)
    transformed_data.to_csv(args.output, index=False)
    print(f"Transformed data saved to {args.output}")
