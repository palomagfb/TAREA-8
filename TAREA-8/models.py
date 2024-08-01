class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_item(self, index):
        return self.items[index]

    def display_items(self):
        print("+------+-----------+-------+------+
| 番号 | 商品名 | 金額 | 数量 |
+======+===========+=======+======+")
        for i, item in enumerate(self.items):
            print(f"| {i:<4} | {item.name:<9} | {item.price:<5} | {item.quantity:<4} |")
        print("+------+-----------+-------+------+")

class ShoppingCart:
    def __init__(self, owner, wallet):
        self.owner = owner
        self.wallet = wallet
        self.items = []

    def add_item(self, item, quantity):
        if item.quantity >= quantity:
            self.items.append((item, quantity))
            item.quantity -= quantity
        else:
            print("在庫が足りません")

    def display_cart(self):
        print("+------+-------+-------+------+
| 番号 | 商品名 | 金額 | 数量 |
+======+=======+=======+======+")
        for i, (item, quantity) in enumerate(self.items):
            print(f"| {i:<4} | {item.name:<5} | {item.price:<5} | {quantity:<4} |")
        print("+------+-------+-------+------+")

    def total_cost(self):
        return sum(item.price * quantity for item, quantity in self.items)

    def check_out(self, store):
        total = self.total_cost()
        if self.wallet >= total:
            self.wallet -= total
            print(f"😱👛 {self.owner}のウォレット残高: {self.wallet}")
            for item, quantity in self.items:
                store.add_item(Item(item.name, item.price, quantity))
            self.items = []
        else:
            print("ウォレットの残高が足りません")
