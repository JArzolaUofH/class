firstnum = int(input())
secnum = int(input())

if (firstnum <= secnum):

    i = firstnum

    while (i <= secnum):
        print(i, end=" ")
        i += 5

    print()

else:
    print("Second integer can't be less than the first.")
