list1 = [9,3,-7,-2,5,-7]
# lambda exp.
no = list(filter(lambda x: (x < 0), list1))
print("Negative numbers in the list: ", no)
