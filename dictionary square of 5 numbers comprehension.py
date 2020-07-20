'''
            Create dictionary to store sqaure of first 10 natural numbers

#normal method

d={}

for i in range(1,11):
    d[i]=i**2

print(d)
'''

#comprehension

print({i:i**2 for i in range(1,11)})
