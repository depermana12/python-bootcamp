studentScores = input("please enter a list of student heights separated by space: ").split()
print(studentScores)
for n in range (0, len(studentScores)):
    studentScores[n] = int(studentScores[n])

print(studentScores)

highScores = 0
for scores in studentScores:
    if scores > highScores:
        highScores = scores

print(f"the highest score in the class is: {highScores}")
    
   