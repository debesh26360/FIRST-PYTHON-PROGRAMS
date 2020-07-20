l1=[1,2,3,4,5,6]
'''
l2=[]

def even(n):
    return n%2==1


print([i for i in filter(even,l1)])
'''
print([i for i in filter(lambda n:n%2!=0,l1)])
