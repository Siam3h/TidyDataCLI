# TidyDataCLI

TidyDataCLI is a powerful command-line tool designed to streamline the process of cleaning and processing Excel/CSV data. It offers features such as removing duplicates, sanitizing data using regular expressions, and generating visual frequency plots. TidyDataCLI is cross-platform and can be easily run on any operating system, including via Docker, without needing to install Python.

## Features

- **Remove Duplicates:** Easily remove duplicate entries from your dataset.
- **Regex Cleaning:** Sanitize your data by applying regular expressions to clean up unwanted patterns.
- **Frequency Plots:** Generate visual frequency plots for any column in your dataset.
- **Cross-Platform Compatibility:** Run on any platform, including via Docker.
- **Support for Excel and CSV files:** Seamlessly handle both `.csv` and `.xlsx` files.

## Installation

To install TidyDataCLI, simply run:

```bash
pip install TidyDataCLI
```

## Usage

### 1. Remove Duplicates

To remove duplicate rows from a dataset:

```bash
tidydata remove_duplicates --input-file input.csv --output-file output.csv
```

You can also specify a subset of columns to check for duplicates:

```bash
tidydata remove_duplicates --input-file input.csv --output-file output.csv --subset column1,column2
```

### 2. Regex Cleaning

To clean your data using a regular expression:

```bash
tidydata regex_clean --input-file input.csv --output-file output.csv --pattern "\d+"
```

This will remove all numeric characters from your data.

### 3. Generate Frequency Plots

To generate a frequency plot for a specific column:

```bash
tidydata plot_frequency --input-file input.csv --column-name column_name --output-dir ./plots
```

The frequency plot will be saved as a `.png` file in the specified output directory.

## Example

Given a CSV file `data.csv`:

```csv
Name, Age, Country
Alice, 29, USA
Bob, 32, Canada
Alice, 29, USA
```

### Removing Duplicates

Command:

```bash
tidydata remove_duplicates --input-file data.csv --output-file cleaned_data.csv
```

Output (`cleaned_data.csv`):

```csv
Name, Age, Country
Alice, 29, USA
Bob, 32, Canada
```

### Regex Cleaning

Command:

```bash
tidydata regex_clean --input-file data.csv --output-file cleaned_data.csv --pattern "\d"
```

Output (`cleaned_data.csv`):

```csv
Name, Age, Country
Alice, , USA
Bob, , Canada
Alice, , USA
```

### Generating Frequency Plot

Command:

```bash
tidydata plot_frequency --input-file data.csv --column-name Country --output-dir ./plots
```

This generates a bar plot showing the frequency of each country in the dataset, saved in the `./plots` directory.

## Docker Support

If you prefer not to install Python or other dependencies, you can use TidyDataCLI with Docker:

```bash
docker run -v $(pwd):/data tidydatacli tidydata <command> --input-file /data/input.csv --output-file /data/output.csv
```

## Contributing

## Contributing

Contributions are welcome! Please feel free to [submit a pull request](https://github.com/siam3h/tidydatacli/pulls) or [open an issue](https://github.com/siam3h/tidydatacli/issues).

## License

TidyDataCLI is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or issues, please contact Siama at [siamaphilbert@outlook.com].
