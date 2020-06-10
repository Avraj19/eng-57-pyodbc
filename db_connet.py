import pyodbc

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'

# establishing connection
con = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + password)

print('Testing connection\n' + str(con))

# Make a courser:

cursor = con.cursor()
# print('Testing cursor\n' + str(cursor))

# Querying with python
query_redult = cursor.execute('SELECT * FROM Products')
# print(query_redult)
# # This will print out one row at a time
# print(query_redult.fetchone())
# # If you print again it will print the next line on the table
# print(query_redult.fetchone())
# print(query_redult.fetchone())
# print(query_redult.fetchone())
# # If you want to get back to the top of the table you will need to execute the program again.

# # This will the whole table
# # Form where you left, this means if you printed out a few lines with .fetchone(),
# # then this will continue on from there
# print(query_redult.fetchall())


data_point_card = query_redult.fetchone()

# # This one entry of data ia a pyodbc.row object
# print(type(data_point_card))

# # Behaves like an iterable list - organised with index
# print(data_point_card[1])

# # Also behave like a oop object, where the initialized parameters are the column name
# print(data_point_card.ProductName)

# # fetchall --> outputs all the pyodbc.row  (s) into list because it remains state
# # This is DANGOURS because it will slow down the server
list_all_rows = query_redult.fetchall()
# print(list_all_rows)

#####################################################################
# Search documentatio/or internet to use a while loop to get our all of the data using the .fetchone() method

# # This will get all the rows

# sql = 'SELECT * FROM Products'
# number_of_rows = cursor.execute(sql)

# while True:
#     row = cursor.fetchone()
#     if row is None:
#         break
#     print(row)

# # This will get the number of rows asked
# print(cursor.fetchmany(2))
