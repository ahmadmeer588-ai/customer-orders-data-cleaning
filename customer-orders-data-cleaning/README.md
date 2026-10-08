# Customer Orders Data Cleaning

## Project Overview

This project focuses on cleaning and validating a messy customer orders dataset using Python and Pandas.

The original dataset contained inconsistent formatting, missing values, mixed date formats, duplicate records, inconsistent country and category names, and non-numeric order amounts.

The goal was to transform the raw dataset into a clean, consistent, and analysis-ready dataset while preserving information wherever possible.

## Tools & Technologies

* Python
* Pandas
* Excel
* CSV
* VS Code

## Dataset

The dataset contains customer and order-related information with the following columns:

* `CustomerID`
* `Name`
* `Email`
* `Phone`
* `Country`
* `SignupDate`
* `Category`
* `OrderAmount`

The original dataset contained **155 rows and 8 columns**.

## Data Cleaning Process

### 1. Removed Empty Rows

Completely empty rows were identified and removed from the dataset.

### 2. Removed Repeated Header Row

A repeated column-header row was present inside the dataset and was removed.

### 3. Cleaned Order Amount

The `OrderAmount` column contained values with:

* Currency symbols
* `USD` text
* Commas
* Parentheses representing negative values
* Missing values

These values were cleaned and converted into a numeric `CleanOrderAmount` column.

### 4. Standardized Signup Dates

The dataset contained dates in multiple formats, including:

* `21-Nov-2022`
* `02-26-21`
* `2022-07-24`
* `August 10, 2022`
* `09/30/2023`

The dates were converted into a consistent datetime format.

### 5. Cleaned Customer Names

Names were standardized by:

* Removing leading/trailing spaces
* Removing inconsistent internal spacing
* Standardizing capitalization

### 6. Cleaned Email Addresses

Email values were:

* Trimmed
* Converted to lowercase
* Validated using a basic email-format check

Missing email addresses were retained because no reliable source was available to recover them.

### 7. Standardized Phone Numbers

Phone numbers contained different formatting styles such as parentheses, spaces, hyphens, and periods.

Formatting characters were removed while preserving the `+` sign where present.

Phone numbers were kept as strings because they are identifiers rather than numerical quantities.

### 8. Normalized Country Names

Different representations of the same country were standardized.

Examples:

* `USA`, `US`, `U.S.A.` → `United States`
* `UK`, `U.K.`, `Britain` → `United Kingdom`
* `CA` → `Canada`
* `KSA`, `S. Arabia` → `Saudi Arabia`
* `DE` → `Germany`
* `AUS` → `Australia`

### 9. Normalized Categories

Inconsistent capitalization, spelling, and naming were standardized.

Examples:

* `SPORTS`, `sports`, `Sport` → `Sports`
* `electronics`, `Electronic`, `ELECTRONICS` → `Electronics`
* `Book`, `BOOKS`, `Books` → `Books`
* `Toy`, `TOYS`, `toys` → `Toys`
* `Cloths`, `Apparel` → `Clothing`
* `Home&Garden`, `Home & garden` → `Home & Garden`

### 10. Investigated Missing Values

Missing values were investigated rather than automatically filled.

Where no reliable source existed to recover the information, the missing values were retained as `NaN`.

This prevented the introduction of fabricated data.

### 11. Investigated Duplicate Records

Exact duplicate records were identified and inspected before removal.

Seven duplicate records were removed because the duplicated rows matched across all columns.

### 12. Data Type Validation

Final data types were checked and corrected where necessary.

* `CustomerID` → integer
* `Name` → string
* `Email` → string
* `Phone` → string
* `Country` → string
* `SignupDate` → datetime
* `Category` → string
* `CleanOrderAmount` → float

## Data Quality Decisions

An important part of this project was deciding **what not to change**.

Missing values were not blindly replaced with guesses.

Negative order amounts were also preserved because they may represent legitimate business events such as refunds, reversals, or adjustments. Without a defined business rule, deleting them could result in information loss.

## Final Dataset

After cleaning and validation:

* **Rows:** 142
* **Columns:** 8
* **Duplicate rows:** 0
* **CustomerID missing:** 0
* **Name missing:** 0
* **SignupDate missing:** 0

Some missing values remain in `Email`, `Phone`, `Country`, `Category`, and `CleanOrderAmount` because reliable replacement values were not available.

## Project Structure

```text
customer-orders-data-cleaning/
│
├── data/
│   ├── raw_customer_orders.xlsx
│   └── cleaned_customer_orders.csv
│
├── data_cleaning.py
│
└── README.md
```

## Outcome

The original messy dataset was transformed into a validated, analysis-ready dataset while maintaining data integrity and documenting important cleaning decisions.

This project demonstrates practical experience with:

* Data cleaning
* Data validation
* Missing-value investigation
* Duplicate detection
* Data type conversion
* Pandas
* Business-oriented data quality decisions
