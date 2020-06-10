import pyodbc

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'

# establishing connection
con = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + password)


def print_row():
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        print(row)


# print('Testing connection\n' + str(con))

# Make a courser:

cursor = con.cursor()
# print('Testing cursor\n' + str(cursor))
# exe = cursor.execute
## Queries

### Q1 - How many orders in NWDB?
# num_of_orders = cursor.execute('SELECT COUNT(OrderID)'
#                                'FROM Orders')
# print_row()


### Q2 - How many order that the Ship City is Rio de Janeiro?
# q2 = cursor.execute('SELECT COUNT(OrderID)'
#                     'FROM Orders'
#                     'WHERE ShipCity LIKE \'Rio%\'')
#
# print_row()


### Q3 - Select all orders that the Ship City is Rio de Janeiro or Reims?
q3 = cursor.execute('SELECT OrderID'
                    'FROM Orders'
                    'WHERE ShipCity LIKE \'%Rio%\' OR ShipCity LIKE \'%Reims%\'')

# "SELECT COUNT(OrderID)"
#                     "FROM Orders"
#                     "WHERE ShipCity LIKE '%Rio%' OR ShipCity LIKE '%Reims%'"
print_row()
### Q4 - Select all of the entries where the Company name has a z or a Z in the table of Customers


### Q5 - We need to update all of our FAX information! This Day and age it is a must! :sweat_smile::sweat_smile::sweat_smile: Find me the Name of All of the companies that we do not have their FAX numbers! I would also like to know with whom I need to speak with, their contact numbers and what city they are base in.


### Q6 - Ahh there you are! My prize :star::star:SPARTANTS:star::star:! MY MARES AND MY STALLIONS! We need to re-target all of our Customers is Paris! Get me information on these clients.


### Q7 - WAIT! Where are you going? (...) These clients are hard to sell too! We need more intel.. Can you find out, from these clients from Paris, whom orders the most by quantity? Who are our top 5 clients?


### Q8 - OMG What are you? Some kind of SQL Guardian Angel? THIS IS AMAZING! May God pay you handsomely :smile_cat: because I have no cash on me!..  I do have one more request. I need to know more about these these Paris client. Can you find out which ones their deliveries took longer than 10 days? Display the Business/client name, contact name, all their contact details (don't forget the fax!), as well as the number of deliveries that where overdue! Just add a column named: 'Number overdue orders'! simple, thank you!
