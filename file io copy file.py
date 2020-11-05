'''
        copy file
'''
file1=open('C:\\Garden Gnome Record.jpg','rb')
file2=open('C:\\Users\i\dbi.0098-LAP-125530.000\\Desktop\\Garden Gnome Record.jpg','wb')

file2.write(file.read())

file2.close()
file1.close()

print('File copied successfully')
