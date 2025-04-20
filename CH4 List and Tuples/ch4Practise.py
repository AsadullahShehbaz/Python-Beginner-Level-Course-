t1 = (1,2,3,4,5,1,1,3,2)

print(sum(t1))

print(t1.count(5))

marks = []

for i in range(5):
    while True:
        try:
            mark = int(input("Enter Marks : "))
            marks.append(mark)
            break
        except ValueError:
                print("Invalid Input")
marks.sort()
print(marks)

