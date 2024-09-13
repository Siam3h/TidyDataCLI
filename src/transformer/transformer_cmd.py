import argparse
import pandas as pd
from rich.console import Console
from rich.progress import track
from .transformer import DataTransformer
from .exception_utils import ColumnNotFoundError, DataValidationError, render_error_message

console = Console()

def transformation_command(subparsers):
    """
    Define the command-line arguments and functionality for the 'transform' command.

    Args:
        subparsers (argparse._SubParsersAction): The subparsers object from argparse.

    Returns:
        None
    """
    parser = subparsers.add_parser('transform', help="Transform data")
    parser.add_argument('input', type=str, help="Input file path")
    parser.add_argument('output', type=str, nargs='?', default=None, help="Output file path (optional)")
    parser.add_argument('--sort', type=str, nargs='+', help="Column(s) to sort by")
    parser.add_argument('--ascending', action='store_true', help="Sort in ascending order")
    parser.add_argument('--filter', type=str, help="Condition to filter data by")
    parser.add_argument('--transform', type=str, help="Custom transformation (lambda function) to apply to the data")
    parser.add_argument('--add', nargs=2, metavar=('COLUMN', 'VALUE'), help="Add a value to a column")
    parser.add_argument('--aggregate', type=str, choices=['sum', 'mean', 'count'], help="Aggregate data by a specified column")
    parser.add_argument('--head', type=int, help="View the first n rows of the data")
    parser.add_argument('--tail', type=int, help="View the last n rows of the data")

    parser.set_defaults(func=transform_command)

def transform_command(args):
    """
    Execute data transformations based on command-line arguments.

    Args:
        args (argparse.Namespace): The command-line arguments parsed by argparse.

    Returns:
        None
    """
    try:
        console.print(f"[green]Reading data from {args.input}...[/green]")
        data_frame = pd.read_csv(args.input)
    except FileNotFoundError:
        console.print(render_error_message(FileNotFoundError(args.input)))
        return
    except pd.errors.EmptyDataError:
        console.print(render_error_message(DataValidationError("Input file is empty or cannot be read.")))
        return

    transformer = DataTransformer()

    try:
        for _ in track(range(1), description="Transforming data..."):

            if args.sort:
                console.print(f"[cyan]Sorting data by {args.sort} in {'ascending' if args.ascending else 'descending'} order...[/cyan]")
                data_frame = transformer.sort_data(data_frame, by=args.sort, ascending=args.ascending)

            if args.filter:
                console.print(f"[cyan]Filtering data with condition: {args.filter}...[/cyan]")
                data_frame = transformer.filter_data(data_frame, condition=args.filter)

            if args.transform:
                console.print(f"[cyan]Applying custom transformation...[/cyan]")
                func = eval(args.transform)
                data_frame = transformer.apply_custom_transformation(data_frame, func)

            if args.add:
                column, value = args.add
                console.print(f"[cyan]Adding value {value} to column {column}...[/cyan]")
                if column not in data_frame.columns:
                    raise ColumnNotFoundError(column)
                data_frame[column] += float(value)

            if args.aggregate:
                console.print(f"[cyan]Aggregating data by {args.sort} using {args.aggregate} function...[/cyan]")
                aggregation_func = {'sum': 'sum', 'mean': 'mean', 'count': 'count'}
                data_frame = data_frame.groupby(args.sort).agg(aggregation_func[args.aggregate])

            if args.head:
                console.print(f"[cyan]Displaying first {args.head} rows...[/cyan]")
                console.print(data_frame.head(args.head))
                return

            if args.tail:
                console.print(f"[cyan]Displaying last {args.tail} rows...[/cyan]")
                console.print(data_frame.tail(args.tail))
                return

        if args.output:
            console.print(f"[green]Saving transformed data to {args.output}...[/green]")
            data_frame.to_csv(args.output, index=False)
            console.print(f"[bold green]Transformed data successfully saved to {args.output}[/bold green]")
        else:
            console.print(data_frame)

    except (ColumnNotFoundError, DataValidationError) as e:
        console.print(render_error_message(e))

    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {str(e)}[/bold red]")
