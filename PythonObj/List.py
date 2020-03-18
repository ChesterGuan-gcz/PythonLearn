# -*- coding: utf-8 -*-


# define
# propoties: it can have multiple variable type
my_list = [1,2,3]
my_list2 = ["string", 100, 23.2]

print(my_list)
print(my_list2)

#check the length :
print(len(my_list))

 
#indexing and slicing and merging
my_list = [1,2,3]

print(my_list[1])
print(my_list[1:])

another_list = [4,5]
merge_list = my_list + another_list
print(merge_list)


#can change element: what string cannot do 
my_list[0] = "all I want is to change"
print(f"Here is first item of my list {my_list[0]}")

#add item in the end of the list
my_list.append("six")
print(my_list)


#remove things from list (pop) default to pop at end
my_list = [1,2,3,"end"]

print(my_list.pop())
print(my_list)

my_list = [1,2,3,"end"]
popitem = my_list.pop(0)
print(f"the poped item is {popitem} and the list now is {my_list}")


#sort and reverse: it won't return anything, just sort the original list
new_list = ['a','e','x','b','c']
num_list = [1,5,3,9,5]

#not return
sort_list = new_list.sort()
type(sort_list)

print(new_list)
num_list.sort()
print(num_list)

new_list.reverse()
num_list.reverse()
print(num_list)
print(new_list)

#Nested List