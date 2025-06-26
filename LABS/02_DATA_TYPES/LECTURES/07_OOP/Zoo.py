class Zoo():
    __animals = 0

    def __init__(self,name :str):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self,species,name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fishes":
            self.fishes.append(name)
        elif species == "birds":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self,species):
        result = ''
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fishes":
            result += f"Fishes in {self.name}: {', '.join(self.mammals)}"
        else:
            result += f"Birds in {self.name}: {', '.join(self.mammals)}"          
        result += f"\nTotal animals: {Zoo.__animals}"
        return result


zoo_name = input()
num_animals = int(input())

zoo = Zoo(zoo_name)

for animal in range(num_animals):
    current_animal = input().split()
    species_ = current_animal[0]
    animal_name = current_animal[1]

    zoo.add_animal(species_,animal_name)

species = input()

print(zoo.get_info(species))
