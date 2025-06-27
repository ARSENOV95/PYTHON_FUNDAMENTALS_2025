class Storage():
    def __init__(self,capacity : int):
        self.capacity = capacity
        self.storage = []

    def add_product(self):
            while len(self.storage) < self.capacity:
                product = input()
                self.storage.append(product)


    
    def get_products(self):
        return self.storage
    

storage = int(input())

store = Storage(storage)

store.add_product()
print(store.get_products())