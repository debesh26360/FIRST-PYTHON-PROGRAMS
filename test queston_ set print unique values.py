'''
WAP to print unique values
'''

#do not print duplicate numbers

s=set()
print('Enter ten numbers')

for i in range(10):
    s.add(int(input()))
    print(s)
