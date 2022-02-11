# justine arzola 1804667

l_juice = (int(input("Enter amount of lemon juice (in cups):\n")))
water = (int(input("Enter amount of water (in cups):\n")))
agave = (float(input("Enter amount of agave nectar (in cups):\n")))
servings = (float(input("How many servings does this make?\n\n")))
print("Lemonade ingredients - yields", '{:.2f}'.format(servings), "servings")
print('{:.2f}'.format(l_juice), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave), "cup(s) agave nectar\n")
newserv = (int(input("How many servings would you like to make?\n\n")))
l_juice1 = l_juice/servings
water1 = water/servings
agave1 =agave/servings

newl_juice =l_juice1*newserv
new_water = water1*newserv
new_agave = agave1*newserv


print("Lemonade ingredients - yields", '{:.2f}'.format(newserv), "servings")
print('{:.2f}'.format(newl_juice), "cup(s) lemon juice")
print('{:.2f}'.format(new_water), "cup(s) water")
print('{:.2f}'.format(new_agave), "cup(s) agave nectar\n")

newl_juiceg = newl_juice/16
new_waterg = new_water/16
new_agaveg = new_agave/16

print("Lemonade ingredients - yields", '{:.2f}'.format(newserv), "servings")
print('{:.2f}'.format(newl_juiceg), "gallon(s) lemon juice")
print('{:.2f}'.format(new_waterg), "gallon(s) water")
print('{:.2f}'.format(new_agaveg), "gallon(s) agave nectar")

