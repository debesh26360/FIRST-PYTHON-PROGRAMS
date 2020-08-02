'''
        SET in tuple
'''

#empty set
s=set()
print(s)


#set with values
s={2,5,1,7,5}
print(s)


#indexing in set is not possible
#print(s[0])
#print(s[1])
#print(s[2])
#print(s[3])
#print(s[4])

#foreach loop is possible

for i in s:
    print(i)

# heterogenous

s={1,1.1,'a'}
print(s)

#set of characters is also ordered
s={'a','a','d', 'e'}
print(s)

#set by itself sorts in ascending value
