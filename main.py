
class Supplier:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Shop:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

class Flower:
    def __init__(self, id, name, price, shop_id):
        self.id = id
        self.name = name
        self.price = price
        self.shop_id = shop_id

class Bouquet:
    def __init__(self, id, flowers, price, shop_id):
        self.id = id
        self.flowers = flowers
        self.price = price
        self.shop_id = shop_id

class Client:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Delivery:
    def __init__(self, id, supplier_id, shop_id, flower, flower_count, price, data):
        self.id = id
        self.supplier_id = supplier_id
        self.shop_id = shop_id
        self.flower = flower
        self.flower_count = flower_count
        self.price = price
        self.data = data


class Repository:
    def __init__(self):
        self.suppliers = []
        self.shops = []
        self.flowers = []
        self.bouquets = []
        self.clients = []
        self.delivery = []

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def add_shop(self, shop):
        self.shops.append(shop)

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_bouquet(self, bouquet):
        self.bouquets.append(bouquet)

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
repo.add_flower(flower1)
repo.add_flower(flower2)


bouquet1 = Bouquet(1, [flower1, flower2], 20.0, 1)
repo.add_bouquet(bouquet1)


client1 = Client(1, "Андрей")
client2 = Client(2, "Иван")
repo.add_client(client1)
repo.add_client(client2)


print("Поставщики:", repo.get_all_suppliers())
print("Магазины:", repo.get_all_shops())
print("Цветы:", repo.get_all_flowers())
print("Букеты:", repo.get_all_bouquets())
print("Покупатели:", repo.get_all_clients())
