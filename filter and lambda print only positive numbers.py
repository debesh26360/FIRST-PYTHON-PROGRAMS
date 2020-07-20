'''
        Filter function
'''

#normal logic
'''
l1=[1,2,3,4,5,6]

l2=[]

for i in l1:
    if(i1%2==0):
        l2.append(i)

print(l2)
'''

l1=[1,2,3,4,5.6,6,-4,-3,1.4]

l2=[]
'''

def displayint(n):
    return (type(n)==float)


print([i for i in filter(displayint,l1)])
'''
print([i for i in filter(lambda n:type(n)==int,l1)])
