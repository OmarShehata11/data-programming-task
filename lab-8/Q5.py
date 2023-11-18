def scoreToGrade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:  
        grade = 'B'
    elif score >= 70:
        grade = 'C'    
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return grade


scores = input("enter grades with spaces between them > ").split()
scores = [ int(x) for x in scores]

grades = []

for i in scores:
    grades.append(scoreToGrade(i))
    
print(grades)
    
