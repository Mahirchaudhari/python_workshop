x = 10
to_guess = True
while to_guess:
	guess = int(input("enter number:"))
	if guess == x:
		print("equal")
		to_guess == False
	elif guess > x:
		print("greater")
	else:
		print("less than")
