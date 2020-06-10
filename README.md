# Connecting Python with DB

This class will allow us to connect python with DB.

To do so, we will need a package called PYODBC.
- packages are external, while libraries are standered and do not need to be installed.

This package abstracts our connection to the DB.

## Installation of PYODBC
To install, in terminal type in:

```
pip install pyodbc
```

## How to use PYODBC
That's it, its installed but now how to use it. It's the same just import.

```python
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
# Printing con let u know if you are connected with the server
print(conn)
# Should print out something like
'<pyodbc.Connection object at 0x0000017ED8ABF6B0>'
```
- Make sure anything inside the brackets are a string.


