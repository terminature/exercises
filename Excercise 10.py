from random import sample

a = sample(range(1,100),15)
b = sample(range(1,100),20)


similar_numbers = [x for x in set(b) if x in set(a)]

print (similar_numbers)