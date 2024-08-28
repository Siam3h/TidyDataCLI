import argparse
from ..app.cli.cleaning_cmd import cleaning_command
from ..app.cli.transformation_cmd import transformation_command
from ..app.cli.visualization_cmd import visualization_command
from ..app.cli.import_export_cmd import import_export_command
from ..app.cli.reporting_cmd import reporting_command

def cli():
    parser = argparse.ArgumentParser(description="CLI tool for automating Excel/CSV data tasks.")
    
    subparsers = parser.add_subparsers(title="commands", description="Available commands")

    cleaning_command(subparsers)
    transformation_command(subparsers)
    visualization_command(subparsers)
    import_export_command(subparsers)
    reporting_command(subparsers)

    args = parser.parse_args()
    args.func(args)
