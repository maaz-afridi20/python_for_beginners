'''
for x in 'banana':
    print(x)
'''

'''
fruits = ['appol', 'banana', 'mango']
for items in fruits:
    print(items)
    if(items=='banana'):
        break

'''

'''
fruits = ['appol', 'banana', 'mango']
for items in fruits:
    if(items=='banana'):
        break
    print(items)
'''

'''
# continue statement.
fruits = ['appol', 'banana', 'mango']
for items in fruits:
    if(items=='banana'):
        continue
    print(items)
'''

'''
# range functions
for i in range(0, 33, 3):
    print(i)
'''

'''
for x in range(6):
    print(x)
else:
    print('loop has ended.')
'''

'''
# the else part will not be execute if we end the loop by break statement.

for i in range(10):
    if i==5:
        break
    print(i)
else:
    print('finally')
'''

'''
# nested loops

adj = ['red', 'green', 'blue']
fruits = ['appol', 'banana', 'mango']

for x in adj:
    for y in fruits:
        print(x, y)
'''
