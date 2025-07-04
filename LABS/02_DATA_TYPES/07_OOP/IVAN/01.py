class Storage:
    storage = []

    def __init__(self,capacity : int):
        self.capacity = capacity

    def add_product(self,product :str):
        if self.capacity > 0:
            self.capacity -= 1
            Storage.storage.append(product)

    def get_products(slef):
        return Storage.storage