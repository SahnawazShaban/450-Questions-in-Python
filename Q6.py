# Q6 : Find the Union and Intersection of the two sorted arrays.
def unionFunction(l1, l2, union1, intersect1):
    m = len(l1)
    n = len(l2)
    for i in range(0, m):
        if l1[i] not in union1:
            union1.append(l1[i])

    for i in range(0, n):
        if l2[i] not in union1:
            union1.append(l2[i])

    for i in range(0, m):
        if l1[i] in l2:
            intersect1.append(l1[i])

    for i in range(0, n):
        if l2[i] in l1:
            intersect1.append(l2[i])


l1 = [1, 2, 4, 5, 6, 7, 8]
l2 = [3, 2, 4, 7, 8]
union1 = []
intersect1 = []
unionFunction(l1, l2, union1, intersect1)

print("Union : ", sorted(union1))
print("Intersect : ", sorted(set(intersect1)))
