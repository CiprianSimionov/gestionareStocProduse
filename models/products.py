"""cream modelul(obiectul) pentru aplicatia noastra(gestionare stoc produse"""
from db.crud.products_crud import ProductsDB
import uuid


class Product:
    def __init__(self, product_name, description, ingredients, price, weight, quantity, id=None):
        self.id = id or str(uuid.uuid4())
        self.product_name = product_name
        self.description = description
        self.ingredients = ingredients
        self.price = price
        self.weight = weight
        self.quantity = quantity
        self.product_db = ProductsDB()

    def add(self):
        product_data = self.dict_product()
        with ProductsDB() as db:
            db.create(product_data)



    def update(self):
        product_data = self.dict_product()
        with ProductsDB() as db:
            db.update(product_data, self.id)


    def delete(self):
        with ProductsDB() as db:
            db.delete(self.id)


    def dict_product(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "description": self.description,
            "ingredients": self.ingredients,
            "price": self.price,
            "weight": self.weight,
            "quantity": self.quantity
        }

    def __repr__(self):
        return (f"Produsul are id-ul: {self.id} \n"
                f"Numele produsului este: {self.product_name} \n"
                f"Descrierea produsului: {self.description} \n"
                f"Ingredientele produsului: {self.ingredients} \n"
                f"Pretul produsului: {self.price} \n"
                f"Greutatea produsului: {self.weight} \n"
                f"Cantitatea de produs: {self.quantity}")