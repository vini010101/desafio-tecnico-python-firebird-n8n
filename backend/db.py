import fdb

con = fdb.connect(
    host='localhost',
    database='/firebird/data/employee.fdb',
    user='sysdba',
    password='masterkey'
)
