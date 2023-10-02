single_string = input().split(" ")

list_opposite_nums = []

for num in single_string:
    current_num = int(num)
    opposite_num = -current_num
    list_opposite_nums.append(opposite_num)
print(list_opposite_nums)