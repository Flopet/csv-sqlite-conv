# CSV to SQLite Converter

A Python-based command-line tool that converts CSV files into SQLite databases with customizable table schemas and data type enforcement.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Inputs and Behavior](#inputs-and-behavior)
  - [Example Session](#example-session)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
  - [Core Components](#core-components)
  - [Key Features Implementation](#key-features-implementation)
- [Sample Data](#sample-data)
- [Troubleshooting & Error Handling](#troubleshooting--error-handling)
  - [Common Issues](#common-issues)
- [Development](#development)
  - [Running Tests](#running-tests)
  - [`ptest.py`](#ptestpy)
  - [Contributing](#contributing)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Overview

This tool provides a quick and efficient way to:
- Import CSV data into SQLite databases
- Define custom data types for each column
- Handle duplicate prevention with unique constraints
- Choose between strict and flexible type enforcement
- Manage existing tables (overwrite or create new ones)

## Features

- **Interactive Setup**: Guided prompts for database name, CSV file selection, and column configuration
- **Type Safety**: Choose from `TEXT`, `INTEGER`, or `REAL` data types for each column
- **Duplicate Prevention**: Unique constraints are automatically enabled to avoid duplicate row entries
- **Flexible Schema**: Option for strict type enforcement or SQLite's dynamic typing
- **Error Handling**: Robust file validation and database connection management
- **Column Normalization**: Automatic conversion of column names (spaces to underscores, lowercase)

## Requirements

- Python 3.x
- SQLite3 (included with Python standard library)
- CSV files **with headers**

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd csv-sqlite-conv
```

2. **No additional dependencies required! This uses standard Python libraries only!**

## Usage

### Basic Usage

Run the main script and follow the instructions in your console:

```bash
python main.py
```

### Inputs and Behavior

1. **Database Name**: Enter the desired database name (`.db` extension added automatically)
2. **CSV File**: Specify the CSV filename (`.csv` extension added automatically)
3. **Column Types**: For each column in your CSV, specify the SQLite data type:
   - `TEXT` - For strings and text data
   - `INTEGER` - For whole numbers
   - `REAL` - For decimal numbers
4. **Table Management**: If a table with the same name exists, choose to overwrite or create a new one
5. **Type Enforcement**: Choose whether to enable SQLite's `STRICT` mode for type enforcement

### Example Session

```
Enter the DB name: contacts
Enter the CSV file name: test

Fields in CSV file: ['name', 'phone', 'email']

Enter the data type for name: TEXT
Enter the data type for phone: TEXT  
Enter the data type for email: TEXT

Do you want to strictly enforce data types? (y/n): y

Created table test in database contacts.db.
Appended data from test.csv to DB table 'test'.
- Committed changes to database contacts.db.

Closed connection to database contacts.db.
```

## Project Structure

```
csv-sqlite-conv/
├── main.py          # Main entry point and user interface
├── NewDB.py         # Database connection and data insertion logic
├── NewTable.py      # Table creation and CSV parsing logic  
├── ptest.py         # Testing utilities
├── test.csv         # Sample CSV file for testing
├── big_test.csv     # Large sample CSV file
└── README.md        # This documentation
```

## Architecture

### Core Components

#### `NewDB` Class
- Manages SQLite database connections
- Handles data insertion from CSV files
- Provides transaction management (commit/rollback)
- Uses parameterized queries to prevent SQL injection

#### `NewTable` Class  
- Parses CSV headers and creates table schemas
- Interactive column type specification
- Handles table name conflicts
- Normalizes column names for SQL compatibility
- Supports both strict and dynamic typing modes

#### `main.py`
- Orchestrates the conversion process
- Provides user interface for configuration
- Coordinates database and table creation

### Key Features Implementation

#### Data Type Mapping
The tool maps CSV data to SQLite types:
- **TEXT**: String data, phone numbers, emails, general text
- **INTEGER**: Whole numbers, IDs, counts
- **REAL**: Decimal numbers, prices, measurements

#### Column Name Normalization
CSV headers are automatically normalized:
- Spaces replaced with underscores
- Converted to lowercase  
- Quoted for SQL compatibility

Example: `"First Name"` → `"first_name"`

#### Duplicate Prevention
All tables include a UNIQUE constraint across all columns:
```sql
UNIQUE("column1", "column2", "column3")
```

#### Strict Mode Support
When enabled, SQLite STRICT mode enforces declared column types:
```sql
CREATE TABLE example (...) STRICT
```

## Sample Data

The project includes some basic sample CSV files:
- `test.csv` - Small contact list for testing
- `big_test.csv` - 10k row dataset for performance testing

⭐️ **I recommend trying out the program with larger datasets. The performance my surprise you!
Additional sample CSV files available at: [datablist/sample-csv-files](https://github.com/datablist/sample-csv-files)**

## Troubleshooting & Error Handling

- **File Not Found**: 3 attempts to locate CSV files with helpful error messages
- **Database Connection**: Graceful handling of SQLite connection errors
- **Invalid Data Types**: Validation of user input for column types
- **Table Conflicts**: Interactive resolution of existing table names

### Common Issues

**"File not found" errors**
- Ensure CSV files are in the project directory
- Enter filename without extension
- Check file permissions

**Database connection errors**
- Verify write permissions in project directory
- Check available disk space
- Ensure SQLite3 is properly installed

**Data import issues**
- Verify CSV has proper headers
- Check for encoding issues (UTF-8 recommended)
- Ensure data matches declared column types (in strict mode)

## Development

### Running Tests

The project includes some basic testing utilities I wrote to print
out information in a way that can be easily seen identified in the console
for troubleshooting or debugging.

### `ptest.py`:

```python
from ptest import ptest, dbtest

# Test a function and print it's return value in an easily identifiable way
# ptest( [TEST FUNCTION], [STRING] )
ptest(test(), "test name")

Output:
    ====================
    Test Name: test_name
    Output: This was a test!
    ====================

# Test database and table objects
# dbtest( [DB_OBJECT], [TABLE_OBJECT] )
dbtest(test_db, test_table)

Output:
    |   DB Test Results
    |___________________________
    |
    | db = <NewDB.NewDB object at 0x123456789>
    | db.name = test.db
    | db.cursor = <sqlite3.Cursor object at 0x123456789>
    |_______________
    |   
    | table = <NewTable.NewTable object at 0x123456789>
    | table.csvfile = test.csv
    | table.tablename = test
    | table.columns = "name", "phone", "email"
    |____________________________
    |
    | tables available in db: [('test',)]

```

### Contributing

This is a learning project.
Feel free to report any issues or suggest any changes that may help me clean things up for increase efficiency! 

## Future Enhancements

Potential improvements:
- **Batch Processing**: Support for multiple CSV files
- **Type Inference**: Automatic data type detection
- **Configuration Files**: Save/load conversion settings
- **Progress Indicators**: For large file processing
- **Export Options**: Convert SQLite back to CSV
- **Advanced Constraints**: Foreign keys, custom validations

## License

This project is for educational purposes.