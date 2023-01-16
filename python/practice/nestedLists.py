students = []
grades = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append(name)
    grades.append(score)   

# find second lowest grade
lowestGrade = min(grades)
remainingGrades = [i for i in grades if i != lowestGrade]
secondLowestGrade = min(remainingGrades)

secondLowestStudents = []
for grade in remainingGrades:
    if grade == secondLowestGrade:
        index = grades.index(secondLowestGrade)
        student = students[index]            
        secondLowestStudents.append(student)
        del grades[index]
        del students[index]

sortedList = sorted(secondLowestStudents)
for student in sortedList:
    print(student)    
