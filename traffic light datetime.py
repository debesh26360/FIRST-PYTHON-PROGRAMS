import time
import datetime.datetime

hour=print(datetime.now().hour)    

def countdown(n):
    for i in range(n,0,-1):  
        print(i)
        time.sleep(1)           #starts from 10 then 10-1 i.e 9, then 8, then 7....



def trafficlight():

    color='red'
    if(hour>=0 and hour<7):

        if(color=='yellow'):
            print('color is yellow. slow')
            color='red'
            countdown(5)

       else:

            if(color=='red'):
                print('color is red. stop')
                color='green'
                countdown(10)
         
            if(color=='green'):
                print('color is green. continue')
                color='yellow'
                countdown(10)

            
            if(color=='yellow'):
                print('color is yellow. slow')
                color='red'
                countdown(5)

    trafficlight()# this is part of the function

#trafficlight()  #function starts from here




