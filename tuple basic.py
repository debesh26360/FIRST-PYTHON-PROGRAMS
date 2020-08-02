'Tuple Demo'

#empty tuple
t=()
print(t)

#tuple with values
t=(2,4,0,7,6)
print(t)


#indexing in tuple
print(t[0])

#for loop    #If you want to print all values but don't want to write lot of code
for i in range(0,5):   #i value is not fixed
    print(t[i])

#foreach loop  #only used for collections but not used here #only used when values are already present

for i in t:
    print(i)

#Heterogenous property

t=(1,1.2,'mahesh') #multiple datatypes are stored
print(t[i])

#immutable i.e. cannot be replaced

#t[3]=40
#print(t)

#dynamic i.e can store any amount of data

t1=(1,2,3,4)
t2=(5,6,7)

t3=t1+t2
prin(t3)

#tuple does not allow duplicate values

s={5,321,54,67,,23,86,53,1,8,5,8,5,3,4,6,4}
print(s)           #this will print numbers but not their duplicate values
