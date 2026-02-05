arr = [2, 3, -8, 7, -1, 2, 3]

max_sum = arr[0]

for i in range(len(arr)):
    current_sum = 0
    for j in range(i, len(arr)):
        current_sum += arr[j]
        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)
