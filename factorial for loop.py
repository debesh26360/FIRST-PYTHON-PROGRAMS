'''

            Factorial of 5 i.e 5!    #refer to notes

'''

fact=1
for i in range(1,6):
    fact=fact*i            # i is increment

print('Factorial is',fact)

'''

# recursion mode


def factorial(n):
    if(n==1):
        return 1    
    else:
        return n*factorial(n-1)

print(factorial(4))

'''
