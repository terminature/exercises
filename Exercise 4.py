'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

same_numbers = [x for x in a if x in b]

for x in a:
    if x in b:
        c.append(x)

print (same_numbers)'''


a = [1,1,1,6,7,8,9,4,9]
b = [1,6,87,98,67,45,10,11,12,13,14,15,16]
print (set(a) & set(b))