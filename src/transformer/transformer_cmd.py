import click
import pandas as pd
from .transformer import DataTransformer

@click.group(
    help="""
    **Data Transformation and Views Commands**

    This group provides commands for performing various data transformations and viewing, such as:

    - **Adding New Column to data**: Add a new column to the DataFrame with a specified value.\n
    - **Dropping an entire Column**: Drop a column from the DataFrame.\n
    - **Renaming a Column**: Rename a column in the DataFrame.\n
    - **Viewing of the first top rows**: View the first `n` rows of the DataFrame.\n
    - **Viewing of the last bottom rows**: View the last `n` rows of the DataFrame.\n

    ### Examples:

    1. **Add A New Column to data**:
    \b
    python cmd.py transform add-column input.csv --column_name 'Added_Column_Data.csv'

    2. **Rename a Column**:
    \b
    python cmd.py transform rename-column input.csv --old_name 'Old Name' --new_name 'New Name' --output 'renamed_column_data.csv'
    
    1. **View the last `n` rows of the DataFrame**:
    \b
    python cmd.py transform view-tail input.csv --n 10 --output 'viewed_tail_data.csv'

    """
)
def cli():
    """A command-line interface for data cleaning using Standardizer, Basic_Cleaner, and TextOperations."""
    pass

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--column_name', help='The name of the new column.')
@click.option('--value', help='The value to be assigned to the new column. Can be a single value or a list/Series with length equal to the DataFrame.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the cleaned data (optional).')
def add_column(input_file, column_name , value, output):
    """Add a new column to the DataFrame with a specified value."""
    data = pd.read_csv(input_file)
    column_add = DataTransformer(data)
    transformed_data = column_add.add_column(column_name=column_name, value=value).data

    if output:
        transformed_data.to_csv(output, index=False)
    else:
        print(transformed_data.head())

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--column_name', help='The name of the column to drop.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the cleaned data (optional).')
def drop_column(input_file, column_name, output):
    """Drop a column from the DataFrame."""
    data = pd.read_csv(input_file)
    column_drop = DataTransformer(data)
    transformed_data = column_drop.drop_column(column_name=column_name).data

    if output:
        transformed_data.to_csv(output, index=False)
    else:
        print(transformed_data.head())

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--old_name', help='The name of the column to drop.')
@click.option('--new_name', help='The name of the column to drop.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the cleaned data (optional).')
def rename_column(input_file,old_name, new_name, output):
    """Rename a column in the DataFrame."""
    data = pd.read_csv(input_file)
    column_renamed = DataTransformer(data)
    transformed_data = column_renamed.rename_column(old_name=old_name, new_name=new_name).data

    if output:
        transformed_data.to_csv(output, index=False)
    else:
        print(transformed_data.head())

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--n', default=5, help=' The number of rows to display. Defaults to 5.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the cleaned data (optional).')
def view_head(input_file,n, output):
    """View the first `n` rows of the DataFrame."""
    data = pd.read_csv(input_file)
    data_viewed = DataTransformer(data)
    transformed_data = data_viewed.view_head(n=n).data

    if output:
       transformed_data.to_csv(output, index=False)
    else:
        print(transformed_data.head())

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--n', default=5, help=' The number of rows to display. Defaults to 5.')
@click.option('--output', default=None, type=click.Path(), help='Path to save the cleaned data (optional).')
def view_tail(input_file,n, output):
    """View the last `n` rows of the DataFrame."""
    data = pd.read_csv(input_file)
    data_viewed = DataTransformer(data)
    transformed_data = data_viewed.view_tail(n=n).data

    if output:
        transformed_data.to_csv(output, index=False)
    else:
        print(transformed_data.head())


"""
Add commands to the main CLI group
"""
cli.add_command(add_column)
cli.add_command(drop_column)
cli.add_command(rename_column)
cli.add_command(view_head)
cli.add_command(view_tail)

if __name__ == '__main__':
    cli()
