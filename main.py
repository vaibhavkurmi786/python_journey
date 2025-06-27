# this is a single line comment

"""This is a multi line comment
 now i can write anything
in any number of lines
that i need to because this way i dont have to
use # again and again to comment
each and every line in a single go


"""

# by the way the python does not support multi line comments the above that we wrote is a docstring

# name variable with value as vaibhav
name = "vaibhav"

# age variable with value as 20
age = 20


# important points to remember while creating variables

# 1 can not use number at the start while creating a variable name (but can be used at the last)
# 2 can not use space at the starting or in between while creating a variable name (but can be used at the last as its not counted by python because its ignored at the execution time)
# 3 can not use special characters at the starting or in between while creating a variable


# NAMING CONVENTION 

# there are 3 ways to name a variable 
# 1) Camel Case = pythonLanguage
# 2) Pascal Case = Python Language
# 3) Snake Case = python_language 

# DATATYPES
# 1) NUMBERS
# 1.A) INT  => any number from -infinity to +infinity that doesn't contain a decimal is an integer value (ex)=> 786
# 1.B) FLOAT => any number that has a decimal in it ofr can be written in p/q format is a float value  (ex)=> 2.0
# 1.C) COMPLEX => any number written with j at its last is a complex value (ex)=> 2j

# 2) STRINGS  => anything that is written between "" or '' is called a string (ex)=> 'vaibhav', "kurmi
# 3) BOOLEAN  => True or False (ex)=> b = True, f= False


# in strings if we want to know the unicode of any character we use the method (ord) and to convert any number to character use use the method (chr) (ex)=> ord('a')

# print(ord('a'))
# print(chr(121))


# STRING INDEXING
# this means we can access any element of the string 
# there are two types of string indexing
# 1) positive
# 2) negative

# str = 'vaibhav kurmi'
# print(str[6]) this is the (ex) of positive indexing
# print(str[-3]) this is the (ex) of negative indexing


# STRING SLICING
# the syntax for slicing a string is =>  [starting point : ending point : how many jumps to make while slicing]

# print(str[2:6:1])
# print(str[:6:1])
# print(str[2::1])
# print(str[::])

# if we leave the start point and define the rest two point that means the starting point is from the start of the string
# if we leave the end point and define the rest two point that means the end point is till the end of the string
# if we leave the all point and just maintain the syntax that means the string will be sliced from the start till the end and by default the jump is always 1


# TYPE CONVERSION
# There are four types of type conversion
# 1) int() convert to integer  
# 2) float() convert to float
# 3) str() convert to string
# 4) bool() convert to boolean


# a= '1'
# print("before conversion", type(a))
# a = int(a)
# after using int()
# print("after conversion", type(a))

# a= float(a)
# # after using float()
# print("after conversion", type(a))

# a= bool(a)
# # after using float()
# print("after conversion", type(a))


# converion of integer to string is possible in all cases
# conversion of string to integer is possible in some cases
# conversion to boolean is possible for all except the falsy value as it can either be True or False
# falsy values ( False, 0, 0.0, "", [] list, {}dictionary, ()tupple)

# all the above viewed are explicit conversion i.e when using the methods to do conversion

# but some cases like dividing 12 by 3 the answer will be 4 according to us but according to python the answer will be 4.0
# so there will be a implicit conversion as python will automatically convert it into float 

# print(type(12/3))


# INPUT OUTPUT

# to take input from the user we just use the method input()

# name = input("please enter your name: ")

# to show the output we use the method print()

# this is a raw string
# print("hello : ", name) 

# this is a formatted string
# print(f"hello :  {name}") 

# OPERATORS

# there are diffefrent types of operators in python
# arithemetic operators = ['+', '-', '*', '/', '//', '%', '**']
# logical operators = ['and', 'or', 'not']
# comparison operators = ['==', '!=', '>', '<', '>=', '<=']
# assignment and compound assignment operators = ['=', '+=', '-=', '*=', '/=', '//=', '%=']


