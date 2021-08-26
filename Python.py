# ***These are my notes for the python course*** the triple stars mean its important to me.

# print(bin(3))
# print(int('0b11', 2))

# The data types 

# int
# float
# complex
# str
# bool 
# list 
# tuple 
# set 
# dict

# Variables

# iq = 3
# iq2 = 7
# print(iq + iq2)
# put variables in caps to show that it is a constant
#------------------------------
# iq = 100
# user_age = iq/5
#----------------------------------------
# augmented assignment operator
# value = 5
# value += 3
# print(value)
#--------------------------------

# username =  'megamind'
# password = 'supersecret'

# first_name = 'm'
# last_name = 'h'
# full_name = first_name + ' ' + last_name
# print(full_name)
# ------------------------------

#type conversion 
# add str or int to convert a datatype
# e.g
# # str(100)
# '100' is usually an int data type, but adding str converts it into 
# a string datatype
#------------------------------------

# Escape sequence 
# \t makes a tab
# \n makes a new line
# \ makes python look at whats after the \ as a string
# weather = "its\'s \"kinda\" sunny"
# print(weather)
#------------------------------------------

# Formatted strings
# user_id = 'joe'
# name = user_id

# print(f'welcome back {name}')
#this is a python 3 luxery
#in python 2 they used .format
#-----------------------------

#string indexes
# selfish = 'me me me'
# print(selfish[3:8])

#[start:stop:stepover]
# print(selfish[0:8:3])

# print(selfish[::-3])
#-----------------------------------------

#methods

# quote = 'no way jose'

# print(quote.())
#-----------------------------------------

#booleans

# name = 'mahmud'
# is_cool = False

# is_cool = True

# print(bool())
#---------------------------------------

# Type conversion
# name = 'Mahmud Hanish'
# age = 17
# status = 'online'

# birth_year = input('what year were you born?')

# age = 2021 - int(birth_year)

# print(f'your age is {age}')
#--------------------------------------------

#password checker

# username = input('enter username: ')
# password = input('enter password: ')
# hidden_password = '*' * len(password)
# password_length = len(password)
# print(f"{username}'s password {hidden_password} is {password_length} characters long")
#----------------------------------------------

#lists

# li = [1,2,3,4,5,]
# li2 = ['a','b','c',3]
# li3 = [True,1,2,3,'g']

# shopping_cart = ['whiskey', 'ravioli', 'mouse']
# print(shopping_cart[2])

#list slicing

# shopping_cart = [
#     'whiskey', 
#     'ravioli', 
#     'mouse' ,
#     'cheese' ,
#     'pesto' ,
#     'illegal firearm' ,
#     'beetroot' ,
#     ]

# new_cart = shopping_cart[:]
# new_cart[2] = 'gun'
# shopping_cart[0] = 'grape juice'
# print(new_cart)
# print(shopping_cart)
#==========================================

#pattern matching ***3.10 feature **new
# this is like elif, except on steroids, it seems that it can check for multiple cases for a statement
# e.g
# command_2 = 42

# match command_1:
#     case 42
#         print("This is 42")
#     case 200:
#         print("This is 200")

#this checks command_2 for its value and prints an output depending on the value.
#=================================================

#matrix

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# print(matrix)
#===================================================

# list methods

basket = ['a','b','c','d','e','a']

# #adding
# # new_list = basket.append(100)      # <-- this new list only added the value of 100 to basket, it isn't producing a result, so if i print new_list it will output none.
# basket.append(100)
# new_list = basket # this new list gives a result though

# print(new_list)

#insert: modifies the list, doesnt create a new list
# basket.insert(1, 600) 
# print(basket)

#==================================================================

#extend: extend also modifies the list, and doesnt create a new one in place of the old list.
# new_list = basket.extend([100, 101])
# print(new_list)
# print(basket)

#===================================================================

#removing methods: .pop & .remove : .pop removes the value in the place specified, while .remove removes the value specified, as shown below.
# .remove modifies the list, and pop can create a new list by returning whatever you "popped"


# new_list = basket.pop(1)
# new_list = basket.remove(1)

#clear is a removal methed that just clears the list, e.g

# basket.clear()
# print(basket)

#clear returns [] because the list was cleared obviously.

#the reason that i get a value returned with .pop, and i get 'none' with .remove is because .remove doesn't return a value, so none is printed. this will be explained in more detail further down.
# ***even if 2 methods are the "same" it doesnt mean that they function the same, just like how we saw with pop and remove***
#================================================================

#more list methods:

# print(basket.count('a'))
#count counts the number of a certain object, like 'a'

#sort: doesn't return anything
# basket.sort()

#sorted is a function, there for it doesnt modify the list, it creates a copy

# print(sorted(basket))

#.copy creates a copy the list

# basket.copy()

#.reverse reverses the order of the list, and doesnt sort it, it also only modifies it

# basket.reverse()
# print(basket)
#==================================================================

#list patterns
# basket.sort()
# basket.reverse()
# # print(basket[::-1])
# # print(basket)
# # print(list(range(1,101)))
# bruh2 = ' '.join(['hi', 'my', 'name', 'is', 'joe'])

# print(bruh2)
#======================================================================

#list unpacking

# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]

# print(a)
# print(b)
# print(c)
# print(other)
# print(d)
#======================================================================

#none is like 'null' it represents the absence of value
# None
#======================================================================

#Dictionary, is an unordered 'key : value' pair 
 
# user = {
# 'cart': [1,2,3],
# 'greet': 'goodmorning',
# 'is cool': False
# }



#when to use a dictionary, and when to use a list
#use a list when you want order. A dictionary holds more informaion however.
#dictionary keys cannot change, therefore i can use sstrings, booleans, even int. however i can't use a list as a key. and keys have to be unique.

# user2 = dict(name = 'mahmud')

#this is another way to make a dictionary


# user = {
# 'cart': [1,2,3],
# 'greet': 'goodmorning',
# 'is cool': False
# }
# user.update({'basket': [3,4,5]})
# print(user)
#=======================================



#tuple, un-modify-able list
# my_tuple = (1,2,3,4,5)

# print(my_tuple.count(2))
#two methods for tuples that are important, count and index. which we covered before with lists.

#Set is an unordered collection of unique objects

# my_list = [1,2,3,4,5,5]

# my_set = {1,2,3,4,5,5}
# new_set = my_set.copy()
# my_set.add(69)
# print(my_set.difference(new_set))

# set function can be used to remove duplicates




print('hello world')