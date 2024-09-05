![TidyDataCLI Logo](https://github.com/Siam3h/TidyDataCLI/blob/main/TidyDataCLI.jpg)

# TidyDataCLI

## **Overview**

[![GitHub stars](https://img.shields.io/github/stars/Siam3h/tidydatacli?style=social)](https://github.com/Siam3h/tidydatacli/stargazers)
[![PyPI version](https://img.shields.io/pypi/v/tidydatacli)](https://pypi.org/project/tidydatacli/)
[![GitHub forks](https://img.shields.io/github/forks/Siam3h/tidydatacli?style=social)](https://github.com/Siam3h/tidydatacli/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Siam3h/tidydatacli)](https://github.com/Siam3h/tidydatacli/issues)
[![GitHub license](https://img.shields.io/github/license/Siam3h/tidydatacli)](https://github.com/Siam3h/tidydatacli/blob/main/LICENSE)

TidyDataCLI is a robust command-line tool built for automating the process of cleaning, transforming, and visualizing Excel/CSV data. Designed to be cross-platform, it can run seamlessly on Linux, macOS, and Windows, and can even be used through Docker without requiring Python to be installed.

**Why use TidyDataCLI?**  
With its wide range of features, TidyDataCLI simplifies complex data tasks, offering tools for:

- **Data Cleaning**: Remove duplicates, standardize column names, trim spaces, validate ages, and much more.
- **Data Transformation**: Sort, filter, apply custom transformations, and aggregate data effortlessly.
- **Visualization**: Generate professional-grade charts like bar charts, word clouds, heat maps, and Gantt charts.
- **Report Generation**: Create detailed PDF or text reports directly from your data files.

---

## **Features**

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

### Cross-Platform
	  - Runs on Linux, macOS, and Windows and Docker Environments

---

## **Table of Contents**
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

---

## **Installation**

### **Requirements**
- Python 3.7+
- Pip (Python package manager)
- Docker (Optional, for containerized execution)

### **Install via pip**
```bash
pip install TidyDataCLI
```

### **Install from Source**
1. Clone the repository:
   ```bash
   git clone https://github.com/Siam3h/tidydatacli.git
   ```
2. Navigate to the directory:
   ```bash
   cd tidydatacli
   ```
3. Install the package:
   ```bash
   pip install .
   ```

### **Running with Docker**
For a containerized approach:
1. Pull the Docker image:
   ```bash
   docker pull tidydatacli
   ```
2. Run TidyDataCLI via Docker:
   ```bash
   docker run -v $(pwd):/data tidydatacli tidydata <command> --input /data/input.csv --output /data/output.csv
   ```

---

## **Usage**

Once installed, TidyDataCLI can be invoked using the following syntax:

```bash
tidydata <command> [options]
```

### **Example Commands**

#### Cleaning Data:
```bash
tidydata clean --input data.csv --output cleaned_data.csv --remove_duplicates --clean_columns
```

#### Transforming Data:
```bash
tidydata transform --input data.csv --output transformed.csv --sort column1 --filter "age > 30"
```

#### Visualizing Data:
```bash
tidydata visualize --input data.csv --type bar --x category --y sales --output bar_chart.png
```

#### Generating Reports:
```bash
tidydata report --input data.csv --output report.pdf --format pdf --summary
```


## **Commands Overview**

### 1. `clean`
Clean your dataset by removing duplicates, trimming spaces, or performing regex-based cleaning.

### 2. `transform`
Apply transformations such as sorting, filtering, adding columns, and custom lambda functions.

### 3. `visualize`
Create visual representations of your data, such as bar charts, pie charts, and word clouds.

### 4. `report`
Generate reports in **text** or **PDF** format with customizable summaries or detailed outputs.


## **Running with Docker**

To avoid dependency management, you can use Docker:
```bash
docker run -v $(pwd):/data tidydatacli tidydata clean --input /data/input.csv --output /data/output.csv
```


## **Error Handling**

Error messages are displayed for common issues like file not found, invalid columns, or missing options.

Example error:
```bash
Error: Input file 'non_existent_file.csv' not found.
```


## **Contributing**

We welcome contributions!  
1. Fork the repository.
2. Create a new branch.
3. Make your changes and submit a pull request.

Find issues or suggestions? Please open an [issue](https://github.com/Siam3h/tidydatacli/issues) on GitHub.


## **License**

TidyDataCLI is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## **Contact**

For any questions or issues, please contact Siama at [siamaphilbert@outlook.com](mailto:siamaphilbert@outlook.com).
