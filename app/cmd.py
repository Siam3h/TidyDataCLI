import argparse
from cleaner.cleaner_cmd import CleaningCommand
from filehandler_cmd import import_export_command
from visualiser_cmd import VisualiserCommand
from reporter_cmd import reporting_command

def cli():
    parser = argparse.ArgumentParser(description="CLI tool for automating Excel/CSV data tasks.")
    subparsers = parser.add_subparsers(title="commands", description="Available commands")

    # Subcommand
    CleaningCommand.add_cleaning_subparser(subparsers)
    import_export_command(subparsers)
    VisualiserCommand.add_visualising_subparser(subparsers)
    reporting_command(subparsers)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    cli()
