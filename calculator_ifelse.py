choice = input("enter choice(+/-/*//): ")
x = int(input("enter first number: "))
y = int(input("enter second number: "))

if choice == '+':
	print("ans is ",x+y)
elif choice == '-':
	print("ans is ",x-y)
elif choice == '*':
	print("ans is ",x*y)
elif choice == '/':
	print("ans is ",x/y)
else:
	print("invalid input")