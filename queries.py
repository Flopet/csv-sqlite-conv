import csv
import sqlite3

from ptest import *


# queries = {
# "create_table" : f"CREATE TABLE IF NOT EXISTS {tablename} ({columns})",
# "row_check" : f"SELECT * FROM {tablename} WHERE ({columns}) = ({values});"
# "insert"
# "small_list"
# "long_list"
# "full_list"
# }

class NewDB:
    def __init__(self, dbname):
        self.name = dbname

        ##################################################
        #   Connect to the SQLite database
        ##################################################
        try:
            # Connect to the DB
            self.db = sqlite3.connect(self.name)
            print(f"Successfully connected to the database: {self.name}")
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")

        #Create cursor object
        self.cursor = self.db.cursor()

    ##################################################
    #   Append data from a CSV file to a table in the DB
    ##################################################
    def appenddata(self, table):
        with open(table.csv) as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                values = ""
                for cell in row:
                    values += f"'{row[cell]}', "
                values = values[:-2]

                self.cursor.execute(f"INSERT OR IGNORE INTO {table.name} VALUES ({values});")
        print(f"Appended data from {table.csv} to DB table '{table.name}'.")
        self.commit()

    ##################################################
    #   Commit changes to the database
    ##################################################
    def commit(self):
        try:
            self.db.commit()
            print(f"- Committed changes to database {self.name}.")
        except sqlite3.Error as e:
            print(f"Error committing changes to the database: {e}")

    ##################################################
    #   Close the database connection
    ##################################################
    def close(self):
        self.db.close()
        print(f"Closed connection to database {self.name}.")

class NewTable:
    def __init__(self, db, csvfile):
        self.db = db
        self.csv = csvfile
        self.name = csvfile.split('.')[0]
        cursor = db.cursor

        ##################################################
        #   Get the field names from the CSV file and return
        #   them as a comma-separated string to be used in
        #   the SQL queries
        ##################################################
        with open(self.csv) as csvfile:
            csvreader = csv.DictReader(csvfile)
            fields = csvreader.fieldnames
            ptest(fields, "CSV Fields")
            self.columns = ", ".join(fields)
            columns_with_types = ""

            # Ask user for data types for each field
            for field in fields:
                column_type = input(f"Enter the data type for {field}: ").upper()
                acceptable_types = ["TEXT", "INTEGER", "REAL"]
                while column_type not in acceptable_types:
                    print(f"Invalid data type '{column_type}'. Please enter one of the following: {acceptable_types}")
                    column_type = input(f"Enter the data type for {field}: ").upper()
                columns_with_types += f"{field} {column_type}, "
        query = f"CREATE TABLE IF NOT EXISTS {self.name} ({columns_with_types}UNIQUE({self.columns}));"

        ##################################################
        #   Generate a tablename based on the CSV filename and
        #   create a new table in the database with the fields
        #   specified in the CSV file.
        ##################################################
        # Check if table already exists in database
        table_list = cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table';").fetchone()
        if table_list is not None:
            if self.name in table_list:
                ask = input(f"Table {self.name} already exists. Would you like to add to existing table? (y/n)").lower()
                while ask != "y" and ask != "n":
                    ask = input(f"Invalid input. Please enter 'y' or 'n'.").lower()
                if ask == "y":
                    cursor.execute(f"DROP TABLE {self.name};")
                elif ask == "n":
                    # If the table already exists and the user doesnt want
                    # to overwrite the current, ask user for a new table name.
                    new_name = input(f"What would you like to name this new table (lowercase with underscores)? ")
                    self.name = new_name

        # UNIQUE(col1, col2, col3, ...) Restricts the table to contain unique rows
        query = f"CREATE TABLE IF NOT EXISTS {self.name} ({columns_with_types}UNIQUE({self.columns}));"

        # Ask user if column types should be strictly enforced or not
        options = ["y", "n"]
        strict = input("Do you want to enforce strict data types? (y/n): ").lower()
        if strict == options[0]:
            query = query[:-1] + " STRICT" + query[-1:]
        cursor.execute(query)

        print(f"Created table {self.name} in database {db.name}.")
        db.commit()




