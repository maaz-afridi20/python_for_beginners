print("dictionary using loops")
# mydict = {'name': 'maaz', 'class': 'university', 'year': '2020', 'uni': 'kust'}

 #for x in mydict:  # only show keys
  #  print(x)

# for y in mydict:  # shows values.
  #   print(mydict[y])

# for x in mydict.keys(): show keys one by one.
  #   print(x)

# for x in mydict.values(): shows values of keys. one by one.
 #    print(x)

# for x, y in mydict.items():  shows keys as well as values.
#     print(x, y)


print('dictionary with in the dictionary.!')

mydict = {'name': 'maaz', 'class': 'university', 'year': '2020', 'uni': 'kust', 'anotherDict': {'i am 2nd dict'} }
print(mydict['anotherDict'])
