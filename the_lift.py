people_waiting = int(input())
state_of_the_lift_places = list(map(int, input().split()))
filled_lift = []
full_seat = 4

for space in state_of_the_lift_places:
    while space < full_seat and people_waiting > 0:
        space += 1
        people_waiting -= 1
    filled_lift.append(space)

if people_waiting == 0 and sum(filled_lift) < len(filled_lift) * full_seat:
    print("The lift has empty spots!")
elif people_waiting > 0 and sum(filled_lift) == len(filled_lift) * full_seat:
    print(f"There isn't enough space! {people_waiting} people in a queue!")

print(" ".join(map(str, filled_lift)))






# РАБОТЕЩИ КОДОВЕ

# people_waiting = int(input())
# state_of_the_lift_places = list(map(int, input().split()))
# filled_lift = []
#
# for space in range(len(state_of_the_lift_places)):
#     while state_of_the_lift_places[space] < 4 and people_waiting > 0:
#         state_of_the_lift_places[space] += 1
#         people_waiting -= 1
#
# if people_waiting == 0 and sum(state_of_the_lift_places) < len(state_of_the_lift_places) * 4:
#     print("The lift has empty spots!")
# elif people_waiting > 0 and sum(state_of_the_lift_places) == len(state_of_the_lift_places) * 4:
#     print(f"There isn't enough space! {people_waiting} people in a queue!")
#
# print(" ".join(map(str, state_of_the_lift_places)))
