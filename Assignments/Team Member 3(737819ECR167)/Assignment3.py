import random
l=[]
a=int(input("Enter the no.of inputs: "))
for i in range(0,a):
    e=int(input())
    l.append(e)
print(l)
temp=random.choice(l)
hum=random.choice(l)
print(temp,hum)
if temp>100:
    if hum>80:
        print("MOST DANGEROUS")
    else:
        print("HIGH TEMPERATURE")
elif temp==100:
    print("Care needed !! no risk")
else:
    print("All good")
