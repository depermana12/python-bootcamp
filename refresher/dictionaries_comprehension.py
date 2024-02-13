users = [
    (0, "Bob", "pass123"),
    (0, "Rolf", "pass456"),
    (0, "Jane", "pass789"),
    (0, "Patrick", "pass321"),
]
"""
make user[1] index as key, and iterate the tuple as a value.
this is helpful, because we can access information using username
"""
username_mapping = {user[1]: user for user in users}
print(username_mapping)
print(username_mapping["Bob"])


username_input = input("Enter your username: ")
password_input = input("Enter your password: ")
"""
destructuring the tuple, id, username, and password
using username as a key, it will return the information for destructure
"""
_, username, password = username_mapping[username_input]

if password_input == password:
    print("Login successfully")
else:
    print("Incorrect password")