num = 1 
var = 1
while var < 20:
    if num % var == 0:
        var = var + 1
    else:
        var = 1
        num = num + 1
print(num)