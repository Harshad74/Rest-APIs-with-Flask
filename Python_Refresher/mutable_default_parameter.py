from typing import List, Optional

class student:
    def __init__(self, name:str, grades: Optional[List[int]]= None):
        self.name=name
        self.grades=grades or []

    def take_exam(self,result: int):
        self.grades.append(result)

bob=student("Bob")
rolf=student("Rolf")
bob.take_exam(60)
print(bob.grades)
print(rolf.grades)