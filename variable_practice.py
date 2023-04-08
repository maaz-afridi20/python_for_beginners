print("this is variable practice")

# this is the way to assigning multiple values.

x, y, z = 'orange', 'yellow', 'black'
print(x)
print(y)
print(z)

# way for making one value to different variables.
a = b = c = "myClass"
print(a)
print(b)
print(c)

fruits = ["apple", "banana", "mango", "waterMelon"]
q = w = e = fruits
print(q)
print(w)
print(e)

# below is function.!
x = "awesome"
def myfunc():
    print("python is " + x)

myfunc()

def anFunc():
    global p
    p = "excellent"

anFunc()
print("python is "+ p)