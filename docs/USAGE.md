## Usage

Once installed, you can execute the `tidydata` command from the terminal.

### Basic Syntax

```bash
tidydata <command> [options]
```

## Commands Overview

### 1. `clean`

The `clean` command is used to clean and sanitize data files, handling duplicates, column name cleaning, and trimming spaces.

```bash
tidydata clean --input <input_file> --output <output_file> [options]
```

#### Options:
- `--remove_duplicates`: Removes duplicate rows.
- `--clean_columns`: Standardizes column names (lowercase, no spaces).
- `--trim_spaces`: Trims leading/trailing spaces.
- `--regex_clean <pattern>`: Cleans data using a regular expression.

### 2. `transform`

The `transform` command applies sorting, filtering, and transformations to the dataset.

```bash
tidydata transform --input <input_file> --output <output_file> [options]
```

#### Options:
- `--sort <column>`: Sort data based on a specific column.
- `--filter <condition>`: Filter rows based on a condition (e.g., "age > 30").
- `--add <column> <value>`: Add or modify column values.
- `--transform <lambda_function>`: Apply custom transformations.

### 3. `visualize`

The `visualize` command generates charts and visual representations of data.

```bash
tidydata visualize --input <input_file> --type <chart_type> --x <x_column> --y <y_column> --output <output_image>
```

#### Options:
- `--type <chart_type>`: Specify the chart type (e.g., `bar`, `pie`, `histogram`, `wordcloud`).
- `--x <column>`: The column to use for the x-axis (for bar/histogram).
- `--y <column>`: The column to use for the y-axis (for bar charts).

Example:
```bash
tidydata visualize --input data.csv --type bar --x category --y sales --output ./charts/bar_chart.png
```

### 4. `report`

The `report` command generates textual or PDF reports based on data from Excel/CSV files.

```bash
tidydata report --input <input_file> --output <report_file> --format <pdf|text>
```

#### Options:
- `--format`: Specify report format (`pdf` or `text`).
- `--summary`: Generate a summary report.
- `--detailed`: Generate a detailed report with statistics.

Example:
```bash
tidydata report --input data.csv --output report.pdf --format pdf --summary
```

## Cleaning Data

Cleaning your data involves sanitizing it for better analysis. You can clean the data using various options like removing duplicates, trimming spaces, and more.

```bash
tidydata clean --input data.csv --output cleaned_data.csv --remove_duplicates --clean_columns --trim_spaces
```

## Transforming Data

You can transform data by sorting, filtering, adding new columns, or applying custom transformations using lambda functions.

```bash
tidydata transform --input data.csv --output transformed_data.csv --sort column1 --filter "age > 30" --add new_column 5
```

## Visualizing Data

TidyDataCLI supports different types of charts for visualizing data. Common visualizations include bar charts, pie charts, histograms, and word clouds.

### Generate a Bar Chart

```bash
tidydata visualize --input data.csv --type bar --x category --y sales --output ./charts/bar_chart.png
```

### Create a Word Cloud

```bash
tidydata visualize --input data.csv --type wordcloud --column text_column --output ./charts/wordcloud.png
```

## Report Generation

TidyDataCLI allows generating reports in text or PDF formats to summarize or detail insights from your data.

```bash
tidydata report --input data.csv --output summary_report.pdf --format pdf --summary
```

## Running with Docker

You can run TidyDataCLI using Docker to avoid dependency management issues. Ensure Docker is installed on your system before running the commands.

```bash
docker run -v $(pwd):/data tidydatacli tidydata clean --input /data/input.csv --output /data/output.csv
```

## Error Handling

TidyDataCLI has built-in error handling for common issues like file not found, invalid column names, and missing required options.

For example, if you try to clean a file that doesn’t exist, you will receive an error message:
```bash
Error: Input file 'non_existent_file.csv' not found.
```

Ensure that:
- The input file path is correct
- The column names provided match those in the dataset
- Necessary options for the command are included
