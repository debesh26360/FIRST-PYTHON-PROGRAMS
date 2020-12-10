membership=input('type yes or no for membership ')

if membership in ['y','Y','yes','YES']:
    
    cost = int(input('Please enter a cost:'))
    if cost>=1000:    

        print('You have won a discount by 15 percent')
        cost *= 0.85
    
    elif cost<1000:

        print("You have won a discount by 5 percent")
        cost *= 0.95
               
    print ('Now the total cost is ', cost)

elif membership in ['n','no','N','No']:

    cost = int(input('Please enter a total_cost:'))
    if cost>=1000:    

        print('You have won a discount by 5 percent')
        cost *= 0.85
    
    elif cost<1000:

        print("No discount")
        cost *= 1
               
    print ('Now the total cost is ', cost)



