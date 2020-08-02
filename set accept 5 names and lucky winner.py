'''
        WAP to accept 5 names and store in set and random lucky winner
'''


s=set()
print('Enter 5 names')
for i in range(5):
    s.add(input())

for i in s:
    print(i,' is the random lucky winner')
    break
