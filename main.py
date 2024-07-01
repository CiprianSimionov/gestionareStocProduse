"""cream metodele pentru ca aplicatia sa fie interactiva"""
from db.db_connection import create_database
from models.products import Product
from db.crud.products_crud import ProductsDB

#functiile pentru user

def add_user(username, first_name, last_name, email, password, confirm_password):
    pass

def update_user(username, first_name, last_name, email, password):
    pass

def delete_user(id_user):
    pass

def all_users():
    pass

def get_info_user():
    username = input("Insert username: ")
    first_name = input("Insert first name: ")
    last_name = input("Insert last name: ")
    email = input("Insert your email: ")
    password = input("Insert your password: ")
    return username, first_name, last_name, email, password

def get_info_user_id():
    return input("Insert your id: ")

#functii pentru products

def add_product(name, description, ingredients, price, weight, quantity):
    try:
        produs_nou = Product(product_name=name, description=description, ingredients=ingredients, price=price, weight=weight, quantity=quantity)
        produs_nou.add()
        print("Produs adaugat cu succes in sistem")
    except Exception as e:
        print(f"Eroarea la adaugarea produsului este: {e}")

def update_product(product_id, name, description, ingredients, price, weight, quantity):
    try:
        produs_actualizat = Product(id=product_id, product_name=name, description=description, ingredients=ingredients, price=price, weight=weight, quantity=quantity)
        produs_actualizat.update()
        print("Produsul a fost actualizat.")
    except Exception as e:
        print(f"Eroarea este: {e}")


def delete_product(product_id):
    try:
        produs_sters = Product(id=product_id, product_name="", description="", ingredients="", price=None, weight=None, quantity=None)
        produs_sters.delete()
        print("Produsul a fost sters din sistem.")
    except Exception as e:
        print(f"Eroarea este: {e}")

def all_products():
    products_db = ProductsDB()
    produse = products_db.read()
    for produs in produse:
        print(f"Id: {produs['id']}, nume_produs: {produs['product_name']}")

def get_info_product():
    name = input("Insert product name: ")
    description = input("Insert product description: ")
    ingredients = input("Insert ingredients: ")
    price = float(input("Insert product price: "))
    weight = int(input("Insert weight: "))
    quantity = int(input("Insert the quantity: "))
    return name, description, ingredients, price, weight, quantity

def get_info_product_id():
    return input("Insert product id: ")

if __name__ == "__main__":
    create_database()
    print("Ce date vrei sa introduci in sistem? ")
    print("1. utilizatori")
    print("2. produse")
    optiune = input("Scrie una din cele 2 optiuni: ")

    if optiune == "1":
        print("Pentru utilizatori poti face urmatoarele operatiuni: ")

    elif optiune == "2":
        print("Pentru produse poti face urmatoarele operatiuni: ")
        while True:
            print("1. Add product: ")
            print("2. Update product: ")
            print("3. Delete product: ")
            print("4. List products: ")
            print("5. Exit")

            optiune = input("Scrie numarul operatiunii: ")

            if optiune == "1":

                name, description, ingredients, price, weight, quantity = get_info_product()
                add_product(name, description, ingredients, price, weight, quantity)
                print("Am adaugat produsul.")
            elif optiune == "2":
                product_id = get_info_product_id()
                name, description, ingredients, price, weight, quantity = get_info_product()
                update_product(product_id, name, description, ingredients, price, weight, quantity)
                print("Am actualizat produsul.")
            elif optiune == "3":
                product_id = get_info_product_id()
                delete_product(product_id)
                print("Am sters produsul.")
            elif optiune == "4":
                all_products()
                print("Lista produse: ")
            elif optiune == "5":
                break
            else:
                print("Nu exista aceasta optiune.Incearca din nou")

    else:
        print("Nu exista aceasta optiune. Incearca din nou.")



