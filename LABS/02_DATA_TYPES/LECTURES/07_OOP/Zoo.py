class Zoo ():

    __animal_count = 0


    def __init__(self, zoo_name :str):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []


    def add_animal(self,species :str,name :str):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)   
        
        Zoo.__animal_count += 1

    def get_info(self,species :str):
        result = ''
        if species == "mammal":
            result += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species == "bird":            
            result += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"       
        result += f"Total animals: {Zoo.__animal_count}"
        
        return result

z_name = input()
num_animals = int(input())

zoo = Zoo(z_name)

for animal in range(num_animals):
    current_animal = input().split()
    animal_species = current_animal[0]
    animal_type = current_animal[1]

    zoo.add_animal(animal_species,animal_type)

species_ = input()

print(zoo.get_info(species_))