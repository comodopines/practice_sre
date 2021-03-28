#Create a dictionary
d1 = {'a':5, 'b':4, 'e':1, 'd':2, 'c':3}

#Update an element in dictionary
d1['a'] = 10

#Find a key in dictionary
if 'x' in d1.keys():
  print(d1['x'])
  
if 'x' in d1:
  print(d1['x'])

#Python 3
if d1.has_key('x'):
  print(d1['x'])
 
#Setting/Initalizing if a key is missing
#Using in
if 'x' in d1.keys():
  pass
else:
  d1['x']=23
  
# Best way to initalize and increment if you are making frequency dictionary
#https://stackoverflow.com/a/473344
my_dict = {}
my_dict[some_key] = my_dict.get(some_key, 0) + 1  

#Let's say if you had a list
my_dict = {}
my_dict[some_key] = my_dict.get(some_key, []).append(some_value_to_list)  
#wrong

#Using try catch
try:
    dict[key] += 1
except KeyError:
    dict[key] = 1


#Using not in
if 'x' not in d1.keys():
  d1['x']=23
  
#Setting using set default
#https://stackoverflow.com/a/42315120
d1.setdefault('x', 23)
#if 'x' is present the present value is returned, else 23 is assigned and returned


