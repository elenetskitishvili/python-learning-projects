students = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 85),
            ("Eve", 78), ("Frank", 85), ("Mark", 50), ("George", 21)]


# 1)Unique Grades:
unique_grades = set([student[1]for student in students])
print(unique_grades)

# 2)Top Performers:
students_copy = [*students]
students_copy.sort(key=lambda student: student[1], reverse=True)
top_performers = [top_performer[0] for top_performer in students_copy[0:3]]
print(top_performers)


# 3)Failed Students:
failed_students = [student for student in students if student[1] < 51]
print(failed_students)
