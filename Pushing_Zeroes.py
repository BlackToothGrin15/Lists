x=eval(input("Enter a list with zeroes as elements:"))
y=[]
z=[]
a=[]
c=0
for i in x:
    if i==0:
        c+=1
    else:
        z.append(i)
for j in range(c):
    z.append(0)

print("Arranged list:",z)
