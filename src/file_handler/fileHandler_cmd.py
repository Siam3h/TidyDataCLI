import argparse
from .fileHandler import import_data, export_data, get_handler

def import_export_command(subparsers):
    import_parser = subparsers.add_parser('import', help="Import data")
    import_parser.add_argument('source', type=str, help="Source file path")
    import_parser.add_argument('destination', type=str, help="Destination file path")
    import_parser.add_argument('--format', type=str, choices=['csv', 'excel', 'json'], required=True, help="File format")
    import_parser.set_defaults(func=import_command)

    export_parser = subparsers.add_parser('export', help="Export data")
    export_parser.add_argument('data_source', type=str, help="Data source file path")
    export_parser.add_argument('destination', type=str, help="Destination file path")
    export_parser.add_argument('--format', type=str, choices=['csv', 'excel', 'json'], required=True, help="File format")
    export_parser.set_defaults(func=export_command)

def import_command(args):
    try:
        import_data(args.source, args.destination, file_format=args.format)
        print(f"Data imported from {args.source} to {args.destination}")
    except Exception as e:
        print(f"An error occurred: {e}")

def export_command(args):
    try:
        import_handler = get_handler(args.format, args.data_source)
        data = import_handler.load_data()
        export_data(data, args.destination, file_format=args.format)
        print(f"Data exported from {args.data_source} to {args.destination}")
    except Exception as e:
        print(f"An error occurred: {e}")
