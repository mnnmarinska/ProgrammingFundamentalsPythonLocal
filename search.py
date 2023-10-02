n = int(input())
command = input()

list_to_print = []
list_with_correct_command = []
list_to_split = []
for word in range(n):
    sentence = input()
    list_to_print.append(sentence)
for word_2 in list_to_print:
    if command in word_2:
        list_with_correct_command.append(word_2)
print(list_to_print)
print(list_with_correct_command)