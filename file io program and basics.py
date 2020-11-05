'''
            write data in file
'''

file=open('foo.txt','w')
# file=open('foo.txt','a')  a means append
file.write('hello world\n')
file .close()

print('Data saved successfully')

'''
        modes

        r - read       #default
        w - write
        a - append

            binary files include txt, png, pdf etc file types
            
        rb - read binary
        wb - write binary
'''
