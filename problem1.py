three = 0
five = 0
ans = 0 
for i in range(1,1000):
    if i % 3 == 0:
        three = three + i
    else:
        three = three
print(three)

for i in range(1,1000):
    if i % 3 == 0:
        five = five
    elif i % 5 == 0:
        five = five + i
    else:
        five = five
print(five)
sum = three + five
print(sum)
