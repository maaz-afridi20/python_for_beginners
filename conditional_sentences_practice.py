names = ['maaz', 'payman', 'khan', 'ali']
name = input('Enter your name \n')
print('you entered name is ' + name+ '\n')

if(name in names):
    print('your name is present')
else:
    print('your name is not present.')