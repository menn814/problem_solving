Student=[]
for _ in range (int(input())):
    name = input()
    grade = float(input())
    Student.append([name,grade])
grade = sorted(set(student[1] for student in Student))
lowest =grade[1]
names =sorted(student[0] for student in Student if student[1] == lowest)
for name in names:
    print(name)