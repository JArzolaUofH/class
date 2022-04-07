# Justine Arzola 1804667
words = input().split()

for word in words:
    count = 0
    for item in words:
        if word == item:
            count += 1
    print(word, count)
