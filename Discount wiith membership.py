membership=input('type yes or no for membership ')

if membership in ['y','Y','yes','YES']:
    
    total_cost = int(input('Please enter a total_cost:'))
    if total_cost>=1000:    

        print('You have won a discount by 15 percent')
        total_cost *= 0.85
    
    elif total_cost<1000:

        print("You have won a discount by 5 percent")
        total_cost *= 0.95
               
    print ('Now the total cost is ', total_cost)

elif membership in ['n','no','N','No']:

    total_cost = int(input('Please enter a total_cost:'))
    if total_cost>=1000:    

        print('You have won a discount by 5 percent')
        total_cost *= 0.85
    
    elif total_cost<1000:

        print("No discount")
        total_cost *= 1
               
    print ('Now the total cost is ', total_cost)



