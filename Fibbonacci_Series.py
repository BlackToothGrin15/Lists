n=int(input("Enter no. of terms:"))
x=[]

first=0
second=1
third=0

x.append(first)
x.append(second)

for i in range(n-2):
    third=first+second
    x.append(third)
    first=second
    second=third

print("Fibbonacci series:\n",x)
