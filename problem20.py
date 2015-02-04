a = 100
b = 99
stor = 0
ans = 1
while a > 0:
    stor = a * b
    ans = ans * stor
    a = a - 2
    b = b - 2
ans = sum(map(int, str(ans)))
print(ans)
