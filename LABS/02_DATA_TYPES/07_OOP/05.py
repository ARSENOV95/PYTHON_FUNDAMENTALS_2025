class Class():

    __students_count = 22

    def __init__(self,name :str): #we define the initall object attributes clas 11b will have a name - 11b, two lists - student names and grades 
        self.name = name
        self.students = []
        self.grades = []      
         # we define class valtiable for the total number of students, this valriable will be elidgable for all instances of the  object


    def add_student(self,name: str, grade: float): # first instance method is add student, for each insatance we add a student, we will add his name in students and grades
        if Class.__students_count > 0:
           self.students.append(name)
           self.grades.append(grade)

           Class.__students_count -= 1 #after each instance we will removed one student form the count until 0 
        
        
    def get_average_grade(self): #after all students are added we will calcutalte the average grade and return the result
        average_grade = 0
        if  self.students:
            average_grade = sum(self.grades)/len(self.grades)

        return average_grade
    
    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {Class.get_average_grade(self):.2f}" #i nthe end we will print the class name list ofe students
                                                                                                                          #and call the resutl of the method for hte grade 


a_class = Class("11B")
print(a_class)

