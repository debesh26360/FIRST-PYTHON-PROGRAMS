'''
        UDF- User defined Functions
'''

'''
        print()
        int()                            #built in function
        input()


                #Logic Separation

def add():

            #addition logic

def sub():

            #sub logic

def mul():

            #mul logic
    
def div():

            #div logic
'''

def myfunction():
    print('this is my function')

#call a function
myfunction()   #the print line comes to this line without indentation


#parameterized function

def square(n):
    print('square is',n**2)

def cube(n):
    print('cube is',n**3)
    
square(5)
square(6)   
cube(5)
cube(6)


def square(n):
    return n**2     #25 is returned to the the line from where it took the value 5
        #print('square is',n**2)

def cube(n):
    return n**3
    #print('cube is',n**3)

ans1=square(5)    #5 goes to the 1st return line
ans2=cube(ans1)

print(ans2)
