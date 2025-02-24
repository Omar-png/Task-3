#Task: Filter and Transform a list
num = 1
numbers = []

while num <= 20:
    numbers.append(num)
    num += 1

newlist = []
for i in numbers:
    if i % 3 == 0:
        newlist.append(i)

print (newlist)