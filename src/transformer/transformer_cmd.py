import argparse
import pandas as pd
from .transformer import DataTransformer

def transformation_command(subparsers):
    parser = subparsers.add_parser('transform', help="Transform data")
    parser.add_argument('input', type=str, help="Input file path")
    parser.add_argument('output', type=str, help="Output file path")
    parser.add_argument('--sort', type=str, nargs='+', help="Column(s) to sort by")
    parser.add_argument('--ascending', action='store_true', help="Sort in ascending order")
    parser.add_argument('--filter', type=str, help="Condition to filter data by")
    parser.add_argument('--transform', type=str, help="Custom transformation (lambda function) to apply to the data")
    parser.add_argument('--add', nargs=2, metavar=('COLUMN', 'VALUE'), help="Add a value to a column")
    parser.add_argument('--aggregate', type=str, choices=['sum', 'mean', 'count'], help="Aggregate data by a specified column")

    parser.set_defaults(func=transform_command)

def transform_command(args):
    data_frame = pd.read_csv(args.input)
    transformer = DataTransformer()

    if args.sort:
        data_frame = transformer.sort_data(data_frame, by=args.sort, ascending=args.ascending)

    if args.filter:
        data_frame = transformer.filter_data(data_frame, condition=args.filter)

    if args.transform:
        try:
            func = eval(args.transform)
            data_frame = transformer.apply_custom_transformation(data_frame, func)
        except Exception as e:
            raise ValueError(f"Invalid transformation function: {e}")

    if args.add:
        column, value = args.add
        if column not in data_frame.columns:
            raise ValueError(f"Column {column} does not exist.")
        data_frame[column] += float(value)

    if args.aggregate:
        aggregation_func = {'sum': 'sum', 'mean': 'mean', 'count': 'count'}
        data_frame = data_frame.groupby(args.sort).agg(aggregation_func[args.aggregate])

    data_frame.to_csv(args.output, index=False)
    print(f"Transformed data saved to {args.output}")
