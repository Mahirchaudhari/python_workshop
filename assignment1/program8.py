x = "python is a wonderful programing language."
print(len(x))
i = 0
while (i<len(x)):
	if x[i]=='s':
		print(i)
		break
	i+=1