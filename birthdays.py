birthdays = {'Alif': 'Nov 30' , 'Futu' : 'June 07'}

while True:
    print('Input the name. For exit keep it blank')
    name = input()
    if name == '' :
        break
    if name in birthdays :
        print(birthdays[name])
    else :
        print('No entry found. Enter the birthday for this name')
        bday = input()
        birthdays[name] = bday
        print('Database updated')
exit()
