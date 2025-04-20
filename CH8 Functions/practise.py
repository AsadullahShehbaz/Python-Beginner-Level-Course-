a = 11
b = 12
c = 20
d = 13

# print(a)
# print(b)
# print(c,end="")
# print(d)

def sumAll(n):
    if (n==1):
        return 1
    return n + sumAll(n-1)
# print(sumAll(6))
names = ["Ahmed","Qasim","Faheem","Usama","an","Qonan","Ahsan"]
def remove(word):
    return names.remove(word)
print("Qasim")

def rem (word):
    n = []
    for item in names:
        if not(item == word):
            n.append(item.strip(word))
    return n

print(rem("an"))