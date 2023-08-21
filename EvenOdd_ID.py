x=eval(input("Enter an integer list:"))
l=len(x)
for i in range(l):
    if x[i]%2==0:
        x[i]+=3
    else:
        x[i]-=3
print("New list:",x)
