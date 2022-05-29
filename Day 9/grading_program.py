student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student_name in student_scores.keys():
    score = student_scores[student_name]
    if score > 90:
        student_grades[student_name] = 'Outstanding'
    elif 90 >= score > 80:
        student_grades[student_name] = 'Exceeds Expectations'
    elif 80 >= score > 70:
        student_grades[student_name] = 'Acceptable'
    elif score < 70:
        student_grades[student_name] = 'Fail'

        # 🚨 Don't change the code below 👇
print(student_grades)
