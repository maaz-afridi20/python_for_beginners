#repeat something.mulyiple time.
#while loop.

i = 0
while i<10:
    print("yes." + str(i))
    i = i+1 #this will increment i by 1 so the loop will stop after 10executin
'''
j = 1
while j<=50:
    print(j)
    j = j+1
print("rest of the code.")


n = 0
while n<10:
    print("khan")
    n=n+1
'''
#content of a list using while loop.

a = ['maaz',32,'khan,',43,22,'hehe']
k = 0
while k<len(a):
    print(a[k]) #will print the valuse of the list using loop.
    k = k+1



#now printing llist using for looop...
'''here we dont need such type of initioalization like of while loop.
it will thorugh out the value one by one 
'''
fruits = ['banaan','manga','grapes','marshmallo','watermellow']
for item in fruits:
    print(item)


#RANGE FUNCTION.
'''range will only print the value from 0 to that value
which is present in the bracket here is 8 so it will start from 0 to 7
by default it is started from 0 but if we give value then it will start
from that value like, range(2,10) it will start from 2 and end with 9
we can also specify the step size like how many numbers will it 
(chorna) behind for eg. range(1,50,2) it will start from 1 than 2 than 5etc
'''
for i in range(8):
    print(i)

for m in range(1,20,2):
    print(m)


#BREAK STATEMENT.

for n in range(1,10):
    print(n)
    if n==5:
        break  #this will stop the loop on 5 from ongoing to 10

'''
for n in range(1,10):
    print(n)
    if n==5:
        break 
else:
    print("this is out of the loop")

in the loop we also use the else statemnt and this else statement will
run when the loop is complete. so here we have added a break statement
which will breal the loop in the middile or on the specific value so 
this means that the loop didnot executed full. so when the loop is not
executed full then the else part will not print.
this will only print when the loop successfull executed (means that) from
head to bottom.   '''

#CONTINUE STATEMENT.
for v in range(10):
    if v==5:
        continue
    print(v)

''' 
in continue function when the value is going on decently and printing
from 1 to 10 it wll run 1 than 2 ,3,4 and when it come to 5
it will continue direct means that it will not check the conditon
means that it will not going downword it will go direct upword
and will skip 5 in above case.
in this way we can also print even numbers by skipping odd numbers
and vise versa.
'''

# PASS STATEMENT /
''' is ka matlab hai k fil hal is ko chor do abi ye khaali hai..
iss k neechay wla statement print kro.like

i = 10
for i>0:
    pass
agar hm waiasy ye chor dy to error aye ga. but agr pass likh dei
tu ye samj jaye ga k fill hal chor do

print("hi")
'''