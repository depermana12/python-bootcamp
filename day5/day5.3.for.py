

studentHeights = input("please enter a list of student heights separated by space: ").split()
print(studentHeights)
for n in range (0, len(studentHeights)):
    studentHeights[n] = int(studentHeights[n])

print(studentHeights)


totalHeight = 0
for height in studentHeights:
    totalHeight += height

print(totalHeight)

totalStudent = 0
for student in studentHeights:
    totalStudent += 1
    print(student)

print(totalStudent)

average = round(totalHeight / totalStudent)

print(average)