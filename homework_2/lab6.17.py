userpassword = input("please enter password:")
result = ''

i = 0
while i < len(userpassword):
    new = userpassword[i]
    if new == 'i':
        result += '!'
    elif new == 'a':
        result += '@'
    elif new == 'm':
        result += 'M'
    elif new == 'B':
        result += '8'
    elif new == 'o':
        result += '.'
    else:
        result += new
    i += 1

result += "q*s"
print(result)
