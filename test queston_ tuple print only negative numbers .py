'''
WAP to accept 10 numbers and create tuple of negative numbers
'''
# to store only negative numbers
t=()
print('Enter 10 numbers')
for i in range(10):
    n=int(input())
    if(n<0):
        t=t+(n,)

print(t)

#OR

t=()
print('Enter 10 numbers')
for i in range(10):
    t=t+(int(input()),)

for i in t:
    if(i<0):
        print(i)
