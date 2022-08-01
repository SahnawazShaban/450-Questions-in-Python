*****************************************************************
# Q1.Reverse the array
# s is starting element
# e is ending element

def reverseElement(test_list, s, e):
    while s < e:
        test_list[s], test_list[e] = test_list[e], test_list[s]
        s += 1
        e -= 1


test_list = [23, 4, 2, 76, 22, 90, 21]
reverseElement(test_list, 0, 6)
print("Reverse Element : ", test_list)


EXTRA : 
#for string

def reverseElement(test_list, s, e):
    while s < e:
        test_list[s], test_list[e] = test_list[e], test_list[s]
        s += 1
        e -= 1


test_list = ["shaan", "rohit", "maisa", "maitry", "somil", "akki", "sam"]
reverseElement(test_list, 0, 6)
print("Reverse Element : ", test_list)

****************************************************************

#reverse a string element - single element

def nameReverse(l1):
    for i in l1:
        res = l1[::-1]
    print(res)


l1 = "shaan"
nameReverse(l1)
print(l1)

****************************************************************

#reverse a string element - multiple element

def reverseElement(test_list, s, e):
    while s < e:
        test_list[s], test_list[e] = test_list[e], test_list[s]
        s += 1
        e -= 1
        res = [i[::-1] for i in test_list]
    print("The reversed string list is : ", str(res))


test_list = ["shaan", "rohit", "maisa", "maitry", "somil", "akki", "sam"]
reverseElement(test_list, 0, 6)
