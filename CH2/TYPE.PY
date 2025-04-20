while (True):
    x = int (input("Enter the Dividend :"))
    z= int (input("Enter the Divisor "))

    if (z==0):
        print("Divide by zero is not good")
    else:
        print(f"This is the remainder { x % z}")