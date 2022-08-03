# Q5 : Move all the negative elements to one side of the array
l = [-3, -1, 5, 2, 4, -2, 8, 4, -7]

for i in range(len(l)):
    if l[i]>0:
        print(l[i],end=" ")

for i in range(len(l)):
    if l[i]<0:
        print(l[i], end=" ")
