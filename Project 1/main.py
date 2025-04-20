computer = -1

yourChoice = input("Enter your choice : ")

youDictionary = {
    "snake": 1,
    "water":-1,
    "gun":0
}
yourNumber = youDictionary[yourChoice]
if(computer==-1 and yourNumber==-1):
    print("Draw match...")
else:
    print("Not Draw match...")
