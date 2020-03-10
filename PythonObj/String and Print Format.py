# -*- coding: utf-8 -*-

"""
Variable:
Variable name: Lowercase better
Allowing to change form
Be aware of using type() to check the type of variable

"""

#Allowing to change form
my_dogs = 2
my_dogs = ["Sammy", "Franke"]


# Be aware of using type()
type(my_dogs)




"""
String
    Using single or double quotes
    Can use indexing and slicing to grab sub-sections of the string.
    index: []
        h e l l o
        0 1 2 3 4
    Reverse index:
        h e  l  l  o
        0 -4 -3 -2 -1
        
    slicing:
        start:stop:step
        
    Properties and Methods
    Immutability: typically means you cannot change
    Merge strings: Plus Mutiplication
    
    Example Methods: upper, lower, split
    
"""
#initialize string
my_string = 'hello world' 
my_sentence = " I'm going on a run "


# Print function
print(my_string)


# Print in two line
print("Hello \nWorld")


# THe length of a String
len("I am")
print(len("I am"))


#indexing and slicing
my_string = "Hello World"
print(my_string[0])
print(my_string[8])


#index from back
print(my_string[-1])


#Slicing
my_string = "abcdefghijk"

#print start from indexing 2 (include index 2)
my_string[2:]
#print until the index 3 (not include the index 3)
my_string[:3]
#grab string in middle lenth is end position - start position
my_string[2:5]



#Step size: jumping over a size

my_string = "abcdefghijk"
my_string[::2]
my_string[::3]
my_string[2:7:2]


#Trick: reverse string
my_string[::-1]


#Properties and methods
#Immutiability
name = "Sam" #change it to Pam
# name[0] = "P" # you cannot do this (item assignment)


#Plus: Merging string together
last_letters = name[1:] #am
name = "P" + last_letters


#Multiple: 
string = "ab"
print(string * 10)


#Method: upper lower split
string = "Hello world"
string.upper()
print(string) #string still equal to "Hello world"
print(string.upper()) #Print HELLO WORLD
print(string.lower()) #Print hello world

string.split() #Return a list devided by space or the letter you pass in 
#Out[10]: ['Hello', 'world']
string.split("l")
#Out[11]: ['He', '', 'o wor', 'd']



"""
Print Formatting with Strings

.format
f-strings

"""

print("This is a string {}".format('INSERT'))

print('The {} {} {}'.format("fox","brown","quick"))

print('The {2} {1} {0}'.format("fox","brown","quick"))

print('The {0} {0} {0}'.format("fox","brown","quick"))

print('The {q} {b} {x}'.format(q = "fox",b = "brown",x = "quick"))

number = 1

print("This is a string {}".format(number))

#float formatting: {value: width.precision f} 
#width: how long you want this string to be
result = 100/7
print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))
print("The result was {r:10.5f}".format(r=result))#this will add space to the number

#f-string
name = "Tom"
age = 13
print(f'Hello, {name}. you are {age} years olds')












