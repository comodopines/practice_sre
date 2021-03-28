#Create a dictionary
d1 = {'a':5, 'b':4, 'e':1, 'd':2, 'c':3}

#Print dictionary sorted by keys
for item in sorted(d1.items()):
  print(item)

'''
('a', 5)
('b', 4)
('c', 3)
('d', 2)
('e', 1)
'''


#print dictionary sorted by keys method 2 (my preference)
for item in sorted(d1.items(), key=lambda kv:kv[0]):
  print(item)

'''
('a', 5)
('b', 4)
('c', 3)
('d', 2)
('e', 1)
'''

#method 2 now gives us a way to sort based on values too
for item in sorted(d1.items(), key=lambda kv:kv[1]):
  print(item)
 
'''
('e', 1)
('d', 2)
('c', 3)
('b', 4)
('a', 5)
'''

#Couple it with reverse=True and now you have a complete way of sorting a dictionary (Java hashmap) with either value or key, reverse or not
print('Sorting on keys ascending [reverse=False is default]')
for item in sorted(d1.items(), key=lambda kv:kv[0], reverse=False):
  print(item)

print('Sorting on keys descending [reverse=False is default]')
for item in sorted(d1.items(), key=lambda kv:kv[0], reverse=True):
  print(item)

'''
Sorting on keys ascending [false is default]
('a', 5)
('b', 4)
('c', 3)
('d', 2)
('e', 1)
Sorting on keys descending [false is default]
('e', 1)
('d', 2)
('c', 3)
('b', 4)
('a', 5)
'''

#Sorting on the values
print('Sorting on values ascending [reverse=False is default]')
for item in sorted(d1.items(), key=lambda kv:kv[1], reverse=False):
  print(item)

print('Sorting on values descending [reverse=False is default]')
for item in sorted(d1.items(), key=lambda kv:kv[1], reverse=True):
  print(item)

'''
Sorting on values ascending [reverse=False is default]
('e', 1)
('d', 2)
('c', 3)
('b', 4)
('a', 5)
Sorting on values descending [reverse=False is default]
('a', 5)
('b', 4)
('c', 3)
('d', 2)
('e', 1)
'''

#Lets see how it works with dictionary of lists

d2 = {'a':[5,2], 'b':[4,3], 'e':[1,3], 'd':[2,5], 'c':[3,2]}
for item in sorted(d2.items(), key=lambda kv:kv[1], reverse=False):
  print(item)

'''
('e', [1, 3])
('d', [2, 5])
('c', [3, 2])
('b', [4, 3])
('a', [5, 2])
'''
