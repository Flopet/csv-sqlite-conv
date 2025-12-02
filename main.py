import csv
import sqlite3
from ptest import *
from queries import *

def main():
    #file = input("Enter the CSV file name: ") + ".csv"
    file = "test.csv"                 #TEST INPUT
    #dbname = input("Enter the DB name: ") + ".db"
    dbname = "test.db"                    #TEST INPUT

    db = NewDB(dbname)
    table = NewTable(db, file)

    db.appenddata(table)
    db.close()

main()