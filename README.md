# TidyDataCLI Documentation

## 📚 Table of Contents

- [Home](#home)
- [Installation](#installation)
- [Usage](#usage)
- [Tutorials](#tutorials)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

<details>
<summary><strong>Home</strong></summary>

<p align="left">
  <a href="https://github.com/Siam3h/tidydatacli/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Siam3h/tidydatacli?style=for-the-badge&color=ffd700&logo=github">
  </a>
  <a href="https://pepy.tech/project/tidydatacli">
    <img alt="Total Downloads" src="https://img.shields.io/badge/dynamic/json?color=10b981&label=Downloads&query=total_downloads&url=https://pepy.tech/api/projects/tidydatacli&style=for-the-badge&logo=python">
  </a>
  <a href="https://github.com/Siam3h/tidydatacli/network/members">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/Siam3h/tidydatacli?style=for-the-badge&color=8b5cf6&logo=github">
  </a>
  <a href="https://pypi.org/project/tidydatacli/">
    <img alt="PyPI version" src="https://img.shields.io/pypi/v/tidydatacli?style=for-the-badge&color=34d399&logo=pypi">
  </a>
  <a href="https://github.com/Siam3h/tidydatacli/issues">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/Siam3h/tidydatacli?style=for-the-badge&color=f97316&logo=github">
  </a>
  <a href="https://github.com/Siam3h/tidydatacli/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/Siam3h/tidydatacli?style=for-the-badge&color=38bdf8&logo=open-source-initiative">
  </a>
</p>


TidyDataCLI is a powerful command-line tool designed to streamline the process of cleaning, transforming, visualizing, and reporting on Excel and CSV data. 
It is particularly useful for data analysts, researchers, and anyone working with tabular data who needs an efficient way to prepare data for analysis. 
The tool adheres to the principles of "tidy data," ensuring datasets are structured for easy analysis. <br>

TidyDataCLI is cross-platform, running seamlessly on Linux, macOS, Windows, and via Docker, making it accessible without requiring a local Python installation.

##### Features
TidyDataCLI offers a comprehensive set of features categorized into four main areas: <br> Data Cleaning, Data Transformation, Visualization, and Report Generation.

##### Cross-Platform Compatibility

Runs on Linux, macOS, Windows, and Docker, ensuring flexibility across different environments.


To follow the project and it's releases visit [github](https://github.com/siam3h/tidydatacli).

</details>

<details>
<summary><strong>Installation</strong></summary>

#### Requirements

* `Python 3.7 or higher`: Required for native installation. <br>
* `Pip`: Python package manager for installing dependencies.  <br>
* `Docker (Optional)`: For containerized execution. <br>

#### Install via pip
The simplest way to install TidyDataCLI is using pip. <br>

`pip install TidyDataCLI`

#### Install from Source
To install from the source code:<br>

Clone the repository: `git clone https://github.com/Siam3h/TidyDataCLI`


Navigate to the repository directory: `cd tidydatacli`


Install the package: `pip install`

#### Running with Docker
For users preferring a containerized environment: <br>

Pull the Docker image: `docker pull tidydatacli`


Run the tool, mounting the current directory to, <br> Example: `/data:docker run -v $(pwd):/data tidydatacli tidydata <command> --input /data/input.csv --output /data/output.csv`

</details>

<details>
<summary><strong>Usage</strong></summary>

#### Overview
TidyDataCLI supports four primary commands:<br>

clean: Performs data cleaning tasks like removing duplicates or standardizing formats. <br>

transform: Applies transformations such as sorting, filtering, or adding columns. <br>

visualize: Generates visual representations like charts or word clouds. <br>

report: Creates reports in text or PDF format.<br>

###### Command Options
For a complete list of options.

`tidydata <command> --help` 

###### 1) Data Cleaning

Remove Duplicates: Eliminates duplicate rows to ensure data integrity.<br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Regex Cleaning: Uses regular expressions to remove or replace unwanted patterns in text data. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Column Name Cleaning: Standardizes column names by removing spaces, special characters, or converting to a consistent case. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Trim Spaces: Removes leading and trailing spaces from text fields. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Age Validation: Validates age data to ensure it falls within a specified range. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Change Case: Converts text to upper, lower, or title case for consistency. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Date Standardization: Converts dates to a uniform format (e.g., YYYY-MM-DD). <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

##### 2) Data Transformation

Sorting: Sorts data by one or more columns in ascending or descending order. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Filtering: Extracts subsets of data based on user-defined conditions. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Custom Transformations: Applies custom lambda functions for advanced data manipulation. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Column Addition: Creates new columns based on calculations or existing data. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Aggregation: Performs summary operations like sum, mean, count, min, or max.
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

##### 3) Visualization
TidyDataCLI supports various visualization types to help users explore and communicate data insights: <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Bar Charts: Compare categorical data (e.g., sales by region). <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Pie Charts: Show proportions (e.g., market share). <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Word Clouds: Visualize text data by highlighting frequent terms. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Line Charts: Display trends over time (e.g., monthly revenue). <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Box-and-Whisker Plots: Show data distribution and outliers. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Gantt Charts: Visualize project timelines or schedules. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Heat Maps: Highlight patterns in numerical data (e.g., correlation matrices). <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Histograms: Display the distribution of numerical data (e.g., age distributions). <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

Tree Maps: Represent hierarchical data (e.g., organizational structures). <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

##### 4) Report Generation

Generates reports in text or PDF format, customizable with summary statistics, visualizations, or detailed data tables. <br>
`tidydata clean standardize-date input.csv --column 'Join Date' --output 'standardized_dates.csv'`

</details>

<details>
<summary><strong>Tutorials</strong></summary>

This section provides step-by-step guides for common tasks using TidyDataCLI. <br>

Assuming a sample dataset data.csv with columns name, age, date, category, and value. <br>

##### Cleaning a Dataset

###### Remove Duplicates and Clean Column Names

To remove duplicate rows and standardize column names <br>(e.g., converting "Customer Name" to "customer_name"): <br>
`tidydata clean --input data.csv --output cleaned_data.csv --remove_duplicates --clean_columns`

Trim SpacesTo remove leading/trailing spaces from text fields: <br>
`tidydata clean --input data.csv --output cleaned_data.csv --remove_duplicates --clean_columns --trim_spaces`

Standardize DatesTo convert dates to a uniform format (e.g., YYYY-MM-DD):<br>
`tidydata clean --input data.csv --output cleaned_data.csv --remove_duplicates --clean_columns --trim_spaces --standardize_dates`

Validate Age DataTo ensure age values are within a reasonable range (e.g., 0–120): <br>
`tidydata clean --input data.csv --output cleaned_data.csv --validate_age`

</details>

<details>
<summary><strong>Best Practices</strong></summary>

To maximize the effectiveness of TidyDataCLI:

###### Backup Data <br>
Always work on a copy of your original dataset to prevent data loss. <br>

###### Use Descriptive File Names<br>
Name output files clearly (e.g., cleaned_data_2025-06-21.csv) to track processing steps. <br>

###### Check for Updates <br>
Regularly visit the GitHub repository for new features or bug fixes. <br>

###### Use Docker for Consistency <br> 
For team workflows or cross-system use, leverage Docker to avoid dependency issues. <br>

###### Validate Data Early <br> 
Use cleaning and validation options (e.g., --validate_age) to catch errors before transformations. <br>

###### Optimize Visualizations <br> 
Ensure columns selected for visualizations match the chart type (e.g., numerical data for histograms).<br>

###### Document Workflows<br>
Record commands and transformations for reproducibility, especially in complex projects. <br>

###### Handle Large Datasets<br>
For large files, monitor system resources and consider splitting-objcopy <br>

</details>

<details>
<summary><strong>Troubleshooting</strong></summary>

### Common issues and solutions:

###### File Not Found <br> 
Verify the file path and ensure the file exists.<br> 
###### Invalid Input Format <br> 
Confirm the file is a valid CSV or Excel file and not corrupted.<br> 
###### Command Usage Errors<br> 
Check syntax using `tidydata <command> --help.`<br> 
###### Performance Issues<br> 
For large datasets, use Docker or ensure sufficient system memory.<br> 
###### Visualization Errors<br>  
Ensure selected columns exist and match the expected data type (e.g., numerical for histograms)<br> 

For unresolved issues, visit the [Github Issues Page](https://github.com/siam3h/tidydatacli/issues) or contact the. maintainer, [siama](mailto:siama@codegenies.org). <br> 

###### Error Handling
TidyDataCLI provides informative error messages for common issues, such as file not found, invalid formats, or incorrect command usage. <br> 

Always consult the `tidydata <command> --help.` option for correct syntax and refer to the troubleshooting section for guidance.

</details>

<details>
<summary><strong>Contributing</strong></summary>

### Contributions are welcome! 

To contribute:

Fork the repository on [Github](https://github.com/siam3h/tidydatacli). <br>

Create a branch for your changes.<br>

Submit a pull request with your improvements or bug fixes. <br>

Report issues or suggest features via the [Github Issues Page](https://github.com/siam3h/tidydatacli/issues). <br>

Refer to the [Github](https://github.com/siam3h/tidydatacli) repository’s contributing guidelines for detailed instructions.

###### License
TidyDataCLI is released under the MIT License.

###### Contact
For support or feedback, contact the maintainer at [Philbert Siama](mailto:siama@codegenies.org).

###### About
Developed by [Philbert Siama](https://siama.codegenies.org), TidyDataCLI aims to provide a user-friendly, powerful tool for data preparation. It is actively maintained and open to community contributions.

</details>

