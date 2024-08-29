import argparse
from app.cmd.cleaning_cmd import CleaningCommand

def cli():
    parser = argparse.ArgumentParser(description="CLI tool for automating Excel/CSV data tasks.")
    
    subparsers = parser.add_subparsers(title="commands", description="Available commands")

    # Add the cleaning command
    CleaningCommand.add_cleaning_subparser(subparsers)
    
    # Add other commands as needed
    # transformation_command(subparsers)
    # visualization_command(subparsers)
    # import_export_command(subparsers)
    # reporting_command(subparsers)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    cli()
