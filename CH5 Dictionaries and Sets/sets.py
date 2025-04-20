s = set()
print(s)

se = {11,12,2,2}
# add method to add elements to the set in python 
se.add(2012)
print(f"The values of se After adding 2012 :  {se}")
# clear method to clear the set and delete all the elements
# se.clear()
print(f"The values of se :  {se}")
# copy method to copy the set values in new set 
see = se.copy()
print(f"The values of see : {see}")

set1 = {2,0,1,2,13}
set2 = {1,1,1,2}

print(f"set1 : {set1.intersection(set2)}")
# print(f"The set 1 - set 2 : {set1.difference_update(set2)}")

# set1.difference_update(set2)
# print(f"The difference update : {set1}")

# set2.discard(2)
# print(f"The values of set2 : {set2}")