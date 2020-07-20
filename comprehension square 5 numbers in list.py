'''
        Comprehension technique
        WAP to create a list of 5 numbers and create square of all numbers


l1=[1,2,3,4,1,5]
l2=[]

for i in l1:
    l2.append(i**2)

print(l2)

'''
#comprehension technique


l1=[1,2,3,4,1,5]
print([i**2 for i in l1])     #in one line, all three things are being done


#takes i value as 1 from l1 and then does the operation i**2.
      #then it takes the next value in the list and then again performs the operation i**2
        #flow: first the for loop is executed, then the i**2 is executed
