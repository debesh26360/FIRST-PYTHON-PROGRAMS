s=set()
print('Enter 10 numbers')
for i in range(10):
    s.add(int(input()),)

t=tuple(s)  #converts to tuple
print(t[1])

# to find smallest number


t=()
print('Enter 10 numbers')
for i in range(10):
    t=t+(int(input()),)


smallest=t[0]                   #took first tuple value as smallest
for i in range(10):
    if(i<smallest):
        smallest=i                     #here you switched the first 'smallest' number wil the smaller vaulue and to keep searching.
                                             #in the last, you arrive at the smallest value
        
print(smallest)
