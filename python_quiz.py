
#Task 1: Adding machine
'''
Write a function that adds two numbers x,y and returns the output x + y. 
Sample input might be x=-1, y=8 in which case the expected output is 7. 
The expected output is either float or int.
'''

def func(x,y):
    return x+y

func(1,8)

#Task 2: Character count
'''
Write a function that takes two arguments
- s an arbitrary string.
- l a letter (i.e. any valid single character).

The function should search the string for occurences of the letter and 
return an integer indicating how many times the letter l occurs in the string s.
Note: Your function should be case-insensitive, i.e. it shouldn't care if the letter is "H" or "h"
'''

def string_func(s,l):
    return (s.lower().count(l.lower()))

string_func("Heej med dig", "e")

#Task 3: Function isEven
'''
Write a function which evaluates if a given integer number (given as a parameter for the function) is an even number. 
The function should return a Boolean value True if the number is even and False if the number is odd.
Given a list (or array) of n integer numbers, write a program which uses the function isEven to determines the number of even items in the list.
'''

def isEven(n):
    return (n % 2 == 0)

even_count = 0
list_numbers = [1,2,4,5,3,2]

for num in list_numbers: 
    if isEven(num):
        even_count = even_count + 1
print(even_count)
          
   

#Task 4: Search in List
'''
Given a list (or array) of n floating-point numbers, write a program which searches and outputs the largest number in the list.
'''

print(max(list_numbers))

#Task 5: String and Loops
'''
Write a function which takes a string (word) as an argument. 
The function should print the complete word on the first line 
and remove the last character on each successive line, ending with a single (the first) character.
Example: Input word is Test
Function output:
Test
Tes
Te
'''

def string_w(word1):
    while word1:
        print(word1)
        word1 = (word1[:-1])
        if len(word1) == 1:
            return (word1)

string_w("Test")

#Task 6: Get dict keys
'''
Write a function that takes as it's single input any dictionary
The function should return the keys of the input dictionary, in a list.
'''

def getDictKeys(dict): 
    return dict.keys() 


