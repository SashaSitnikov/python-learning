class Student:
    school = "College"
    
    def __init__(self, name):
        self.name = name
        
st1 = Student("Alex")
st2 = Student("John")
st1.school = "University"
print(st1.school, st2.school)
Student.school = "School"
print(st1.school, st2.school)