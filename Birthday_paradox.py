from math import *
from decimal import *

n=365
k=0
a=[]

for i in range(1,365):
    if n==365:
        a.append(n)
    if n>0:
        n=n-1
    a.append(n)
value=prod(a)
print('Value: ', value/(365**2))
# while True:
#     k+=1
#     # result = Decimal(value)/Decimal((365 ** k))
#     result = value/(365 ** k) 
#     if k==23:
#         break
print(f"""
k:\n{k}
Days:\n{a}
Dot:\n{value}

""")



