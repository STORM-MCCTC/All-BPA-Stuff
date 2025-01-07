class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(self.name)
        print(self.grade)

    def is_passing(self):
        if self.grade >= 60:
            passing = True
        else:
            passing = False

        return passing

student_1 = student("John", 95)
student_2 = student("Jane", 60)
student_3 = student("Bob", 74)
student_4 = student("James", 45)

print("----------------------------------")
student_1.display_info()
print(student_1.is_passing())
print("----------------------------------")
student_2.display_info()
print(student_2.is_passing())
print("----------------------------------")
student_3.display_info()
print(student_3.is_passing())
print("----------------------------------")
student_4.display_info()
print(student_4.is_passing())
print("----------------------------------")