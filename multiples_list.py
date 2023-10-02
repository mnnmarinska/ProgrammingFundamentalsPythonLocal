factor = int(input())
count = int(input())

my_list = []
count_num = 0

for num in range(count):
    count_num += 1
    next_num = count_num*factor
    my_list.append(next_num)
print(my_list)