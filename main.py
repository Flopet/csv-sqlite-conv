import csv
import sqlite3
from ptest import *

def main():
    file = input("Enter the CSV file name: ") + ".csv"
    # file = "big_test.csv"                 TEST INPUT
    dbname = input("Enter the DB name: ") + ".db"
    # dbname = "test.db"                    TEST INPUT
    fields, data = processcsv(file)
    createtable(file, dbname, fields, data)


def processcsv(file):
    data = [] # Empty list to store each row of data
    with open(file) as csvfile: # Open the CSV file
        csvreader = csv.DictReader(csvfile)
        fields = csvreader.fieldnames # Get the field names
        for row in csvreader:
            data.append(tuple(row.values())) # Convert each row into a tuple and append to the data list
                                             # Note: tuples are immutable, so we can't change their values after creation'

    print(f"""
    Fields: {fields}
    Data: {data[:3]} ... ({len(data)} rows total)) 
    """)
    return fields, data


def createtable(file, dbname, fields, table_data):
    db = sqlite3.connect(dbname) # Connect to the DB
    cursor = db.cursor() # Create a cursor object for the DB
    tablename = file.split('.')[0] # Extract the new table name from the DB name

    def newtablefields(current_fields):
        result = ""
        for field in current_fields:
            result += f"{field}, "
        result = result[:-2]
        ptest("newtablefields result", result)
        return result
    columns = newtablefields(fields)

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {tablename} ({columns});
    """)

    for row in table_data:
        values = ""
        for cell in row:
            values += f"'{cell}', "
        values = values[:-2]

        check = cursor.execute(f"SELECT * FROM {tablename} WHERE ({columns}) = ({values});").fetchone()

        if check is None:
            cursor.execute(f"""
                         INSERT INTO {tablename} ({columns}) VALUES ({values});
                         """)
            print(f"Added row: {values}")
        else:
            print("Duplicate row found. Skipping...")

    db.commit()
    db.close()


if __name__ == '__main__':
    main()