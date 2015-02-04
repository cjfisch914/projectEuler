num = 600851475143
for i in range(1,10000):
    if num % i == 0:
        stor1 = i #finds factors of num
        for x in range(1,stor1):
            if stor1 % x != 0 and stor1/stor1 == 1:
                stor2=stor1