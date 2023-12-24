l1 = [1,2,3,4,5,6,7,8,9]

print(type(l1),l1)

#lst [ initial : end : indexJump ]
#initial = list slicing starts from the given number
#end = slicing ends to this number i.e. one number before the given end number slicing is done
#indexJump = steps size from one index to next index  

print(l1[::])	# 0 to len of list (end)
print(l1[-1])	# negative indexing means start at last element index
print(l1[0])	# positive indexing first element 
print(l1[::-1])	# 0 to len of list and then it will jump from -1 i.e. end to first
print(l1[:-1])	# 0 to position given to end is -1 
print(l1[0:8])	
print(l1[0:9])
print(l1[0:9:3])#0 to 9th index means first element to last element(who's inedx is 8) with 3 inedxjump 3

print()
tup = (1,2,3,4,5,6,7,8,9)
print(type(tup),tup)

print(tup[::])	
print(tup[-1])	
print(tup[0])	 
print(tup[::-1])	
print(tup[:-1])	
print(tup[0:8])	
print(tup[0:9])
print(tup[0:9:3])

print()
s1 = {1,2,3,4,5,6,7,8,9}
print(type(s1),s1)
"""
print(s1[::])	
TypeError: 'set' object is not subscriptable

There is no index attached to any element in set. 
So they do not support any indexing or slicing operation
"""

print()
dic = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'}
print(type(dic),dic)
"""
print(dic[::])	
Dictionary slicing operation
line 23, in <module>
    print(dic[::])      # 0 to len of list (end)
TypeError: unhashable type: 'slice'
"""