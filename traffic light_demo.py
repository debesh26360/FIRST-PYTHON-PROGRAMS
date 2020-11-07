import time
from datetime import datetime

hour=datetime.now().hour


def countdown(n):
    for i in range(n,0,-1):
        print(i)
        time.sleep(1)
        

def trafficlight():


    if(hour>=0 and hour<7):
        
        print("Continue driving")
        for i in range(1,0,-1):
            time.sleep(1)
            
    else:
        
        color="red"
        
        if(color=="red"):
            print("Color is red. Please stop!!!")
            color="green"
            countdown(10)
    
        if(color=="green"):
            print("Color is green. Continue driving")
            countdown(10)
            color="yellow"
        
        if(color=="yellow"):
            print("Color is yellow. Slow down and stop!!!")
            countdown(5)
        

    trafficlight()




trafficlight()


        
    
