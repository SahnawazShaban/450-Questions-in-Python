# Q8 : Find Largest sum contiguous Subarray [V. IMP]

arr = [9, 0, 8, -19, 5, 6, -5, 4, 30]
size = len(arr)
max_sub_arr = arr[0]
max_current = arr[0]

for i in range(1, size):
    max_current = max(arr[i], max_current + arr[i])
    max_sub_arr = max(max_sub_arr, max_current)

print("Sum : ", max_sub_arr)
