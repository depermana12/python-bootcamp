# multiple assign shortcuts
x, y = 5, 10

friends_hobby = {"Rolf": "Basketball", "Bob": "Soccer", "Anne": "Run"}

"""
convert into tuple using friends_hobby.item()
then destructure tuple, first tup element assign to friend and
second tup element assign to hobby
"""
for friend, hobby in friends_hobby.items():
    print(f"{friend}: {hobby}")


people = [
    ("Bob", 42, "Artist"),
    ("Jane", 30, "Model"),
    ("Lane", 35, "Programmer"),
]

for person in people:
    print((f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}"))


person_tup = ("Bob", 40, "Mechanic")

name, _, profession = person_tup
print(name, profession)