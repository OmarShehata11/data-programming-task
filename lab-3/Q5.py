grades = []
num_students = int(input("Enter number of students: "))

for i in range(num_students):
  grade = int(input("Enter grade for student {}: ".format(i+1)))
  grades.append(grade)

# a
invalid_count = 0
for grade in grades:
  if grade < 0 or grade > 100:
    print("Invalid")
    invalid_count += 1
  else:
    print("Valid")
print("Invalid grades:", invalid_count)  

# b
validity_list = []
for grade in grades:
  if grade >= 0 and grade <= 100:
    validity_list.append(1)
  else:
    validity_list.append(0)

print(validity_list)

# c  
total = sum(grades)
avg = total / num_students
print("Average grade:", avg)

# d
max_grade = max(grades)
max_idx = grades.index(max_grade)
print("Highest grade:", max_grade, "at index", max_idx)  

min_grade = min(grades)
min_idx = grades.index(min_grade)
print("Lowest grade:", min_grade, "at index", min_idx)

# e
above_85 = [grade for grade in grades if grade > 85]
print(len(above_85), "students above 85%")

# f
above_avg = [grade for grade in grades if grade > avg]   
print(len(above_avg), "students above average")
