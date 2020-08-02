'''
WAP in tuple to accept 5 numbers from user and store in tuple and print only even numbers
'''
t=()
print('Enter 5 numbers')
for i in range(5):
    t=t+(int(input()),)
    
for i in t:
    if(i%2==0):
        print(i)
