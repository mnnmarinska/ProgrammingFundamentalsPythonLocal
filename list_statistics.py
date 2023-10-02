n = int(input())

positives = []
negatives = []
count_positives = 0
sum_negatives = 0

for number in range(n):
    current_num = int(input())
    if current_num < 0:
        negatives.append(current_num)
        sum_negatives += current_num
    else:
        positives.append(current_num)
        count_positives += 1
print(positives)
print(negatives)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_negatives}")