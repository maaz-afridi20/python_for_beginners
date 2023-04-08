print("dictionary introduction and practice")
thisdict = {"Name": "Ford", "Electric": False, "Model": 1990, "Colors": ['Red', 'Blue', 'green']}
print(thisdict["Electric"])
# print(thisdict.get("Electric")) another method to out the same result as above
print(type(thisdict))

# print(thisdict.keys()) will give all the names of keys in dictionary

thisdict['Colors'] = 'White'  # will add white to the colors
thisdict['Electric'] = True
print(thisdict.keys()) # will give only the keys
print(thisdict.values())  # will give only values
print(thisdict)

print("Items")
print(thisdict.items())   # will return all the values in type of tuple.

if("Name" in thisdict):
    print("yes this is present.")
else:
    print("not present.!")

thisdict.update({"Year": "2020"})  # will update full another key values pair in present dictionary.
print(thisdict.items())

# thisdict.pop("Year")  # will remove the specific key.

thisdict.popitem()  # will remove full item form the dictionary. the last one item.
print(thisdict.keys())

# thisdict.clear()  # will clear the whole dictionary
# print(thisdict)