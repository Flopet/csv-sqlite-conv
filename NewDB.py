import csv
import sqlite3

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
            print(f"- Committed changes to database {self.name}.\n")
        except sqlite3.Error as e:
            print(f"Error committing changes to the database: {e}")

    ##################################################
    #   Close the database connection
    ##################################################
    def close(self):
        self.db.close()
        print(f"Closed connection to database {self.name}.")