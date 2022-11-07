a = "hello"
# Use the built-in function set() to convert the string to a set
print(set(a))
#{'h', 'l', 'o', 'e'}
b = set([1, 1, 2, 2, 3, 3, 4, 4])
print(b)
#{1, 2, 3, 4}
b.add(5)
print(b)
#{1, 2, 3, 4, 5}
b.update(['a', 'a', 'b', 'b'])
print(b)
#{1, 2, 3, 4, 5, 'b', 'a'}
a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])
print(a.intersection(b))
#{4, 5}
print(a.union(b))
#{1, 2, 3, 4, 5, 6, 7, 8}
#print(1 *)     ??????????????
#{1, 2, 3}
