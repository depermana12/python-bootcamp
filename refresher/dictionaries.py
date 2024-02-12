friend_ages = {"Rolf": 24, "Adam": 30, "Anne":27}

"""
to get the value from dictionaries you need to access them using the key subscript
friend_ages["Rolf"]
the same with changing the value of key, you access them using
key subscript and assign new value friend_ages["Rolf"] = 27
"""


friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]

print(friends[1])
print(friends[1]["name"])

"""
access list of dictionaries using index subscript
and access the dictionaries values using key subscript element
"""

friends_hobby = {"Rolf": "Basketball", "Bob": "Soccer", "Anne": "Run"}

# convert into tuple using friends_hobby.item()
for friend, hobby in friends_hobby.items():
    print(f"{friend}: {hobby}")


students_scores = {"Rolf": 80, "Bob": 90, "Anne": 85}

student_score = students_scores.values()
average = sum(student_score) / len(student_score)
print(average)