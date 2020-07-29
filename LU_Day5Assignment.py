#1 List1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]. Sort the list in increasing order but all zeroes should be on right hand side
list1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]

list1.sort()
countofZero=0
for i in range(len(list1)):
    if list1[i]==0:
        countofZero=countofZero+1
    k=0
while k<countofZero:
    list1.remove(0)
    k=k+1
    list1.append(0)

print(list1)

#2 List1=[10,20,40,60,70,80],List2=[5,15,25,35,45,60],merge the sorted lists and produce a single sorted list but use only 1 while or for loop,without using sort()

list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
list3=list1+list2
list3.sort()
print(list3)