x=eval(input("Enter an integer list:"))
l=len(x)

for i in range(1,l):
    key=x[i]
    j=i-1
    while j>=0 and key<x[j]:
        x[j+1]=x[j]
        j-=1
    x[j+1]=key
print("The sorted list:",x)

