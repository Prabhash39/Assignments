# a = [1,2,3,4]
# a.append(5)
# print(a)


# a = [1,2,3,4]
# new_numbers = [10,11,12,13]
# a.extend(new_numbers)
# print(a)

# a.insert(c,'ram')
# print(a)
# a.remove(4)
# print(a)
# b = a.pop
# print(a,b)
# c = a.copy
# a.clear()
# print(a)
# print(C)


# a = (1,2,3,'ram',4)
# a = list(a)
# a.pop(3)
# a.insert(0,'ram')
# print(a)

# a = {1,2,3,4}
# a.add(8)
# a.update(a)
# print(a)

# a = {1,2,3,4}
# a.remove(2)
# a.discard(4)
# a.pop()
# print(a)

# a = {1,'ram',8.2,'shyam'}
# a.pop()
# print(a)

a ={1,2,3,4}
b ={2,3,4,8}
# c =a.union(b)
# print(c)

# d = a.intersection(b)
# print(d)

# c = a.issubset(b)
# print(c)

# c = a.isdisjoint(b)
# print(c)

# c = a.issuperset(b)
# print(c)

a = {'ram': 1,'shyam' : 2}
a [ 'Hari'] = 4
print(a)
b = a.pop('shyam')
print(b)
print(a)
a.popitem()
print(a)
a['Rabi'] = 2
print(a)
b = a.get('hari', 'dont exist')
print(b)

a = {'ram': 1, 'hari': 2}
for i in a.keys():
    print(i)
for i in a.items():
    print(i)

for i in a.values():
    print(i)


a = {'ram':1}
a.pop('ram')
a['RAM'] = 1
print(a)


a = {'ram': 1}
a.pop('RAM') =a.pop{'ram'}


