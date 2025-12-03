from ptest import *
from NewDB import NewDB
from NewTable import NewTable

def main():
    dbname = input("Enter the DB name: ") + ".db"
    # TODO: Implement dbname input into the NewDB class
    db = NewDB(dbname)
    table = NewTable(db)
    db.appenddata(table)
    db.close()

main()