groceries_list = input().split("!")
command = input()

while command != "Go Shopping!":
    command_parts = command.split()
    action = command_parts[0]
    food = command_parts[1]

    if action == "Urgent":
        if food not in groceries_list:
            groceries_list.insert(0, food)

    elif action == "Unnecessary":
        if food in groceries_list:
            groceries_list.remove(food)

    elif action == "Correct":
        if food in groceries_list:
            new_item = command_parts[2]
            index = groceries_list.index(food)
            groceries_list[index] = new_item

    elif action == "Rearrange":
        if food in groceries_list:
            groceries_list.remove(food)
            groceries_list.append(food)

    command = input()

print(", ".join(groceries_list))
