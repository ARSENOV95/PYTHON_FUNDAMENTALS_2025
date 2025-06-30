class Catalogue:
   
    def __init__ (self, name :str):
        self.name = name
        self.products = []

    def add_product(self,product_name :str):
        if product_name.isalpha():
          self.products.append(product_name)
          return product_name
    
    def get_by_letter(self,first_letter: str):
        return [prod for prod in self.products if prod.startswith(first_letter)] 

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(sorted(self.products))
        return result



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)