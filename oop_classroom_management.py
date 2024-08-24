class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def __str__(self):
        average = self.get_average_grade()
        return f"Name: {self.name}, Grades: {self.grades}, Average: {average:.2f}"


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, new_student):
        self.students.append(new_student)

    def get_top_students(self):
        top_students = sorted(
            self.students, key=lambda student: student.get_average_grade(), reverse=True)
        return top_students[:3]

    def get_failed_students(self):
        failed_students = [
            student for student in self.students if student.get_average_grade() < 51]
        return failed_students


# Students
student1 = Student("Ann")
student2 = Student("Nick")
student3 = Student("Mary")
student4 = Student("John")

# Add Grades
student1.add_grade(90)
student1.add_grade(73)
student1.add_grade(85)

student3.add_grade(72)
student3.add_grade(81)
student3.add_grade(68)

student2.add_grade(42)
student2.add_grade(50)
student2.add_grade(38)

student4.add_grade(96)
student4.add_grade(98)
student4.add_grade(97)

# Create a classroom and add students
classroom = Classroom()
classroom.add_student(student1)
classroom.add_student(student2)
classroom.add_student(student3)
classroom.add_student(student4)

# Top Students
classroom_top_students = classroom.get_top_students()
print("Top Students:")
for student in classroom_top_students:
    print(student)

# Failed Students
classroom_failed_students = classroom.get_failed_students()
print("\nFailed Students:")
for student in classroom_failed_students:
    print(student)
