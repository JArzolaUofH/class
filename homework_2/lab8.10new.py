# Justine Arzola 1804667

newinput = input()

newinput = newinput.lower()

newinput = newinput.replace(" ", "")

low = 0
high = len(newinput) - 1
result = True

while low < high:

    if newinput[low] != newinput[high]:
        result = False

    low += 1

    high -= 1

if result:
    print(newinput, "is a palindrome")

else:
    print(newinput, "is not a palindrome")
