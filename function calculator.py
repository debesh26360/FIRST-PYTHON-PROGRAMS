'''
        Calculator
'''

def add(a,b):
    print('addition is',a+b)

def sub(a,b):
    print('subtraction is',a-b)

def div(a,b):
    print('division is',a/b)

def mul(a,b):
    print('multiplication is',a*b)
'''
def choice():
    ch=input('D you want to continue').lower()
    if(ch==' yes'):
        menu()
'''

#recursion technique
def menu():
    x=int(input('Enter 1st number '))
    y=int(input('Enter 2nd number '))

    print('====================MENU=====================')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Division')
    print('4. Multiplication')

    c=int(input('Enter your choice '))

    if(c==1):
        add(x,y)
    elif(c==2):
        sub(x,y)
    elif(c==3):
        div(x,y)
    elif(c==4):
        mul(x,y)
    else:
        print('error')


#def choice():
    ch=input('Do you want to continue').lower()
    if(ch==' yes'):
        menu()
        
#choice()

menu()
        
    


    

