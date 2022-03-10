textline = input()


while textline != "done" and textline != "d" and textline != "Done":

    for i in range(len(textline) - 1, -1, -1):

         print(textline[i], end="")

    print()
    textline = input()
