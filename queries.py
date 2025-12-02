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


    def appenddata(self, table):
        with open(table.csv) as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                values = ""
                for cell in row:
                    values += f"'{row[cell]}', "
                values = values[:-2]
                if not table.rowcheck(values):
                    self.cursor.execute(f"INSERT INTO {table.name} VALUES ({values});")
                    print(f"Added row: {values}")
                else:
                    continue
        self.commit()

    ##################################################
    #   Commit changes to the database
    ##################################################
    def commit(self):
        try:
            self.db.commit()
            print(f"--- Committed changes to database {self.name}.")
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
            self.columns = ", ".join(fields)

        ##################################################
        #   Generate a tablename based on the CSV filename and
        #   create a new table in the database with the fields
        #   specified in the CSV file.
        ##################################################
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.name} ({self.columns});")
        print(f"Created table {self.name} in database {db.name}.")
        db.commit()

    ##################################################
    #   Check the table for a duplicate row based on the
    #   specified values.
    ##################################################
    def rowcheck(self, values):
        cursor = self.db.cursor
        check = cursor.execute(f"SELECT * FROM {self.name} WHERE ({self.columns}) = ({values});")

        if check.fetchone() is None:
            return False
        else:
            return True




