x=eval(input("Enter a list:"))
mn=x[0]
for i in x:
    if i<mn:
        mn=i
print("Smallest:",mn)
