lst1 = [89,54,78,89,90]
lst2 = [91,83,94,76,88]

set1 = {'hi',7,49,"Good"}
set2 = {7,7,"ms",67,90}

dict1 = {1:'a',2:'b',3:'c'}

tup = (6,67,4,90,434)
tup2 = (68,55,67,55,3)

d1 = dict(zip(lst1,lst2))
print(d1)
d2 = dict(zip(tup,tup2))
print(d2)
d3 = dict(zip(set1,set2))
print(d3)

"""
#list, set, tuple conversion to dictionary
list_dict = dict(lst1)
print(list_dict,type(list_dict))
set_dict = dict(set1)
print(set_dict,type(set_dict))
tuple_dict = dict(tup)
print(tuple_dict,type(tuple_dict)) #dict object is not callable


print(lst1, type(lst1))
print(lst2, type(lst2))
print(set1, type(set1))
print(dict1, type(dict1))
print(tup, type(tup))

#set, dictionary, tuple conversion to list
set_list = list(set1)
print(set_list,type(set_list))
dict_list = list(dict1)
print(dict_list,type(dict_list)) #keys are converted to list
tuple_list = list(tup)
print(tuple_list,type(tuple_list))	

#list, dictionary, set conversion to tuple
list_tuple = tuple(lst1)
print(list_tuple,type(list_tuple))
dict_tuple = tuple(dict1)
print(dict_tuple,type(dict_tuple))
set_tuple = tuple(set1)
print(set_tuple,type(set_tuple))	


#list,dictionary , tuple conversion to set 
list_set = set(lst1)
print(list_set,type(list_set))
dict1_set = set(dict1)
print(dict1_set,type(dict1_set))
tuple_set = set(tup)
print(tuple_set,type(tuple_set))
"""