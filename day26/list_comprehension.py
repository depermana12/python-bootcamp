list_string = input().split(',')

list_num = [int(char) for char in list_string]

list_filter = [num for num in list_num if num % 2 == 0]
print(list_filter)