class Storage():
    def __init__(self, capacity :int):
        self.capacity = capacity
        self.storage = []

    
    def add_product(self, product :str):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage
    

storage_capacity = int(input())

storage =  Storage(storage_capacity)

print()
