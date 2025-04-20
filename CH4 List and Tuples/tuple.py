t1 = (1,2,3,4,5)
t2 = (9,2,3,4)
t3 = t1 + t2 # it will concatenate the tuples to make new tuple 
print(f"The Concatenated Tuple 3 : {t3}")

repeated = t1 * 3 # it will repeat the tuple 3 times 
print(f"The Repeated Tuple 1 : {repeated}")

print(f"Is 2 Exists in the Tuple 1 : {2 in t1}")

t4 = t1[1:3]
print(f"The Sliced Tuple 4 : {t4}")

a,b = t4
print(f"a : {a} , b : {b}")