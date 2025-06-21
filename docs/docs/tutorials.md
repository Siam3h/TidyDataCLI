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