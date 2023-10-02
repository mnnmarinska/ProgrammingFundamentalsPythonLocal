n = int(input())

list_numbers = []
filtered_numbers = []

for numbers in range(n):
    current_number = int(input())
    list_numbers.append(current_number)
command = input()
if command == "even":
    for num in list_numbers:
        if num % 2 == 0:
            filtered_numbers.append(num)
elif command == "odd":
    for num in list_numbers:
        if num % 2 != 0:
            filtered_numbers.append(num)
elif command == "negative":
    for num in list_numbers:
        if num < 0:
            filtered_numbers.append(num)
elif command == "positive":
    for num in list_numbers:
        if num >= 0:
            filtered_numbers.append(num)
print(filtered_numbers)