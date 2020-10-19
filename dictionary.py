'''
    Dictionary
'''

#empty dictionary
d={}
print(d)

#dictionary with key, values pairs
products={'p01':'blue polo shirt','p02':'black polo','p03':'duke hat'}  #if you write another value in the same key, the second value will be printed
print(products)

#access values from key
print(products['p01'])


#serch for p003 and replace if found or create new if not found
products['p003']='green polo shirt'
print(products)


#built-in function

print(products.keys())
print(products.values())

print(products.items())     #both keys and values


#iterate over product keys
for key in products.keys():    #key is built in function
    print(key)

#iterate over product values
for value in products.values():
    print(value)

for key,value in products.items():    #item function gives keys and values at the same time #for k in v 
    print(key,value)

#get value of key p01

print()
v=products.get('p01')
print(v)

#return value of key p08 and if not found, print 'not found' message
print()
v=products.get('p09','not found')
print(v)

#delete data from dictionary
del products['p01']
print(products)

#heterogenous

d={1:'one','two':2,3.3:'three'}
print(d)

#store list in dictionary
student={'name':'sunil','id':'s001',',marks':[1,2,3]}
print(student)

