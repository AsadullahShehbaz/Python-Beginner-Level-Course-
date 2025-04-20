# name = input("Enter your name :")
# print(f"Welcome Sir {name}")

# age = input("Enter your age :")
# print(f"You are {age} years old")

letter = '''
    Dear <|name|>,
    You are  selected !
    <|age|> 
    '''
print(letter.replace("<|name|>","Abdul Hameed ").replace("<|age|> ","22"))
print(letter.replace("  "," "))


