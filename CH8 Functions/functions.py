def average():
    a =int(input ("Enter Number 1 : "))
    b =int(input("Enter Number 2 : "))
    c =int(input("Enter Number 3 : "))
    avg = (a+b+c)/3
    print(f"Average : {avg}")
# average()

def Salam (name="Ahmed"):
    print(f"Assalam O Alaikum {name}")
Salam()
# name = input("Enter your Name : ")
# Salam(name)

def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))