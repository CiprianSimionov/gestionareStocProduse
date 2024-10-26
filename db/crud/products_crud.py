"""implement crud methods for table products"""
from db.crud.interface_crud import CrudABC

class ProductsDB(CrudABC):

    def __init__(self):
        super().__init__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
    def create(self, date_de_intrare_create):
        SQL_QUERY = """
        INSERT INTO products(
        id, product_name, description, ingredients, price, weight, quantity)
        VALUES (:id, :product_name, :description, :ingredients, :price, :weight, :quantity)
        """

        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY, date_de_intrare_create)
        self.connection.commit()


    def read(self, id=None, product_name = None):
        SQL_QUERY = "SELECT * FROM products "

        value = ""
        if id:
            SQL_QUERY += "WHERE id = ?;"
            value = id
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY, (value,))
        elif product_name:
            SQL_QUERY += "WHERE product_name = ?;"
            value = product_name
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY, (value,))
        else:
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY)
            products = cursor.fetchall()


        product_json = []
        for product in products:
            product_json.append({
                "id": product[0],
                "product_name": product[1],
                "description": product[2],
                "ingredients": product[3],
                "price": product[4],
                "weight": product[5],
                "quantity": product[6]
            })
        return product_json



    def update(self, date_de_intrare_update, product_id):
        SQL_QUERY = """
        UPDATE products SET product_name=:product_name, description=:description, ingredients=:ingredients, price=:price, weight=:weight, quantity=:quantity
        WHERE id=:id;
        """

        #product_name (numele coloanei)
        # =: semn de atribuire
        #product_name atribuit (parametri)

        cursor = self.connection.cursor()
        date_de_intrare_update["id"] = product_id
        cursor.execute(SQL_QUERY, date_de_intrare_update)
        self.connection.commit()


    def delete(self, id):
        SQL_QUERY = """
        DELETE FROM products where id = ?;
        """
        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY, (id,))
        self.connection.commit()