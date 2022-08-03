# Q4 : Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo.

abc = [1, 1, 2, 2, 2, 2, 1, 1, 2, 0, 0, 1, 2, 1]

for i in range(len(abc)):
    if abc[i] == 0:
        print(abc[i], end=" ")

for i in range(len(abc)):
    if abc[i] == 1:
        print(abc[i], end=" ")

for i in range(len(abc)):
    if abc[i] == 2:
        print(abc[i], end=" ")

