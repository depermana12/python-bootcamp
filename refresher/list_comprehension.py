numbers = [1, 2, 3]
doubled = [i * 2 for i in numbers]

print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Jen"]
start_s = [friend for friend in friends if friend.startswith("S")]

print(start_s)

""" 
The variable list is stored in the stack with different addresses,

print("friends", id(friends), "start_s", id(start_s))

if you compare 2 different list even with the same element value, you got False.
However if you compare index element with the same value you got True
"""