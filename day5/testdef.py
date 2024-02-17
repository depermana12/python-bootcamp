

studentScores = input("please enter a list of student heights separated by space: ").split()
print(studentScores)
for n in range (0, len(studentScores)):
    studentScores[n] = int(studentScores[n])


def find_highest (numofdata):
    highScores = 0
    for scores in numofdata:
        if scores > highScores:
            highScores = scores
    return highScores

result = find_highest(studentScores)
print(f"the highest score in the class is: {result}")
    
   