planet = ['mercury', 'venue', 'earth', 'mars',
          'jupiter', 'saturn', 'uranus', 'naptune', 'pluto']
planet_name = input("Enter the planet name :")
if planet_name in planet[0:2]:
    print("Its inner planet")
elif planet_name in planet[2]:
    print("you are on earth")
elif planet_name in planet[3:8]:
    print("Its outer planet")
elif planet_name in planet[8]:
    print("pluto is dwarf planet")
else:
    print("Entered some other name...try again ")
