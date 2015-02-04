sOS = 0 #sum of the squares
sOTS = 0 #square of the sum
stor1 = 0 
stor2 = 0
for i in range(1,101):
    sOS = i ** 2
    stor1 = stor1 + sOS
print(stor1)
for i in range(1,101):
    stor2 = stor2 + i
stor2 = stor2 ** 2
print(stor2)
ans = stor2 - stor1
print(ans)