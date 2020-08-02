'''
    WAPto accept 5 name and store in tuple 
'''


t=()

print('Enter 5 names')
for i in range(5):
    t=t+(input(),)  #1st interation has empty value    #()+(Debesh,) this is addition of tuple
                                    #the tuple changes from empty to full
                                    #(Debesh,) represents a tuple

print(t)    
