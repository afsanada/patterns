# 1. concatenate 2 list 
# a=[1,2,3,4]
# b=[5,6,7,8]
# c=a+b
# print(c)

# 2. using extend method 
# a.extend(b)
# print(a)

#3.
# import math

# n = 3.7
# F_num = math.floor(n)
# print(F_num)  o/p : 3

#4.
# print(5//2) o/p: 2
# print(5/2) o/p: 2.5

#5.
# def add(x, y):
#     return x + y
# def apply_func(func, a, b):
#     return func(a, b)
# print(apply_func(add, 3, 5)) o/p: 8

#6.
# x = 10       # x is an integer
# x = "Hello"  # Now x is a string

#7.
# def call_by_val(x):
#     x = x * 2
#     return x


# def call_by_ref(b):
#     b.append("D")
#     return b


# a = ["E"]
# num = 6

# # Call functions
# updated_num = call_by_val(num)
# updated_list = call_by_ref(a)

# # Print after function calls
# print("Updated value after call_by_val:", updated_num)
# print("Updated list after call_by_ref:", updated_list) o/p:Updated value after call_by_val: 12
# Updated list after call_by_ref: ['E', 'D']

#8.
# s1 = 'GeeksforGeeks'

# s2 = lambda func: func.upper()
# print(s2(s1)) o/p: GEEKSFORGEEKS

#9.
# a = [2,3,4,5]
# res = [val ** 2 for val in a]
# print(res)
# o/p : [4, 9, 16, 25]

#10.
# def fun(*argv):
#     for arg in argv:
#         print(arg)

# fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
# o/p:
# Hello
# Welcome
# to
# GeeksforGeeks

# 11. **kwargs
# def fun(**kwargs):
#     for k, val in kwargs.items():
#         print("%s == %s" % (k, val))


# Driver code
# fun(s1='Geeks', s2='for', s3='Geeks')

#o/p: 
# s1 == Geeks
# s2 == for
# s3 == Geeks

#12.
# keys = ['a','b','c','d','e']
# values = [1,2,3,4,5]  

# this line shows dict comprehension here  
# d = { k:v for (k,v) in zip(keys, values)}  

# We can use below too
# d = dict(zip(keys, values))  

# print (d)
# o/p:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# 15. Write a code to display the current time?

# import time

# currenttime= time.localtime(time.time())
# print ("Current time is", currenttime)

#16.print reverse
# numbers = [1, 2, 3, 4, 5]

# while (n := len(numbers)) > 0:
#     print(numbers.pop())

#17.Converting an Integer into Decimals

# import decimal
# integer = 10
# print(decimal.Decimal(integer))
# print(type(decimal.Decimal(integer)))
# o/p: 10
# <class 'decimal.Decimal'>

# 18. Converting a String of Integers into Decimals
# import decimal
# string = '12345'
# print(decimal.Decimal(string))
# print(type(decimal.Decimal(string)))

# o/p:
# > 12345
# > <class 'decimal.Decimal'>

# 19. Reversing a String using an Extended Slicing Technique
# string = "Python Programming"
# print(string[::-1])

# o/p> gnimmargorP nohtyP

# 20. Counting Vowels in a Given Word
# vowel = ['a', 'e', 'i', 'o', 'u']
# word = "programming"
# count = 0
# for character in word:
#     if character in vowel:
#         count += 1
# print(count)

# o/p> 3

#21. Counting Consonants in a Given Word

# vowel =['a','e','i','o','u']
# word = "programming"
# count =0
# for character in word:
#     if character not in vowel:
#         count += 1

# print(count)

# o/p> 8

#22. Counting the Number of Occurrences of a Character in a String

# word= "python"
# letter = "p"
# count = 0
# for character in word:
#     if character in letter:
#         count += 1

# print(count)
#o/p : 1

#23.Writing Fibonacci Series

# fib = [0,1]
# for i in range(5):
#     fib.append(fib[-1] + fib[-2]) 

# Converting the list of integers to string
# print(', '.join(str(e) for e in fib))
# o/p: 0, 1, 1, 2, 3, 5, 8

#24.Finding the Maximum Number in a List
# numberList = [15, 85, 35, 89, 125]
# maxnum = numberList[0]
# for num in numberList:
#     if maxnum < num:
#         maxnum = num
# print(maxnum)
# o/p:125

#25. Finding the Minimum Number in a List
# numberList = [15, 85, 35, 89, 125, 2]

# minNum = numberList[0]
# for num in numberList:
#     if minNum > num:
#         minNum = num
# print(minNum)

# o/p:2

# 26. Finding the Middle Element in a List

# numList = [1, 2, 3, 4, 5]
# midElement = int((len(numList)/2)) 

# print(numList[midElement])
# o/p:3

# 27.Converting a List into a String
# lst = ["P", "Y", "T", "H", "O", "N"]
# string = ''.join(lst)

# print(string)
# print(type(string))

# o/p:YTHON
# <class 'str'>

# 28.Adding Two List Elements Together

# list1 =[1,2,3]
# list2 =[4,5,6]
# res_lst=[]
# for i in range(0,len(list1)):
#     res_lst.append(list1[i]+list2[i])
# print(res_lst)

# o/p:[5, 7, 9]

# 29. OR
# a = [1, 2, 3]
# b = [4, 5, 6]
# c=[x+y for x,y in zip(a,b)]
# print(c)

#30. Comparing Two Strings for Anagrams
# str1 = "String"
# str2 = "String"
# str1 = list(str1.upper())
# str2 = list(str2.upper())
# str1.sort(),str2.sort()

# if(str1==str2):
#     print("True")
# else:
#     print("False")

#     o/p: True

# 31.Checking for Palindrome Using Extended Slicing Technique
# str1 = "Kayak".lower()
# str2 = "Kayak".lower()
# if(str1==str2[::-1]):
#     print("True")
# else:
#     print("False")

#     o/p: True

# 32.Counting the White Spaces in a String

# str1 = " This is a number"
# print(str1.count(' '))

# o/p:4

# 32.Counting Digits, Letters, and Spaces in a String
# Importing Regular Expressions Library
# import re

# name = 'Python is 1'

# digitCount = re.sub("[^0-9]", "", name)
# letterCount = re.sub("[^a-zA-Z]", "", name)
# spaceCount = re.findall("[ \n]", name)

# print(len(digitCount))
# print(len(letterCount))
# print(len(spaceCount))
    
# > 1
# > 8
# > 2

# text = input("Enter String:")

# digitcount = 0
# lettercount = 0
# spacecount = 0

# for char in text:
#     if char >= '0' and char <= '9':
#         digitcount +=1
#     elif (char >='a' and char <= 'z') or (char >= 'A' and char <='Z'):
#         lettercount += 1
#     else:
#         spacecount += 1

# print(digitcount)
# print(lettercount)
# print(spacecount)

# o/p:Enter String:Hello World 123
# 3
# 10
# 2