# Q3 : Find the "Kth" max and min element of an array

def minMax(mini, n, kth):
    mini.sort()
    print(sorted(mini))
    print(kth, "th smallest is ", mini[kth - 1])


mini = [2, 5, 3, 88, 23, 45, 12, 10, 0, -1]
n = len(mini)
kth = int(input("Enter Kth value : "))
minMax(mini, n, kth)


Difference between sort() vs sorted().
EXAMPLE : 
nums = [2, 3, 1, 5, 6, 4, 0]

print(sorted(nums))   # [0, 1, 2, 3, 4, 5, 6]
print(nums)           # [2, 3, 1, 5, 6, 4, 0]

print(nums.sort())    # None
print(nums)           # [0, 1, 2, 3, 4, 5, 6]
