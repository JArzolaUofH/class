# Justine Arzola 1804667
import csv

file = input()
f = open(file)
info = csv.reader(f, delimiter=',')
contents = []
for row in info:
    for content in row:
        contents.append(content.strip())

for i in range(len(contents)):
    if contents[i] not in contents[:i]:
        count = 0
        for c in contents:
            if contents[i] == c:
                count += 1
        print(contents[i], count)
f.close()
