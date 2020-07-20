'''
        Map Function
'''



#without Map

l1=[1,2,3]
l2=[4,5,6]

# I want to obtain l3=[5,7,9]


#normal logic              zip will take first value from l1 and first value from l2

'''
for i,j in zip(l1,l2):        #here zip adds the index values                          
    l3.append(i+j)

print(l3)
'''

def sum(a,b):
    return a+b

print([i for i in map(sum,l1,l2)])   #comprehension in map

# using lambda

print([i for i in map(lambda a,b:a+b,l1,l2)])


#Process for map
'''

passes first bvalue of l1 and ass to function i.e sum
take first value from l2
we got 4 value and store in list
map will pass second of l1 to l2 and add to function i.e sum
then it adds the second value taken from l1 and adds to the second value in l2 and stores in list
the same process for third value of l1 and l2
'''
