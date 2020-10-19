'''
        LIST
'''
#list is ordered, heterogenous, mutable,dynamic

#empty list
l=[]
print(l)

#list with values
l=[2,4,7,2,5,8,9]
print(l)

#indexing in list
print()
print(l[0])
l=[1]
l=[2]
l=[3]
l=[4]
l=[5]
print(l[6])

#for loop

print()
for i in range(0,4):
    print(l[i])

#foreach loop
print()
for i in l:
    print (i)

l=[1,1.0,'asd']
print(l)

#mutable
l[0]=1  #changed the index value from 2 to 1
print(l)

#built in functions
l.reverse()
print(l)

l.sort()
print(l)

#covert to set
t=set(l)

#convert to tuple
a=tuple(l)


#append and extend function
#extend only list can be inserted
#apeend value and list both can be added

l1=[1,2,3]
l2=[5,6]

l1.append(l2)  #add l2 into l1 list
print(l1)

l1.extend(l2)
prine(l1)

#slicing like sublist

l2=[1,145,24,38,4,5]
print(l2[1])
print(l1[1:3])   #3 is the stop value. It will not be included
print(l2[1:5:2])        #2 is the step value i.e n intervals of 2
print(l1[-1])    #index starts with -1 directly from right
print(l2[1:-1:-4])  #slicing from right
print(l2[-1:-4:-2])  #-2 is the step value
print(l2[1:-1:])     #automatically starts from -1 to the last, when the length of list is unknown



l3=[1,2,3,[4,5,6],9]
print(l1[3])
print(l1[3][1])  #3 is the entire list, 1 is the index in the list

for i in l3:
    if(i>3):
        l1.remove(i)

        
l1=[1,2,3]
l1.remove(3)          #remove by value
print(l1)

del l3[0]          #remove by index
print(l1)


l1.pop()            #remove or pop out a value

l3,pop(2)
print(l3)


temp=l3.pop(0)
print(temp)
print(l3)
