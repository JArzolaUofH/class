both = input().split()
names = both[0]

while names != '-1':
    try:
        age = int(both[1]) + 1
        print("{} {}".format(names, age))
    except:
        print("{} 0".format(names))
    both = input().split()
    names = both[0]
