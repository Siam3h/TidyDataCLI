import argparse
from ..visualization import visualize_data

def visualization_command(subparsers):
    parser = subparsers.add_parser('visualize', help="Visualize data")
    parser.add_argument('input', type=str, help="Input file path")
    parser.add_argument('output', type=str, help="Output file path")
    parser.add_argument('--type', type=str, choices=['bar', 'line'], help="Type of visualization")

    parser.set_defaults(func=visualize_command)

def visualize_command(args):
    data_frame = pd.read_csv(args.input)
    visualize_data(data_frame, visualization_type=args.type, output_path=args.output)
    print(f"Visualization saved to {args.output}")
