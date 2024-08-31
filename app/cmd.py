import argparse
from cleaner.cleaner_cmd import CleaningCommand

def cli():
	parser = argparse.ArgumentParser(description="CLI tool for automating Excel/CSV data tasks.")

	subparsers = parser.add_subparsers(title="commands", description="Available commands")

	CleaningCommand.add_cleaning_subparser(subparsers)

	args = parser.parse_args
	if hasattr(args, 'func'):
	    args.func(args)
	else:
	    parser.print_help()

if __name__ == '__main__':

	cli()
