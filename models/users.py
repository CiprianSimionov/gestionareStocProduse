"""cream modelul(obiectul) pentru aplicatia noastra(gestionare stoc produse"""

from db.crud.users_crud import  UsersDB

class User:

    def __init__(self, username, first_name, last_name, email, password, confirm_password = None, id = None):
        self.id = id
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
        pass

    def delete_user(self):
        if not self.id:
            raise Exception("Avem nevoie de id pentru a sterge utilizatorul.")
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