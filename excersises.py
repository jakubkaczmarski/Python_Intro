#@Basics
# Part1:
# 1. Define an integer, a float, a string.
# name = "Paul"
# age = 23
# PI = 3.14
# 2. Assign 5 values in one line.
# counter, i, j, k, p = 0, 0, 0, 0, 0
# 3. Create 4 lists with: only numbers, only strings, only lists and all mixed together.
# n_list = [2,33,3,4,6,7]
# s_list = ["Dog", "Cat", "Fish"]
# m_list = ["Siemanko", 0, "What's up", 2]

# 4. Add, delete, iterate, remove, change, access value in the list.
# test_list = [1,2,3,6,2]
# test_list.append(12)
# for val in test_list:
#     print(val)
# test_list.remove(2)
# for val in test_list:
#     print(val)
# test_list[2] = 1

# 5. Play around with `* - + / % **` on the variables - what is possible for which variable type?
# print(name + " siemanko")
# print(age**age)
# print(PI / PI)
# 6. Create two lists containing 10 instances of different variables. You are also required to create a list called big_list, which contains each variable, 10 times each, by concatenating the two lists you have created.
# first_list = [2,3,5,6,1,9,0,2,4]
# second_list = [0,1,3,2,9,2,1,8,7]

# big_list = [first_list + second_list]
# print(big_list)
# 7. Write a format string with `%s, %f, %d`.

# format_str = (`%s Siemanko %f middle`, "marek", 12)
#to do

# print(format_str)
# 8. Test out `index(), count(), [start:stop:step], reverse, startswith(), endswith(), split(), lower(), upper()` functionalities of string.

# big_string =  "I was in the shop in yesterday"
# print(big_string.index("was"))
# print(big_string.count("in"))
# print(big_string[2: 10])
# print(big_string.startswith("s"))
# print(big_string.endswith("s"))
# print(big_string.split(" "))
# print(big_string.lower())
# print(big_string.upper())
# print(big_string.startswith())

# 9. Play around with `is not in and or`.

# print(big_list is not "Siemnako" or 1 is 1)

# 10. Create 4 functions with 4 different parameter types: default, keyword, variable numbers and required.

# def test_func_():
#     print("test")

# def test_func(num1, num2 = 2):
#     print(num1, num2)

# test_func(1)
# test_func_()

# 11. Create a list with a list inside - does it become one big list or a list with a second list in it?

# list_1 = [[]]
# print(list_1)

# 12. Play with exceptions, implement 10 most popular mistakes in python made by the beginners and try/except them all with proper handling.

# try:
#     l = ["A", "B"]
#     int(l[1])
# except (ValueError, IndexError) as e:
#     print("Amazing ", e)

# 13. Create a class called `Programmer` with attributes `language` and `has_glasses` that inherits from a class called `Person` with `age` and `name` attributes. Implement getters, setters and constructors for them.

# class Person:
#     def __init__(self, name = "default name", age = 10):
#         self.age = age
#         self.name = name

        
# class Programmer(Person):
#     def __init__(self, name = "default name", age = 10):
#         super()
#         self.name = name
#         self.age = age
#         self.language = "Default name"
#         self.has_glasses = False

# generic_dude = Person()
# print("Hi my name is ", generic_dude.name, " i am ", generic_dude.age, " years old")
# programmer_dude = Programmer("Maciek", 12)
# print("Hi my name is ", programmer_dude.name, " i am ", programmer_dude.age, " years old ", ( "and i wear glasses" if programmer_dude.has_glasses else "i don't wear glasses"))
# 14. Convert the list of weights to numpy array, then all of the weights from kg to lbs. Use the scalar conversion of 2.2 lbs per kg for conversion and print the result array in lbs. `weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]`.
# import numpy as np
# weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
# numpy_arr = np.array(weight_kg)
# numpy_arr = numpy_arr * 2.2

# print(numpy_arr)

#@Part 2 
# 1. Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# name, age
# name = input("Write you're name: ")
# age = input("Write you're age: ")
# try:
#     age = int(age)
# except ValueError as er:
#     print("Not a number provided")
#     exit()
# if age <= 100:

#     print("Hi ", name , " you will be a 100 years old in ", 100 - age)
# else:
#     print("You're already a 100 years old")




 # 2. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615
# val_n = 0
# val_n = input("Enter value: ")

