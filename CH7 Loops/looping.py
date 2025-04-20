n = int(input("Enter number : "))
# for i in range(2,num):
#     if(num%i==0):
#         print("Not Prime")
#         break
# else:
#     print("Prime")
#-------------------------------------Q6--------------------------------------
# factorial = 1
# while(num>0):
#     factorial = factorial * num
#     num= num-1
# print(factorial)   
# -------------------------------------Q7--------------------------------------

for i in range (1,n+1):
    print(" "*(n-i),end="")
    print ("*"*(2*i-1))
#--------------------------------------Q8---------------------------------------
for i in range(1,n+1):
    print(f"{i}"*i)