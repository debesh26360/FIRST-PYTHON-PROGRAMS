list1 = [] 
  
num = int(input("Enter number of elements in list: ")) 
  
for i in range(1, num + 1): 
    a= int(input("Enter elements: ")) 
    list1.append(a) 
      
print("Smallest element is:", min(list1)) 
