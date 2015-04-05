x = int(input("enter number :"))
for i in range(2,int(x/2)):
    if x % i == 0:
        print("this is not prime number ")
    else:
        print("prime number ") 