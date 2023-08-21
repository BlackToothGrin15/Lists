x=eval(input("Enter an integer list:"))

print("Prime numbers are:")
for i in x:
    f=0
    for j in range(1,i+1):
        if i%j==0:
            f+=1
    if f==2:
        print(i)
