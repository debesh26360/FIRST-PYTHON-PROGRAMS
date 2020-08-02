a={1,2,3}
b={4,5,3}

print(a-b)            #difference what is in a and not in b i.e 1,2
print(a.difference(b))

print(a|b)                              #1,2,3,4,5
print(a.union(b))                   #1,2,3,4,5


print(a&b)                  #intersection i.e common
print(a.intersection(b))


print(a^b)
print(a._xor_(b))       #not commom in a and b
