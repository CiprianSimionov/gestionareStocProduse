"""Creating models for app interactions"""
from db.db_connection import create_database
from models.products import Product
from db.crud.products_crud import ProductsDB
from models.users import User
from db.crud.users_crud import UsersDB




#user functions

def add_user(username, first_name, last_name, email, password):

        try:
            new_user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            new_user.add()
            print("User added successfully into the system")
        except Exception as e:
            print(f"Following error adding user: {e}")

def update_user(user_id, username, first_name, last_name, email, password):
    try:
        user_updated = User(id=user_id, username=username, first_name=first_name, last_name=last_name,
                                  email=email, password=password)
        user_updated.update()
        print("User updated.")
    except Exception as e:
        print(f"Error is: {e}")

def delete_user(user_id):
    try:
        deleted_user = User(id=user_id, username="", first_name="", last_name="", email="", password="")
        deleted_user.delete_user()
        print("User deleted.")
    except Exception as e:
        print(f"Error is: {e}")

def all_users():
    users_db = UsersDB()
    users = users_db.read()
    for user in users:
        print(f"Id: {user['id']}, username: {user['username']}, email: {user['email']}")

def get_info_user():
    username = input("Insert username: ")
    first_name = input("Insert first name: ")
    last_name = input("Insert last name: ")
    email = input("Insert your email: ")
    password = input("Insert your password: ")
    return username, first_name, last_name, email, password

def get_info_user_id():
    return input("Insert your id: ")


#product functions

def add_product(name, description, ingredients, price, weight, quantity):
    try:
        new_product = Product(product_name=name, description=description, ingredients=ingredients, price=price, weight=weight, quantity=quantity)
        new_product.add()
        print("Product added successfully into the system")
    except Exception as e:
        print(f"Following error adding product: {e}")

def update_product(product_id, name, description, ingredients, price, weight, quantity):
    try:
        product_updated = Product(id=product_id, product_name=name, description=description, ingredients=ingredients, price=price, weight=weight, quantity=quantity)
        product_updated.update()
        print("Product updated.")
    except Exception as e:
        print(f"Error is: {e}")


def delete_product(product_id):
    try:
        produs_sters = Product(id=product_id, product_name="", description="", ingredients="", price=None, weight=None, quantity=None)
        produs_sters.delete()
        print("Product deleted.")
    except Exception as e:
        print(f"Error is: {e}")

def all_products():
    products_db = ProductsDB()
    products = products_db.read()
    for product in products:
        print(f"Id: {product['id']}, product_name: {product['product_name']}, product_price: {product['price']}")

def get_info_product():
    name = input("Insert product name: ")
    description = input("Insert product description: ")
    ingredients = input("Insert ingredients: ")
    price = float(input("Insert product price: "))
    weight = int(input("Insert product weight(integer): "))
    quantity = int(input("Insert stock quantity: "))
    return name, description, ingredients, price, weight, quantity

def get_info_product_id():
    return input("Insert product id: ")

if __name__ == "__main__":
    create_database()
    print("What data would you like to enter into the system? ")
    print("1. Users")
    print("2. Products")
    option = input("Select one option: ")

    if option == "1":
        print("For users you have following operations: ")
        while True:
            print("1. Add user: ")
            print("2. Update user ")
            print("3. Delete user: ")
            print("4. List user: ")
            print("5. Exit")

            option = input("Select option: ")

            if option == "1":
                username, first_name, last_name, email, password = get_info_user()
                add_user(username, first_name, last_name, email, password)
                #print("User added.")
            elif option == "2":
                user_id = get_info_user_id()
                username, first_name, last_name, email, password = get_info_user()
                update_user(user_id, username, first_name, last_name, email, password)
                #print("User updated.")
            elif option == "3":
                user_id = get_info_user_id()
                delete_user(user_id)
                #print("User deleted.")
            elif option == "4":
                all_users()
                #print("List of available users.")
            elif option == "5":
                break

            else:
                print("Invalid option.Try again")


    elif option == "2":
        print("For products you have following operations: ")
        while True:
            print("1. Add product: ")
            print("2. Update product: ")
            print("3. Delete product: ")
            print("4. List products: ")
            print("5. Exit")

            option = input("Select option: ")

            if option == "1":
                name, description, ingredients, price, weight, quantity = get_info_product()
                add_product(name, description, ingredients, price, weight, quantity)
                #print("Product added.")
            elif option == "2":
                product_id = get_info_product_id()
                name, description, ingredients, price, weight, quantity = get_info_product()
                update_product(product_id, name, description, ingredients, price, weight, quantity)
                #print("Product updated.")
            elif option == "3":
                product_id = get_info_product_id()
                delete_product(product_id)
                #print("Product deleted.")
            elif option == "4":
                all_products()
                #print("Products list: ")
            elif option == "5":
                break
            else:
                print("Invalid option. Try again.")

    else:
        print("Invalid option. Try again..")



