

def ptest(test_input, test_name = "ptest"):
    print(f"""
    ====================
    Test Name: {test_name}
    Output: {test_input}
    ====================
    """)

def dbtest(db, table):
    print(f"""
    |   DB Test Results
    |___________________________
    |
    | db = {db}
    | db.name = {db.name}
    | db.cursor = {db.cursor}
    |_______________
    |   
    | table = {table}
    | table.csvfile = {table.csv}
    | table.tablename = {table.name}
    | table.columns = {table.columns}
    |
        """)