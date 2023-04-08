import random
print(random.randrange(1, 100,)) # will create any random number.

for x in "banana": # accessing characters through for loop.!
    print(x)

txt = "The best things in life are free!"
print("free" in txt) # this will check weather the free is present or not.

text = "This is one of the main function"
if("z" in text):
    print("yes this is present")
else:
    print('this is not present.!')

free = "this is most expensive.!"
if("z" not in free):
    print("yes this word is not present.")
else:
    print("this word is present.")

b = 'hello world'
print(b[-5:])