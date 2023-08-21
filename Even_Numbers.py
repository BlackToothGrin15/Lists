x=eval(input("Enter an integer list:"))
y=[]

for i in x:
    if i%2==0:
        y.append(i)
print("The even integers are:",y)
