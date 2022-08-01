# Q1.Reverse the array
# s is starting element
# e is ending element

def reverseElement(a, s, e):
    while s < e:
        a[s], a[e] = a[e], a[s]
        s += 1
        e -= 1


a = [23, 4, 2, 76, 22, 90, 21]
reverseElement(a, 0, 6)
print("Reverse Element : ", a)
