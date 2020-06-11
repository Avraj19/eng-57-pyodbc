from db_connection_oop import Data_base_connection

class DB_customer(Data_base_connection):

    def insert_customer(self):
        customer_name = input(' What is the company name? \n')
        cus_id = input('What is the comapany ID?\n')
        return self.sql_query(f"INSERT INTO Customers (CustomerID, CompanyName) VALUES('{cus_id}','{customer_name}')")

    def get_all_cus(self, customer_name=None):
        result_list = []
        if customer_name is None:
            q_result = self.sql_query("SELECT * FROM Customers")
        else:
            q_result = self.sql_query(f"SELECT * FROM Customers WHERE CompanyName LIKe %{customer_name}")
        while True:
            row = q_result.fetchone()
            if row is None:
                break
            result_list.append(row)

        return result_list













cus = DB_customer()

new_cus = cus.insert_customer()


for i in cus.get_all_cus():
    print(i)