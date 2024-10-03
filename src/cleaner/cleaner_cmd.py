import click
import pandas as pd
from .cleaner import Standardizer, Basic_Cleaner, TextOperations

@click.group(
    help="""
    **Data Cleaning Commands**

    This group provides commands for performing various data cleaning tasks, such as:

    - **Handling Missing Values**: Remove or fill missing values in the dataset.\n
    - **Trimming Whitespace**: Remove extra spaces from text columns.\n
    - **Applying Regex Patterns**: Search and replace text based on regular expressions.\n
    - **Changing Text Case**: Convert text columns to lower, upper, title, or capitalized case.\n
    - **Standardizing Currency**: Remove currency symbols and convert values to numeric format.\n
    - **Standardizing Date Formats**: Convert date columns to a specified format.\n

    ### Examples:

    1. **Standardize a Date Column**:
    \b
    python cmd.py clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'

    2. **Handle Missing Values by Filling**:
    \b
    python cmd.py clean handle-missing-values input.csv --method 'fill' --fill_value 'N/A' --output 'filled_data.csv'
    """
)
def cli():
    """A command-line interface for data cleaning using Standardizer, Basic_Cleaner, and TextOperations."""
    pass

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--column', help='The name of the date column to standardize.')
@click.option('--date_format', default='%Y-%m-%d', help='The desired date format (default is %Y-%m-%d).')
@click.option('--output', default=None, type=click.Path(), help='Path to save the cleaned data (optional).')
def standardize_date(input_file, column, date_format, output):
    """Standardize the format of a date column."""
    data = pd.read_csv(input_file)
    standardizer = Standardizer(data)
    cleaned_data = standardizer.standardize_date(column=column, date_format=date_format).data

    if output:
        cleaned_data.to_csv(output, index=False)
    else:
        print(cleaned_data.head())

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--column', help='The name of the currency column to standardize.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the cleaned data (optional).')
def standardize_currency(input_file, column, output):
    """Standardize currency format by removing symbols and converting to float."""
    data = pd.read_csv(input_file)
    standardizer = Standardizer(data)
    cleaned_data = standardizer.standardize_currency(column=column).data

    if output:
        cleaned_data.to_csv(output, index=False)
    else:
        print(cleaned_data.head())

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output', default=None, type=click.Path(), help='Path to save the cleaned data (optional).')
def trim_spaces(input_file, output):
    """Trim extra spaces in all string columns."""
    data = pd.read_csv(input_file)
    cleaner = Basic_Cleaner(data)
    cleaned_data = cleaner.trim_spaces().data

    if output:
        cleaned_data.to_csv(output, index=False)
    else:
        print(cleaned_data.head())

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--method', default='drop', type=click.Choice(['drop', 'fill']), help='Method to handle missing values (drop or fill).')
@click.option('--fill_value', default=None, help='Value to fill missing values with if "fill" method is chosen.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the cleaned data (optional).')
def handle_missing_values(input_file, method, fill_value, output):
    """Handle missing values in the data."""
    data = pd.read_csv(input_file)
    cleaner = Basic_Cleaner(data)
    cleaned_data = cleaner.handle_missing_values(method=method, fill_value=fill_value).data

    if output:
        cleaned_data.to_csv(output, index=False)
    else:
        print(cleaned_data.head())

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--column', help='The column to apply regex cleaning.')
@click.option('--pattern', help='The regex pattern to search for.')
@click.option('--replacement', help='The string to replace the pattern with.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the cleaned data (optional).')
def apply_regex_cleaning(input_file, column, pattern, replacement, output):
    """Apply regex cleaning to a specified column."""
    data = pd.read_csv(input_file)
    cleaner = Basic_Cleaner(data)
    cleaned_data = cleaner.apply_regex_cleaning(column=column, pattern=pattern, replacement=replacement).data

    if output:
        cleaned_data.to_csv(output, index=False)
    else:
        print(cleaned_data.head())

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--columns', default=None, help='Comma-separated list of columns to apply the transformation. If None, all text columns are used.')
@click.option('--operation', default='lower', type=click.Choice(['lower', 'upper', 'title', 'capitalize']), help='Case transformation operation.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the transformed data (optional).')
def change_case(input_file, columns, operation, output):
    """Change the case of text in specified columns."""
    data = pd.read_csv(input_file)
    columns_list = columns.split(',') if columns else None
    text_ops = TextOperations(data)
    cleaned_data = text_ops.change_case(operation=operation, columns=columns_list).data

    if output:
        cleaned_data.to_csv(output, index=False)
    else:
        print(cleaned_data.head())

"""
Adding commands to the main CLI group
"""
cli.add_command(standardize_date)
cli.add_command(standardize_currency)
cli.add_command(trim_spaces)
cli.add_command(handle_missing_values)
cli.add_command(apply_regex_cleaning)
cli.add_command(change_case)

if __name__ == '__main__':
    cli()
