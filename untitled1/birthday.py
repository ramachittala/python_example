

birthday = {'Ram:' 'DEC 19', 'Swathi:' 'Jun 02'}

while True:
    print ("Enter the name: (blank to quit)")
    name = input()
    if name =='':
        break 

    if name in birthday:
        print(birthday[name] + ' is the birday of' + name )
    else:
        print("i don't have the information for" + name)
        print("what is your birthday")
        bday = input()
        birthday[name] = bday
        print("birthday database has been updated")
