gen = (input("Enter you are male or female :"))
sal = int(input("Enter your salary :"))
if (gen == 'male' and sal < 1000):
    bonus = (sal + (sal * (5 / 100)))
    print("you get a bonus 5%", bonus)
elif(gen == 'female' and sal < 1000):
    bonus = (sal + (sal * (5.5 / 100)))
    print("you get a bonus 5.5%", bonus)
elif(sal > 1000):
    bonus = (sal + (sal * (5 / 100)))
    print("you get bonus 5%", bonus)
