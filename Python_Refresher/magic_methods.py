class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Person is {self.name}, and his age is {self.age}."

    def __repr__(self):
        return f"<Person({self.name},{self.age})>"


bob=Person("Bob",25)
print(bob)