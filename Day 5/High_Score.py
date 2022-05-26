# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
begin = student_scores[0]
for val in student_scores:
    if begin < val:
        begin = val
print(f"The highest score in the class is: {begin}")
