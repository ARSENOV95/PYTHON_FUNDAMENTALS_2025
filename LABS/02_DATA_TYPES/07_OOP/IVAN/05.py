class Class:

    __students_count = 22

    def __init__(self, name :str):
        self.name = name
        self.students = []
        self.grades = []


    def add_student(self,name: str, grade: float):
        if Class.__students_count > len(self.students): #checks if there are sptos left 
            self.students.append(name)
            self.grades.append(grade)
    
    def get_average_grade(self):
        average_grade = sum(self.grades)/len(self.students)
        return float(f"{average_grade:.2f}")

    def __repr__(self):
        average_grade = self.get_average_grade(self)
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {average_grade}"
        

    

