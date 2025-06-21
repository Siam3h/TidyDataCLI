import click
from src.visualiser.visualiser_cmd import cli as visualizer_cli
from src.cleaner.cleaner_cmd import cli as cleaner_cli
from src.reporter.reporter_cmd import cli as report_cli
from src.transformer.transformer_cmd import cli as transform_cli


@click.group(
    help="""
    **Data Management CLI Tool**

    This CLI tool is designed to handle various data operations, including visualization, cleaning, and report generation.

    ### Main Command Groups:

    - **visualize**: Use this group for creating data visualizations such as bar charts, line charts, scatter plots, and word clouds.
    - **clean**: Use this group for performing data cleaning tasks, such as trimming spaces, handling missing values, and applying regex patterns.
    - **report**: Use this group for generating detailed data reports in PDF or TXT format, summarizing descriptive statistics, missing values, and correlations.

    ### Usage:

    Use the `--help` flag with any command group or subcommand to get detailed usage information and options.

    \b
    python cmd.py visualize --help   # View commands for data visualization
    python cmd.py clean --help       # View commands for data cleaning
    python cmd.py report --help      # View commands for report generation

    ### Examples:

    1. **Generate a Basic Bar Chart**:
    \b
    python cmd.py visualize basic-bar-chart input.csv --x_column 'Category' --output 'bar_chart.png'

    2. **Handle Missing Values by Filling**:
    \b
    python cmd.py clean handle-missing-values input.csv --method 'fill' --fill_value 'N/A' --output 'filled_data.csv'

    3. **Create a Summary Report in PDF**:
    \b
    python cmd.py report generate-pdf data.csv --output_pdf summary_report.pdf

    ### Detailed Help for Each Command Group:

    Each command group has its own set of commands and options. Use the following structure to explore:

    \b
    python cmd.py <command_group> <command> --help

    Replace `<command_group>` with one of `visualize`, `clean`, or `report` and `<command>` with the specific command name.

    Example:
    \b
    python cmd.py clean trim-spaces --help

    For a full list of available commands, use the `--help` flag at any level.
    """
)
def cli():
    """Main CLI for handling data visualization, cleaning, and reporting."""
    pass

""" Adding each group to the main CLI """
cli.add_command(visualizer_cli, name='visualize')
cli.add_command(cleaner_cli, name='clean')
cli.add_command(report_cli, name='report')
cli.add_command(transform_cli, name='transform')

if __name__ == '__main__':
    cli()
