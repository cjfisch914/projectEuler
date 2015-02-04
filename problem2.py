num0 = 1
num1 = 2
ans = 0
while num0 <= 4000000:
    sum = num0 + num1 #add the numbers
    num0 = num1 #reassign the first num as the second 
    num1 = sum #reassign the second num as the sum
    if sum % 2 == 0:
        ans = ans + sum
    else:
        ans = ans
ans = ans + 2
print(ans)
