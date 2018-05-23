


#f = open('/home/rama/PycharmProjects/file_handling/example_file', 'r')
f = open('/home/rama/PycharmProjects/file_handling/example_file', 'r')
#f.write('This is my third line\n')
x = f.read()
print('x')

#x = f.read(10)
#print x
#f.write('This is first line\n')
#f.write('This is second line\n')
f.close()

print x
