# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:33:17 2020

@author: Chester
"""

#Dictionary is unordered mapping for stroring objects sing key-value pair
#when to choose dictionary and when to choose list:
#when you want to quickly retrieve the value without needing to know index 
#dictionary cannot be sorted !

#initialize
my_dictionary = {'key1':'value1', 'key2': 'value2'}
print(my_dictionary['key1'])

price_lookup = {'apple': 1.2, 'banana' : 1.5}
print(price_lookup['apple'])


#can embeded list or dictionary
dic = {'sad': 'to be happy', 'happy': {'method1': 'to be more happy', 2:'not to be sad'}, 3: ['list', 2, 2.5]}


print(dic['sad'])
print(dic['happy'][2])
print(dic[3])
print(dic[3][2])


#add pairs to dictionary and modify
d = {'low': 100, 'intermediate': 200}
d['high'] = 300
print(d)
d['intermediate'] = 250
print(d)


#method keys values 
d = {'low': 100, 'intermediate': 200, 'high': 300}
print(d.keys())
print(d.values())
print(d.items())

