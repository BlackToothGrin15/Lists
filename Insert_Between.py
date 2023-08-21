x=eval(input("Enter a sorted list:"))
l=len(x)
save=0
n=int(input("Enter the number to be inserted:"))

for i in range(l):
    if x[i]>n:
        for j in range(i,l):
            save=x[j]
            x[j]=n
            n=save
        break
x.append(save)
print("New list:",x)
