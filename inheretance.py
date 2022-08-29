class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.email = f'{lastname}{firstname}{age}'.lower()

    #def welcome(self):
        print('welcome,',self.firstname,self.lastname,',to the class of')

    def allInfo(self):
        return f'Firstname:{self.firstname}\nLastname:{self.lastname}\nemailname:{self.email}' 

class Student(Person):
    def __init__(self,firstname,lastname,age):
        super().__init__(self,firstname,lastname,age,)
             

x = Person('haruna','joe',200)
print(x.firstname)
print(x.age)
print()
print(Person.allInfo(x))
print()
print('welcome,',self.firstname,self.lastname,'to the class of')