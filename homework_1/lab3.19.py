# justine arzola 1804667

height = (int(input("Enter wall height (feet):\n")))
width = (int(input("Enter wall width (feet):\n")))

area = height * width
print("Wall area:", area, "square feet")

gallon = 350
gallons = area/gallon
print("Paint needed:", '{:.2f}'.format(gallons), "gallons")

print("Cans needed:", round(gallons), "can(s)\n")

color = (input("Choose a color to paint the wall:\n"))

options = {"red": 35,
           "blue": 25,
           "green": 23}
print("Cost of purchasing {} paint: ${}".format(color, (options[color]) * round(gallons)))
