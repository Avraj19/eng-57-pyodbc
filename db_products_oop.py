from db_connection_oop import Data_base_connection


class DB_product_table(Data_base_connection):

    # def __init__(self):
    #     super().__init__()

    def get_by_id(self, id_num):
        return self.sql_query("SELECT * FROM Products WHERE ProductID=" + str(id_num)).fetchone()

    def get_all(self, product_name=None):
        result_list = []
        if product_name is None:
            q_result = self.sql_query("SELECT * FROM Products")
        else:
            q_result = self.sql_query(f"SELECT * FROM Products WHERE ProductName LIKe %{product_name}")
        while True:
            row = q_result.fetchone()
            if row is None:
                break
            result_list.append(row)

        return result_list

    def insert_prduct(self):
        product_name = input(' What is the product name? \n')
        return self.sql_query(f"INSERT INTO Products(ProductName) VALUES('{product_name}')")

        # product_name = input(' What is the product name? \n')
        # supplier_id = int(input(' What is the supplerID? \n'))
        # category_id = int(input(' What is the categoryID? \n'))
        # quantity_per_unit = input(' What is the quantity per unit? \n')
        # unit_price = int(input(' What is the unit price? \n'))
        # units_in_stock = int(input(' What is the units in stock? \n'))
        # units_on_order = int(input(' What is the units on order? \n'))
        # ReorderLevel = int(input(' What is the record level? \n'))
        # Discontinued = int(input('Is it discontinued? \n'))
        # if Discontinued == 1:
        #     Discontinued = True
        # elif Discontinued == 0:
        #     Discontinued = False
        # return self.sql_query("INSERT INTO Products("
        #                       "ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, "
        #                       "UnitsOnOrder, ReorderLevel, Discontinued) "
        #                       "VALUES("
        #                       f"{product_name}, str({supplier_id}), {category_id}, {quantity_per_unit}, {unit_price}, {units_in_stock}, "
        #                       f"{units_on_order}, {ReorderLevel}, {Discontinued}) ")


pro_table = DB_product_table()

# print(pro_table.get_by_id(1))
# # Tests the insert
# pro_table.insert_prduct()
#
# # Prints out list
# for i in pro_table.get_all():
#     print(i)