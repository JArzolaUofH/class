inputValue = input()

inputValue = inputValue.lower()

inputValue = inputValue.replace(" ", "")

low = 0
high = len(inputValue) - 1
result = True

while(low<high):

    if(inputValue[low]!=inputValue[high]):
        result = False

    low+=1

    high-=1

if result:
    print(inputValue, "is a palindrome")

else:
    print(inputValue, "is not a palindrome")
