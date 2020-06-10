import pyodbc


class Data_base_connection():

    def __init__(self, database='Northwind', server='databases2.spartaglobal.academy', username='SA',
                 password='Passw0rd2018'):
        # 1) DB server connection variables
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        # Making connection and cursor
        self.conn = self._establish_conn()
        self.cursor = self.conn.cursor()

    def _establish_conn(self):
        con = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        return con

    def sql_query(self, sql_string):
        return self.cursor.execute(sql_string)


# nwind = Data_base_connection()
#
# print(nwind.sql_query("SELECT * FROM Products"))
