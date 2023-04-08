# function practice
# below is also one of another method key word arguments

'''
def practice(child1, child2, child3):
    print('the youngest child is ' + child3)

practice(child1='khan,', child2='ali ', child3='tareen')

'''

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
