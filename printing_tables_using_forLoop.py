'''
print('this is table')

nmbr = int(input('Enter a number to make a table.!'))

for x in range(1,11):
    print(f"{nmbr} X {x} = {nmbr*x} ")

print('this is table.!')
'''

list = ['harry', 'rahul', 'keymon', 'dude']
for n in list:
    if n.startswith('k'):
        print(f'hello {n} dude.')