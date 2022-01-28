lst1=[1,2,3,4,5,6,7]
lst2=[2,8,9,6,2,3,4,7,8,0,5]
print(lst1,lst2)
if sum(lst1)==sum(lst2):
    print("sum is same")
else:
    print("sum is not same")
print("sum is list1 {0} and sum of list 2 is{1}".format(sum(lst1),sum(lst2)))