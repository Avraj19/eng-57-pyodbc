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
            q_result = self.sql_query("SELECT *"
                                      "FROM Products"
                                      f"WHERE ProductName LIKe %{product_name}")
        while True:
            row = q_result.fetchone()
            if row is None:
                break
            result_list.append(row)

        return result_list


pro_table = DB_product_table()

print(pro_table.get_by_id(1))
