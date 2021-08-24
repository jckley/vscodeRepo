print("--------------------TUPLE to DICT-----------------------")
tup = ((11, "eleven"), (21, "mike"), (19, "dustin"), (46, "caleb"))
print(tup)
dct = dict(map(reversed, tup))
print(dct)

print("--------------------LIST to DICT-----------------------")
list1 = [("helen", 60), ("mark", "young"), ("pip", 11)]
print(list1)
dct1 = dict(map(lambda a: a, list1))
print(dct1)
