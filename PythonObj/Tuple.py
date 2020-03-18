# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:13:35 2020

@author: Chester
"""

#Tuple: immutability: cannot be changed

#initialize
my_tuple = (1,2,3)
my_list = [1,2,3,4]

print("the length of the tuple is {1} and the length of the list is {0}".format(len(my_list), len(my_tuple)))


print(my_tuple[0])
#cannot change  such as: my_tuple[0] = 3

#method index, count
t = ('a','b','a')

print(t.count('a'))
print(t.index('b'))
print(t.index('a'))


#Testing: if there is a list inside a tuple, whether the list can be changed
test_tuple = (1,2,[3,4])
test_tuple[2][0] = 1

print(test_tuple)#Result: the list inside a tuple is changeable 