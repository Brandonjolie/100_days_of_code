# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
student_heights = '180 124 165 173 189 169 146'.split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
count = 0
total = 0
for val in student_heights:
    total += val
    count += 1
print(total)
print(round((total/count)))
