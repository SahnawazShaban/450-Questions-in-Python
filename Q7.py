# Q7 : Write a program to cyclically rotate an array by one.

arr = [1, 4, 6, 2, 4, 5, 7, 9]
a=len(arr)-1
print(arr[a])
for i in range(0, a):
    j = i - 1
    arr[j] = arr[i]
    print(arr[i])
