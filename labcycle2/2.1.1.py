list=[]
a=int(input("enter the limit"))
for i in range(a):
    b=int(input("enter the value"))
    list.append(b)

print(list)
for i in list:
    print(i*i)