# try:
#     val_n = int(val_n)
# except ValueError as err:
#     print("Non integer value provided")

# print(val_n * 1 + val_n * 11 + val_n * 111)

# 3. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.

# row = input("row val: ")
# column = input("column val: ")
# try:
#     row = int(row)
#     column = int(column)
# except ValueError as err:
#     print("Error")
# i = 0
# j = 0

# arr =  [[0] * column] * row
# for column in arr:
#     j = 0
#     for row in column:
#         arr[i][j] = i * j
#         j+=1
#     i+=1
    
# print(arr)


# 4. Write a Python program to check a triangle is valid or not 

# print("Enter triangle dimensions:")
# x = input("x: ")
# y = input("y: ")
# z = input("z: ")


# try:
#     x = int(x)
#     y = int(y)
#     z = int(z)
# except TypeError as err:
#     print("error")
#     exit(1)

# if x + y < z or z + y < x or z + x < y:
    # print("Triangle is not valid")
# else:
#   print("Triangle is valid")
# 5. Write a Python program to construct the following pattern, using a nested loop number.

# 6. Write a Python program to construct the following pattern, using a nested for loop.

# 7. Write a Python program that accepts a string and calculate the number of digits and letters

# inp = input("Put a string\n")

# letters = 0
# digits = 0

# for character in inp:
#     if character.isdigit():
#         digits += 1
#     elif character.isalpha():
#         letters += 1

# print("Letters ", letters)
# print("Digits ", digits)

# 8. Count the number of even and odd numbers from a series of numbers
# input 
# 9. Write a Python program to get the Fibonacci series between 0 to 50
# def fib(num):
#     if num <= 1:
#         return num
#     return fib(num - 1) + fib(num - 2)

# num = 5
# while True:
#     num = fib(num)
#     print(num)
#     if num > 50:
#         break

# 10. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

# for num in range(1500, 2700):
#     if(num % 7 == 0 and num % 5 == 0):
#         print(num)

# 11. Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# import random
# num = random.randint(1, 9)

# while True:
#     guess = input("Guess number from 1 to 9\n")
#     try: 
#         guess = int(guess)
#     except ValueError as err:
#         print("Wrong type")
#     if guess > num:
#         print("Too big")
#     elif guess < num:
#         print("Too small")
#     else:
#         print("You guessed right ")
#         break

# 12. Write a Python program to check the validity of a password (input from users).
# special_characters = "!@#$%^&*()-+?_=,<>/"
# password = input("Enter new_password\n")

# contains_dig = False
# if(len(password) < 8):
#     print("Password has less than 8 characters try again")
# for char in password:
#     if(char.isdigit()):
#         contains_dig = True
# if(not contains_dig):
#     print("Password doesn't have a number")

# 13. Write a Python program to check a triangle is equilateral, isosceles or scalene.

# x = int(input("X\n"))
# y = int(input("Y\n"))
# z = int(input("Z\n"))

# if(x + y < z or x + z < y or y + z < x):
#     print("Traingle doesn't exists")
# elif(x == y == z):
#     print("Triangle is equilateral")
# elif(x == y or y == z or z == x):
#     print("Triangle is isosceles")
# else:
#     print("Triangle is scalene")

# 14. Write a Python program to check whether an alphabet is a vowel or consonant.

# val = input("put alphabet \n")
# vowels = ["A", "E", "I", "O", "U"]
# if(len(val) == 1):
#     for vowel in vowels:
#         if(vowel == val.upper()):
#             print("Vowel")
#             exit(1)
#     print("Consonant")

# 15. Convert a list of characters into a string

# char_list = ["a", "b", "c", "d"]
# out = ""
# out = out.join(char_list)
# print(out)

# 16. Write a Python program to check whether a list contains a sublist.

# big_list = [["big", "small"],["red", "black"]]
# print(big_list.__contains__(["big", "small"]))

# 17. Write a Python program to find common items from two lists.

# list_one = [1, 3, 2, 9, 4, 9, 0]
# list_two = [8, 2, 3, 4, 5, 6, 7]

# print(list[set(list_one).intersection(list_two)])

# 18. Write a Python program to get the difference between the two lists

# list_one = [1, 3, 2, 9, 4, 9, 0]
# list_two = [8, 2, 3, 4, 5, 6, 7]

