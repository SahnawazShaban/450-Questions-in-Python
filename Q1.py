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


EXTRA : 
#for string

def reverseElement(a, s, e):
    while s < e:
        a[s], a[e] = a[e], a[s]
        s += 1
        e -= 1


a = ["shaan", "rohit", "maisa", "maitry", "somil", "akki", "sam"]
reverseElement(a, 0, 6)
print("Reverse Element : ", a)

****************************************************************

#reverse a proper string

def nameReverse(l1):
    for i in l1:
        res = l1[::-1]
    print(res)


l1 = "shaan"
nameReverse(l1)
print(l1)
