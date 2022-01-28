list1=[2,5,7,8,9,1,2,60,70,20]
list2=[5,8,9,1,2,3,674,7,8,0,200]
print(list1,list2)
list=[]
for i in list1:
    if i in list2:
        list.append(i)
print("value occurance in both list is:\t",list)