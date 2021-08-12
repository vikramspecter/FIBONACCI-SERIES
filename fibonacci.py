a=[0,1]
b=int(input("enter number upto which you want the fibonnaci series"))
for i in range(0,b):
    if(i==a[-1]+a[-2]):
        a.append(i)
print(a)
