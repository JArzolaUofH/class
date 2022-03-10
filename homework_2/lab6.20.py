numint = int(input())

if 11 <= numint <= 100:
    while numint % 11 != 0:
        print(numint)
        numint -= 1
    print(numint)
else:
    print("Input has to be in the range of 11-100.")