# sum_set_one = 0
# for el in list_one:
#     sum_set_one += el
# for el in list_two:
#     sum_set_one -= el
# print(sum_set_one)
# 19. Write a Python program to get the maximum number from a list.
# just_list = [3, 111, 2,9]
# max = just_list[0]
# for el in just_list:
#     if(max < el):
#         max = el
# print(max)
# 20. Write a Python program to get the frequency of the elements in a list.
# big_list = [2,4,5,6,1,3,43,22,6,1,5,7,8,2,1,5]

# frequency_list = {}

# for item in big_list:
#     if item in frequency_list:
#         frequency_list[item] += 1
#     else:
#         frequency_list[item] = 1

# print(frequency_list)

# 21. Write a Python program to generate all permutations of a list in Python



# 22. Write a Python program to remove duplicates from a list.

# 23. Write a Python program to find the second smallest number in a list.


# 24. # Write a Python program to sum all the items in a list

# 25. Write a Python program to create a Caesar encryption

# 26. Write a Python program to change a given string to a new string where the first and last chars have been exchanged 


# 27. Write a Python program to count the number of characters (character frequency) in a string.

# 28. Write a Python function to create the HTML string with tags around the word(s).

# 29. Write a Python function that takes a list of words and returns the length of the longest one.

# 30. Write a Python program to remove the nth index character from a nonempty string.


# 31. 'The quick brown fox jumps over the lazy dog.'
# input : "The quick brown fox jumps over the lazy dog."
# output : "dog. lazy the over jumps fox brown quick The "


# 32. Write a Python program to calculate the length of a string.

# 33. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)

# 34. Write a Python program to count the occurrences of each word in a given sentence.

# 35. Check if a given key already exists in a dictionary

# 36. Write a Python script to concatenate following dictionaries to create a new one.

# 37. Write a Python program to iterate over dictionaries using for loops.

# 38. Write a Python program to sort (ascending and descending) a dictionary by value.

# 39. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

# 41. Write a Python program to get the file size of a plain file.

# 42. Write a Python program to read first n lines of a file.

# 43. Write a python program to find the longest words in a file.

# 44. Write a Python program to read a random line from a file.

# 45. (!) Write a Python program to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. 

# 47. Write a Python class to convert a roman numeral to an integer

# 48. Write a Python program to convert an integer to a roman numeral.

# 49. Write a Python class which has two methods: getString and printString. 
# getString accepts a string from the user and printString prints the string in upper case.


# 50. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle. 

# 51. Write a Python class to reverse a string word by word.

# 52. Write a Python program to find the three elements that sum to zero from a set (array) of n real numbers.

# 53. Write a Python program to convert a binary number to decimal number. 

# 54. Write a Python program to flip a coin 1000 times and count heads and tails. 

# 55. Write a Python program to generate a series of unique random numbers.

# 56. Write a Python function to round up a number to specified digits.  
# 57. Write a Python program to calculate the standard deviation of the following data.

# 58. Write a Python program to convert Year/Month/Day to Day of Year.
# 59. Write a Python program to get the current time in Python.
# 60. Write a Python script to display the various Date Time formats.
# 61. Write a Python program to get current time in milliseconds in Python.
# 62. Write a Python program to subtract five days from current date
# 63. Write a Python program to find all five characters long word in a string.
# 64. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
# 65. Write a Python program to find the occurrence and position of the substrings within a string.
# 66. Write a Python program to remove everything except alphanumeric characters from a string.
# 67. Write a Python program to remove the parenthesis area in a string.
# 68. Remove all whitespaces from a string.
# 69. #Write a Python program to remove leading zeros from an IP address.
# 70. Find the length of longest non-repeatable substring in a string
# 71. Given a collection of intervals which are already sorted by start number, merge all overlapping intervals.
# For example,
# Given [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]],
# return [[1, 10], [11, 18], [19, 22]]
# 72. Consider an array of non negative integers. 
# A second array is formed by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which one is missing in the second array.
# Input: [1, 2, 3, 4, 5, 5, 6, 7] [3, 7, 2, 1, 4, 6, 5]
# Output: 5 is the missing number
# 73. Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3,
# the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
# Note:
# Try to come up as many solutions as you can,
# there are at least 3 different ways to solve this problem.

# 74. Given a sorted integer array without duplicates,
# return the summary of its ranges.
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].


