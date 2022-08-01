# Q2 : Find the maximum and minimum elements in an array
def minMax(max_min):
    max = max_min[0]
    min = max_min[0]
    for i in range(len(max_min)):
        if max_min[i] > max:
            max = max_min[i]
        elif max_min[i] < min:
            min = max_min[i]
    print("Maximum : ", max)
    print("Minimum : ", min)


max_min = [2, 5, 3, 88, 23, 45, 12, 10, 0, -1]
minMax(max_min)
