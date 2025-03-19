class Student:
    grade = 4

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def update_grade(cls, grade):   # these are the method to update class varibles 
        cls.grade = grade

    @staticmethod
    def check_age(age):   # these are just common method not related with object
        if age > 18:
            print('Above 18')
        else:
            print('Below 18')

    def get_data(self):
        print({'name': self.name, 'age': self.age, 'grade': self.grade})



s1 = Student('abc', 45)
s2 = Student('def', 32)
s1.get_data()
s2.get_data()

s1.grade = 45   # this will only change for object s1 not for all
s1.get_data()
s2.get_data()


Student.update_grade(38)  # this will change for every object
Student.check_age(34)
s1.check_age(34)

s1.get_data()  # 45
s2.get_data()  # 38


Instance variable overrides class variable: Once s1.grade = 45 was set, s1 stopped referring to the class variable.
Class variable update does not affect instances with an overridden variable: Student.update_grade(38) updated the class-level grade, which is why s2 now has 38, but s1 retains 45.