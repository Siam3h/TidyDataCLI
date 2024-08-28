import argparse
from .cleaning_cmd import cleaning_command
from .transformation_cmd import transformation_command
from .analysis_cmd import analysis_command
from .visualization_cmd import visualization_command
from .import_export_cmd import import_export_command
from .reporting_cmd import reporting_command

def cli():
    parser = argparse.ArgumentParser(description="CLI tool for automating Excel/CSV data tasks.")
    
    subparsers = parser.add_subparsers(title="commands", description="Available commands")

    cleaning_command(subparsers)
    transformation_command(subparsers)
    analysis_command(subparsers)
    visualization_command(subparsers)
    import_export_command(subparsers)
    reporting_command(subparsers)

    args = parser.parse_args()
    args.func(args)
