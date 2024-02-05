class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.user_name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("007", "deddia")
user2 = User("008", "permana")

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

