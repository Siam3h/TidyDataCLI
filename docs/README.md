# TidyDataCLI

## Overview

TidyDataCLI is a versatile command-line tool designed to automate the process of cleaning, transforming, and visualizing Excel/CSV data. The tool is cross-platform and can be run on any operating system, including via Docker, without requiring a Python installation.

## Features

### Data Cleaning
	- Remove Duplicates: Efficiently remove duplicate entries from your dataset.
	- Regex Cleaning: Sanitize data using customizable regular expressions.
	- Column Name Cleaning: Standardize column names by stripping spaces and converting to lowercase.
	- Trim Spaces: Remove leading and trailing spaces from string columns.
	- Age Validation: Validate and clean 'age' columns to ensure data integrity.
	- Change Case: Convert text columns to lowercase, uppercase, title case, or capitalize.
	- Date Standardization: Standardize date formats across specified columns.

### Data Transformation
	- Sorting: Sort data by one or more columns with ascending or descending options.
	- Filtering: Apply conditions to filter rows based on specified criteria.
	- Custom Transformations: Apply user-defined lambda functions for complex transformations.
	- Column Addition: Add values to existing columns and perform arithmetic operations.
	- Aggregation: Aggregate data by summing, averaging, or counting grouped values.

### Visualization
	- Bar Charts: Generate bar charts with customizable x and y axes.
	- Pie Charts: Create pie charts with labels and values for visualization.
	- Word Clouds: Visualize text data using word clouds.
	- Line Charts: Plot line charts for trend analysis.
	- Box-and-Whisker Plots: Create box plots to analyze data distributions.
	- Gantt Charts: Visualize project timelines with Gantt charts.
	- Heat Maps: Generate heat maps to represent data density.
	- Histograms: Plot histograms with adjustable bin sizes.
	- Tree Maps: Visualize hierarchical data using tree maps.

### Report Generation
	- Generate textual or PDF reports from Excel/CSV data

### Cross-Platform
  - Runs on Linux, macOS, and Windows

### Docker Support
  - Avoid dependency issues by running the CLI in a Docker container

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands Overview](#commands-overview)
- [Cleaning Data](#cleaning-data)
- [Transforming Data](#transforming-data)
- [Visualizing Data](#visualizing-data)
- [Report Generation](#report-generation)
- [Running with Docker](#running-with-docker)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Requirements

- Python 3.7 or higher
- Pip (Python package installer)
- Docker (optional)

### Install via `pip`

Install the latest version of TidyDataCLI using pip:

```bash
pip install TidyDataCLI
```

### Install from Source

To install TidyDataCLI from the source:

1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/Siam3h/tidydatacli.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tidydatacli
   ```
3. Install the package locally:
   ```bash
   pip install .
   ```

### Running via Docker

If you prefer not to install Python dependencies, you can run TidyDataCLI inside a Docker container.

1. Pull the Docker image:
   ```bash
   docker pull tidydatacli
   ```
2. Run the CLI commands from the container:
   ```bash
   docker run -v $(pwd):/data tidydatacli tidydata <command> --input /data/input.csv --output /data/output.csv
   ```

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

## Contributing

We welcome contributions to TidyDataCLI! If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and write tests, if applicable.
4. Submit a pull request for review.

For any issues or suggestions, feel free to open an [issue](https://github.com/Siam3h/tidydatacli/issues) on the GitHub repository.

## License

TidyDataCLI is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.
```
