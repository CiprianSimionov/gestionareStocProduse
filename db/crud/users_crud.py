"""implement crud methods for table users"""
from db.crud.interface_crud import CrudABC

class UsersDB(CrudABC):

    def __init__(self):
        super().__init__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


    def create(self, date_de_intrare_create):
        SQL_QUERY = """
            INSERT INTO users(
            id, username, first_name, last_name, email, password) 
            VALUES (:id, :username, :first_name, :last_name, :email, :password);
        """
        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY, date_de_intrare_create)
        self.connection.commit()


    def read(self, id=None, username=None, email=None):
        SQL_QUERY = " SELECT * FROM users "

        value = ""

        if id:
            SQL_QUERY += "WHERE id = ?;"
            value = id
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY, (value,))
        elif username:
            SQL_QUERY += "WHERE username = ?;"
            value = username
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY, (value,))
        elif email:
            SQL_QUERY += "WHERE email = ?;"
            value = email
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY, (value,))

        else:
            cursor = self.connection.cursor()
            cursor.execute(SQL_QUERY)
            users = cursor.fetchall()


        user_json = []
        for user in users:
            user_json.append({
                "id": user[0],
                "username": user[1],
                "first_name": user[2],
                "last_name": user[3],
                "email": user[4],
                "password": user[5]
            })
        return user_json

    def update(self, date_de_intrare_update, user_id):
        SQL_QUERY = """
                UPDATE users SET username=:username, first_name=:first_name, last_name=:last_name, email=:email, password=:password
                WHERE id=:id;
                """

        cursor = self.connection.cursor()
        date_de_intrare_update["id"] = user_id
        cursor.execute(SQL_QUERY, date_de_intrare_update)
        self.connection.commit()

    def delete(self, id):
        SQL_QUERY = """
        DELETE FROM users where id = ?;
        """
        cursor = self.connection.cursor()
        cursor.execute(SQL_QUERY, (id,))
        self.connection.commit()