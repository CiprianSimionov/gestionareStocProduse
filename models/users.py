"""Create model(object) for current application"""

from db.crud.users_crud import UsersDB
import uuid


class User:

    def __init__(self, username, first_name, last_name, email, password, confirm_password=None, id=None):
        self.id = id or str(uuid.uuid4())
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.user_db = UsersDB()


    def add(self):
        self.user_db.create(self.dict_create())

    def update(self):
        user_data = self.dict_create()
        with UsersDB() as db:
            db.update(user_data, self.id)

    def delete_user(self):
        if not self.id:
            raise Exception("Id required in order to delete user.")
        self.user_db.delete(self.id)

    def dict_create(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password
        }