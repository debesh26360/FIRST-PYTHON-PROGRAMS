'''
        Lambda  -  inline function  i.e replacement of function

'''
'''
def square():
    if(n>0):
        return n**2
    else:
        return 'Enter number>0'
'''

square=lambda n:n**2 if(n>0) else 'Enter number>0'

print(square(5))


#Reduce number of lines only for function

'''
num = int(input("enter a number: "))
 
fac = 1
 
for i in range(1, num + 1):
	fac = fac * i
 
print("factorial of ", num, " is ", fac)
'''
