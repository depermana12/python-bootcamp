

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


student_grades = {}


for score in student_scores:
    if student_scores[score] > 91 and student_scores[score] < 100:
       student_grades[score] = "Outstanding"
    elif student_scores[score] > 81 and student_scores[score] < 91:
        student_grades[score] = "Exceeds expetation"
    elif student_scores[score] > 70 and student_scores[score] < 81:
        student_grades[score] = "Acceptable"
    else:
        student_grades[score] = "Fail"

print(student_grades)