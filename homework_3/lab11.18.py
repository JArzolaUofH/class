# justine arzola 1804667
numbers = input()
allnumbers = [int(x) for x in numbers.split(" ") if int(x) >= 0]
allnumbers.sort()
for x in allnumbers:
    print(x, end=" ")
