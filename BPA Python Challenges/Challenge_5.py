class student:
    def __init__(self, name, grade): 
        self.name = name
        self.grade = grade

    def display_info(self): #displaying student info
        print(self.name)
        print(self.grade)

    def is_passing(self): # check if the student is passing
        if self.grade >= 60: # Check if the grade is 60 or higher
            passing = True
        else:
            passing = False

        return passing

student_1 = student("John", 95) #create students
student_2 = student("Jane", 60)
student_3 = student("Bob", 74)
student_4 = student("James", 45)

# Print information for each student
print("----------------------------------")
student_1.display_info()  # Display student 1's info
print(student_1.is_passing())  # print if student 1 is passing
print("----------------------------------")
student_2.display_info()  # Display student 2's info
print(student_2.is_passing())  # print if student 2 is passing
print("----------------------------------")
student_3.display_info()  # Display student 3's info
print(student_3.is_passing())  # print if student 3 is passing
print("----------------------------------")
student_4.display_info()  # Display student 4's info
print(student_4.is_passing())  # print if student 4 is passing
print("----------------------------------")