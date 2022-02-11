# justine arzola 1804667
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

service1 = (input("Select first service:\n"))
service2 = (input("Select second service:\n\n"))

print("Davy's auto shop invoice\n")


cost = {"-": 0, "Oil change": 35, "Tire rotation": 19, "Car wash": 7, "Car wax": 12}
if service1 == "-":
    print("Service 1: No service")
else:
    print("Service 1: {:s}, ${:d}".format(service1, cost.get(service1)))
if service2 == "-":
    print("Service 2: No service")
else:
    print("Service 2: {:s}, ${:d}".format(service2, cost.get(service2)))
total = cost.get(service1) + cost.get(service2)
print("\nTotal: ${:d}".format(total))
