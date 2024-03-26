from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Supplier:
    id: int
    name: str

@dataclass(frozen=True)
class Shop:
    id: int
    name: str
    address: str

@dataclass(frozen=True)
class Flower:
    id: int
    name: str
    price: float
    shop_id: int


@dataclass(frozen=True)
class Client:
    id: int
    name: str

@dataclass(frozen=True)
class Bouquet:
    id: int
    flowers: List[Flower]
    price: float
    shop_id: int

@dataclass(frozen=True)
class Delivery:
    id: int
    supplier_id: int
    shop_id: int
    flower: str
    flower_count: int
    price: float
    data: str

@dataclass(frozen=True)
class Purchase:
    id: int
    bouquet_id: int
    client_id: int

"""""
class Bouquet:
    def __init__(self, id, flowers, price, shop_id):
        self.id = id
        self.flowers = flowers
        self.price = price
        self.shop_id = shop_id

    def __eq__(self, other):
        return (
                isinstance(other, Bouquet) and
                self.id == other.id and
                self.flowers == other.flowers and
                self.price == other.price and
                self.shop_id == other.shop_id
        )




class Delivery:
    def __init__(self, id, supplier_id, shop_id, flower, flower_count, price, data):
        self.id = id
        self.supplier_id = supplier_id
        self.shop_id = shop_id
        self.flower = flower
        self.flower_count = flower_count
        self.price = price
        self.data = data

    def __eq__(self, other):
        return (
                isinstance(other, Delivery) and
                self.id == other.id and
                self.supplier_id == other.supplier_id and
                self.shop_id == other.shop_id and
                self.flower == other.flower and
                self.flower_count == other.flower_count and
                self.price == other.price and
                self.data == other.data
        )
"""

class Repository:
    def __init__(self):
        self.suppliers = []
        self.shops = []
        self.flowers = []
        self.bouquets = []
        self.clients = []
        self.delivery = []
        self.purchases = []

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def add_shop(self, shop):
        self.shops.append(shop)

    def add_flower(self, flower):
        self.flowers.append(flower)

   # def add_bouquet(self, bouquet):
    #    self.bouquets.append(bouquet)

    def add_client(self, client):
        self.clients.append(client)

    def add_delivery(self, delivery):
        self.clients.append(delivery)


    def get_all_suppliers(self):
        return self.suppliers

    def get_all_shops(self):
        return self.shops

    def get_all_flowers(self):
        return self.flowers

    def get_all_bouquets(self):
        return self.bouquets

    def get_all_clients(self):
        return self.clients

    def get_all_delivery(self):
        return self.delivery

    def get_all_purchase(self):
        return self.purchases


    def delivery_flowers(self, delivery):

        pass

    def create_bouquet(self, bouquet):
        if not isinstance(bouquet.id, int):
            raise TypeError(f"Expected 'id' to be of type int")
        if not isinstance(bouquet.flowers, List):
            raise TypeError(f"Expected 'flowers' to be of type List")
        if not isinstance(bouquet.price, float):
            raise TypeError(f"Expected 'price' to be of type float")
        if not isinstance(bouquet.shop_id, int):
            raise TypeError(f"Expected 'shop_id' to be of type int")

        for i in self.bouquets:
            if i.id == bouquet.id:
                raise ValueError(f"A bouquet with this id already exists")

        for flower in bouquet.flowers:
            if flower not in self.flowers:
                raise ValueError("Invalid flower not in the list")

        lt = False
        for i in self.shops:
            if i.id == bouquet.shop_id:
                lt = True

        if lt == False:
            raise ValueError("There is no store with this id")
        self.bouquets.append(bouquet)

    def purchase_bouquet(self, purchase):
        if not isinstance(purchase.id, int):
            raise TypeError(f"Expected 'id' to be of type int")
        if not isinstance(purchase.client_id, int):
            raise TypeError(f"Expected 'client_id' to be of type int")
        if not isinstance(purchase.bouquet_id, int):
            raise TypeError(f"Expected 'bouquet_id' to be of type int")

        for i in self.purchases:
            if i.id == purchase.id:
                raise ValueError(f"A purchase with this id already exists")
        lt = False
        for i in self.shops:
            if i.id == purchase.bouquet_id:
                lt = True
        if lt == False:
            raise ValueError("There is no bouquet with this id")

        cl = False
        for i in self.clients:
            if i.id == purchase.client_id:
                cl = True
        if cl == False:
            raise ValueError("There is no client with this id")
        self.purchases.append(purchase)

repo = Repository()


supplier1 = Supplier(1, "ИП Степанов")
supplier2 = Supplier(2, "ИП Бобров")
repo.add_supplier(supplier1)
repo.add_supplier(supplier2)


shop1 = Shop(1, "Красивый букет", "Калинина 1")
shop2 = Shop(2, "Красивый букет", "Ленини 20")
repo.add_shop(shop1)
repo.add_shop(shop2)


flower1 = Flower(1, "Роза", 10, 1)
flower2 = Flower(2, "Тюльпан", 8, 1)
flower3 = Flower(3, "Тюл", 8, 1)
repo.add_flower(flower1)
repo.add_flower(flower2)


bouquet1 = Bouquet(1, [flower2, flower1], 20.0, 1)
bouquet2 = Bouquet(2, [flower2, flower1], 20.0, 1)
repo.create_bouquet(bouquet1)
repo.create_bouquet(bouquet2)





client1 = Client(1, "Андрей")
client2 = Client(2, "Иван")
repo.add_client(client1)
repo.add_client(client2)

purchase1 = Purchase(1, 1, 1)
repo.purchase_bouquet(purchase1)

print("Поставщики:", repo.get_all_suppliers())
print("Магазины:", repo.get_all_shops())
print("Цветы:", repo.get_all_flowers())
print("Букеты:", repo.get_all_bouquets())
print("Покупатели:", repo.get_all_clients())
print("Покупки:", repo.get_all_purchase())

