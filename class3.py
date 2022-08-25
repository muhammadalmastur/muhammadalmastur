class Student:
    """
    This is a student class that gathers info about each student object.Student.__dict__
    this text was written in a docstring
    """
    # class variable
    split_age = 1.05
    
    # constructor
    def __init__(self, firstname,lastname,level,age):
        # declare instance variables
        self.firstname = firstname
        self.lastname = lastname
        self.email = f'{lastname}{firstname}@student.com'.lower()
        self.level = level
        self.age = age



    def allInfo(self):
        return f'Firstname:{self.firstname}\nLastname:{self.lastname}\nemailname:{self.email}'    

class Teacher(Student):
    def __init__(self,firstname,lastname,level):
        super().__init__(firstname,lastname,level)

std = Student('John','tanko',200,45)
print(Student.allInfo(std))

print(std.firstname)
print(std)