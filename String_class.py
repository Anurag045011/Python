# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:49:06 2023

@author: Anurag
"""

#Python program to demonstrate String Datatype

# Creating a String
a="Virat Kohli, the Indian cricket team captain,is my favourite cricketer" 
print(a)

# Printing First character
String1="I am Anurag"
print("\nFirst character of String is: ")
print(String1[0])
 
# Printing Last character
print("\nLast character of String is: ")
print(String1[-1])

#Program to reverse a string
name = "Anurag Sharma"
print(name[::-1])


# Python Program to demonstrate String slicing
b="python is a case sensitive language"
print(b)

# Printing 1st to 12th character
print("\nSlicing characters from 1-12: ")
print(b[1:12])
 
# Printing characters between 3rd and 2nd last character
print("\nSlicing characters between " +
      "3rd and 2nd last character: ")
print(b[3:-2])

# Splits Word into a List of Individual Characters 
s1 = 'i love python' 
print(list(s1.split()))


# Python3 program to show the working of upper() function
text = 'gaMeRs For liFe'
 
# upper() function to convert string to upper case
print("\nConverted String:")
print(text.upper()) #GAMERS FOR LIFE
 
# lower() function to convert string to lower case
print("\nConverted String:")
print(text.lower()) #gamers for life
 
# converts the first character to upper case and rest to lower case
print("\nConverted String:")
print(text.title()) #Gamers For Life
 
#swaps the case of all characters in the string upper case character to lowercase and viceversa
print("\nConverted String:")
print(text.swapcase()) #GAmErS fOR LIfE
 
# convert the first character of a string to uppercase
print("\nConverted String:")
print(text.capitalize()) #Gamers for life
 
# original string never changes
print("\nOriginal String")
print(text) 

#Returns the number of occurrences of a substring in the string--->count()
my_string = "Gamersforlife"
char_count = my_string.count('e')
print(char_count)
