# Justine Arzola 1804667
playdict = {}

for i in range(1, 6):

    print("Enter player "+str(i)+"'s jersey number:")

    key = int(input())

    print("Enter player "+str(i)+"'s rating:\n")

    value = int(input())

    playdict[key] = value

print("ROSTER")

for i in sorted(playdict):

    print("Jersey number: "+str(i)+", Rating: "+str(playdict[i]))

while(1):
    print("\nMENU")

    print("a - Add player")

    print("d - Remove player")

    print("u - Update player rating")

    print("r - Output players above a rating")

    print("o - Output roster")

    print("q - Quit\n")

    print("Choose an option:")

    n = input()

    if(n=="o"):

        print("ROSTER")

        for i in sorted(playdict):

            print("Jersey number: "+str(i)+", Rating: "+str(playdict[i]))

    elif(n=="a"):

        print("Enter a new player's jersey number:")

        key = int(input())

        print("Enter the player's rating:")

        value = int(input())

        playdict[key] = value

    elif(n=="d"):

        print("Enter a jersey number:")

        key=int(input())

        playdict.pop(key)

    elif(n=="u"):

        print("Enter a jersey number:")

        key = int(input())

        print("Enter a new rating for player:")

        value = int(input())

        playdict[key] = value

    elif(n=="r"):

        print("Enter a rating:")

        rating = int(input())

        print("Above "+str(rating))

        for i in sorted(playdict.items(), key=lambda x:x[1], reverse=True):

            if i[1]>rating:

                print("Jersey number: "+str(i[0])+", Rating: "+str(i[1]))

    else:

        exit(0)
