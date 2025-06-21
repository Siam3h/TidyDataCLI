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