# 75. Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution
# Example:
#     Given nums = [2, 7, 11, 15], target = 26,
#     Because nums[2] + nums[3] = 11 + 15 = 26,
#     return [2, 3].


# 76. Write a Python program to sort a list of elements using the bubble sort algorithm.


# 77. Write a Python program to sort a list of elements using the insertion sort algorithm.


# 78. Write a Python program to sort a list of elements using the selection sort algorithm.


# 79. (!) Write a Python program to sort a list of elements using shell sort algorithm.
# Note : According to Wikipedia "Shell sort or Shell's method, is an in-place comparison sort. 
# It can be seen as either a generalization of sorting by exchange (bubble sort) or sorting by insertion (insertion sort). 
# The method starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between
# elements to be compared. Starting with far apart elements can move some out-of-place elements into position faster than
# a simple nearest neighbor exchange."



# 80. Write a Python program to sort a list of elements using the merge sort algorithm.



# 81.(!) Write a Python program to sort a list of elements using the quick sort algorithm.


# 82. Write a Python program for sequential search.
# Sequential Search: In computer science, linear search or sequential search is a method for finding a particular value in a list
# that checks each element in sequence until the desired element is found or the list is exhausted. The list need not be ordered.


# 83. Write a Python program for binary search. 
# Binary Search : In computer science, a binary search or half-interval search algorithm finds the position of a target value
# within a sorted array. The binary search algorithm can be classified as a dichotomies divide-and-conquer search algorithm and 
# executes in logarithmic time.


# 84. Write a Python program to calculate the value of 'a' to the power 'b'. 


# 85. Write a program to solve the Fibonacci sequence using recursion. 


# 86. Write a Python program to get the factorial of a non-negative integer.   


# 87. Write a Python program to find the greatest common divisor (gcd) of two integers.

# 88. Write a Python program to calculate the sum of a list of numbers. (in recursion fashion)


#@Part 3
# 1. Create a generator with nested loop (two for loops).


# 2. Create a fibonacci generator and stop it after 10 calls in two ways: with passing stop parameter and without passing it.

# 3. Using a list comprehension, create a list from `numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]` that will contain only positive numbers form that list as integers.

# 4. Create a partial function from a function.

# 5. Create a partial function from a built-in method in python (google "built-in methods in python" and choose one you like the most).

# 6. Edit the following function: `def func(u,v,w,x): return u*4 + v*3 + w*2 + x` with partial() call, so the new function takes one parameter and returns 60. Print out the result of new partial function.


# 7. Play around with all code introspection functions.

# 8. Create and call a function that uppercases characters on 10 different type elements in list.

# 9. Use lambda function to raise to the power of 2 each element in the above list with `map()`.
# 10. Pass multiple iterables to `map()` function.
# 11. Recreate `zip()` function with `map()` (lambda is also recommended).
# 12. Calculate the sum of 10 numbers in list with `reduce()`.
# 13. Calculate a chance of winning a lottery (6 out of 49) with `reduce()` function.
# 14. There is a list of floats, all in five decimal places. Return a map object with each element round up to its position decimal places, meaning that you have to round up the first element in the list to one decimal place, the second one to two decimal places etc.
# 15. Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures. That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures. (`multiplywith5 = multiplier_of(5)` `multiplywith5(9)`).
# 16. Create a function that takes 3 arguments and prints them. Call it by passing only *args and **kwargs.
# 17. In one function, use all of fargs, *args and **kwargs.
# 18. Create generator, list, dict and set comprehensions.


# 19. Create a function which receives 2 required + a variable amount of arguments and returns the number of extra args.


# 20. Modify a function `def bar(a, b, c):` so it returns true if the argument with a keyword number equals 7.


# 21. Print out all the duplicates from list.


# 22. Create a coroutine. Use `yield` twice and see what it does. Use `fct.send()` before `next()` as see what it does.


# 23. Create a few 2 dimensional arrays, then try to convert them to nested lists by using list comprehension.


# 24. Use `a = ["Jake", "John", "Eric"]` and `b = ["John", "Jill"]`  lists to print out a set containing all the participants from event A which did not attend event B. Play around with those.


# 25. Create two functions that define a mutable iterable (as none and empty, respectively) as a first parameter and the value as another one. It adds a value to an iterable. Call & print it 3 times. Iterable defined as empty should add to iterable each time fct is called, while none should create a new list each time.