class Catalogue:
    def __init__(self, name:str):
        self.name = name
        self.products = []

    def add_products(self,product_name :str):
        self.products.append(product_name)


    def get_by_letter(self,first_letter :str):
        return [product for product in self.products if [product.startswith(first_letter)]]
    

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n" 
        result += '\n'.join(sorted(self.products))
        return result