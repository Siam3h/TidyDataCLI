import argparse
from cleaner.cleaner_cmd import CleaningCommand
from file_handler.fileHandler_cmd import import_export_command
from transformer.transformer_cmd import transformation_command
from reporter.reporter_cmd import reporting_command
from visualiser.visualiser_cmd import VisualiserCommand

def cli():
    parser = argparse.ArgumentParser(description="A CLI tool to automate cleaning, transformation and visualisation of Excel/CSV data.")
    subparsers = parser.add_subparsers(title="commands", description="Available commands")

    CleaningCommand.add_cleaning_subparser(subparsers)
    VisualiserCommand.add_visualising_subparser(subparsers)
    import_export_command(subparsers)
    reporting_command(subparsers)
    transformation_command(subparsers)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    cli()
