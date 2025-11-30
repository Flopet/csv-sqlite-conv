import csv
import sqlite3

def main():
    file = input("Enter the CSV file name: ")
    dbname = file.split('.')[0] + ".db"
    db = sqlite3.connect(dbname)
    fields, parsed_data = parsecsv(file)
    createtable(dbname, db, fields, parsed_data)


def parsecsv(file):
    parsed = []
    with open(file) as csvfile:
        csvreader = csv.DictReader(csvfile)
        fields = csvreader.fieldnames
        for row in csvreader:
            parsed.append(row)

    print(f"""
    Fields: {fields}
    Data: {parsed} 
    """)
    return fields, parsed


def createtable(dbname, db, fields, parsed_data):
    cursor = db.cursor()
    table = dbname.split('.')[0]
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {table} ({','.join(fields)});
    """)
    for row in parsed_data:
        def getvalues(row):
            values = ""
            for field in fields:
                values += f'"{row[field]}",'
            return values[:-1]

        cursor.execute(f"""
        INSERT INTO {table} VALUES ({getvalues(row)}); 
        """)
    db.commit()
    db.close()


if __name__ == '__main__':
    main()