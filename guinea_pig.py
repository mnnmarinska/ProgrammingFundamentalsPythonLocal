food = float(input())
hay = float(input())
cover = float(input())

guinea_pig_weight = float(input())

month = 30
daily_food = 0.300

not_enough = False

for day in range(1, month + 1):
    food -= daily_food
    if day % 2 == 0:
        hay -= food * 0.05

    if day % 3 == 0:
        cover -= guinea_pig_weight / 3

    if food <= 0 or hay <= 0 or cover <= 0:
        not_enough = True
        break

if not not_enough:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")

