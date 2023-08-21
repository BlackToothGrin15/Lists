x=eval(input("Enter an integer list:"))
l=len(x)

for i in range(l-1):
    for j in range(l-i-1):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
print("The sorted list:",x)

