# sequence_of_elements = input().split()
# command = input()
# moves = 0
#
# while command != "end":
#     first_index, second_index = command.split()
#     moves += 1
#     first_index = int(first_index)
#     second_index = int(second_index)
#     if first_index == second_index \
#             or first_index not in range(len(sequence_of_elements)) \
#             or second_index not in range(len(sequence_of_elements)):
#         midpoint = (len(sequence_of_elements) // 2)
#         additional_element = "-" + str(moves) + "a"
#         sequence_of_elements = sequence_of_elements[:midpoint] + [additional_element] + [additional_element] + sequence_of_elements[midpoint:]
#         print("Invalid input! Adding additional elements to the board")
#     elif sequence_of_elements[first_index] == sequence_of_elements[second_index]:
#         print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
#         element_matched = sequence_of_elements[first_index]
#         sequence_of_elements.remove(element_matched)
#         sequence_of_elements.remove(element_matched)
#
#     elif sequence_of_elements[first_index] != sequence_of_elements[second_index]:
#         print("Try again!")
#     if len(sequence_of_elements) == 0:
#         print(f"You have won in {moves} turns!")
#         break
#     command = input()
#
# if command == "end" and len(sequence_of_elements) > 0:
#     print(f"Sorry you lose :(\n"
#           f"{' '.join(sequence_of_elements)}")


def add_additional_elements(sequence, moves):
    midpoint = len(sequence) // 2
    additional_element = f"-{moves}a"
    sequence = sequence[:midpoint] + [additional_element] * 2 + sequence[midpoint:]
    print("Invalid input! Adding additional elements to the board")
    return sequence

def main():
    sequence_of_elements = input().split()
    command = input()
    moves = 0

    while command != "end":
        first_index, second_index = map(int, command.split())
        moves += 1

        if (
            first_index == second_index
            or first_index < 0
            or first_index >= len(sequence_of_elements)
            or second_index < 0
            or second_index >= len(sequence_of_elements)
        ):
            sequence_of_elements = add_additional_elements(sequence_of_elements, moves)
        elif sequence_of_elements[first_index] == sequence_of_elements[second_index]:
            element_matched = sequence_of_elements[first_index]
            sequence_of_elements = [element for element in sequence_of_elements if element != element_matched]
            print(f"Congrats! You have found matching elements - {element_matched}!")
        else:
            print("Try again!")

        if len(sequence_of_elements) == 0:
            print(f"You have won in {moves} turns!")
            break

        command = input()

    if command == "end" and len(sequence_of_elements) > 0:
        print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")

if __name__ == "__main__":
    main()
