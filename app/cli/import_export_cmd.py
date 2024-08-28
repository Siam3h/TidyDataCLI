import argparse
from ..import_export import import_data, export_data

def import_export_command(subparsers):
    parser = subparsers.add_parser('import', help="Import data")
    parser.add_argument('source', type=str, help="Source file path")
    parser.add_argument('destination', type=str, help="Destination file path")

    parser.add_argument('--format', type=str, choices=['csv', 'excel'], help="File format")

    parser.set_defaults(func=import_command)

def import_command(args):
    import_data(args.source, args.destination, file_format=args.format)
    print(f"Data imported from {args.source} to {args.destination}")
