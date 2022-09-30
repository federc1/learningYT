import csv


class Item:

    pay_rate = 0.8  # Class attribute - The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # validating
        assert price >= 0, f"Price {price} is not greater than 0!"
        assert quantity >= 0, f"Must e greater than 0"

        # Assign to self instance - instance attribute
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to exec
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for i in items:
            Item(
                name=i.get("name"),
                price=float(i.get("price")),
                quantity=int(i.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones
