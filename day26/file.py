with open("file1.txt") as file1:
    data_1 = file1.readlines()

with open("file2.txt") as file2:
    data_2 = file2.readlines()

new_data_3 = [int(num) for num in data_1 if num in data_2]

print(new_data_3)
