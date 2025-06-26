class Circle():
    __pi = 3.14   #"_po" - means protected and cannot be used outised the class
     #_ _pi - hides the atribute logic and protects it from being over weritten 
    def __init__(self,diameter):
        self.diameter = diameter 
        self.radius = diameter/2

    def calculate_circumference(self):
        return 2* Circle.__pi*self.radius
    

    def calculate_area(self):
        return Circle.__pi * (self.radius ** 2)
    
    def calculate_area_of_sector(self,angle):
        return (angle / 360) * Circle.__pi * (self.radius ** 2)
