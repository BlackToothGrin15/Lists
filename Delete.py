x=eval(input("Enter an integer list:"))

n=int(input("Enter the number you want to delete:"))
for i in x:
    if i==n:
        x.remove(i)
print("New list:",x)
