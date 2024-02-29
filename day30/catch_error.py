def make_pie(index):
    fruits = ["Apple", "Pear", "Orange"]
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + " pie")


make_pie(1)


facebook_likes = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Shares': 3}
]

total_likes = 0
for post in facebook_likes:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass


print(total_likes)
