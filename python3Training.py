#NUMERICAL OPERATIONS

#Division always returns a float
print(2/2) #=1.0

#A float is also produced by running an operation on two floats, or on a float and an integer.
print( 8 / 2 )
print( 6 * 7.0 )
print( 4 + 1.65 )

#The modulo operator is carried out with a percent symbol (%) and is used to get the remainder of a division. 
print(20 % 6)
print(1.25 % 0.5) 
print( 7%(5 // 2) )

#STRINGS

#Some characters can't be directly included in a string. For instance, double quotes can't be directly included in a double quote string; this would cause it to end prematurely.
#Characters like these must be escaped by placing a backslash before them.
#Double quotes only need to be escaped in double quote strings, and the same is true for single quote strings.
print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')

#\n represents a new line. It can be used in strings to create multi-line output:
print('One \nTwo \nThree')   

#Newlines will be automatically added for strings that are created using three quotes.
#\t represents a tab.
print("""\tthis
is a
multiline
text""")  


#As with integers and floats, strings in Python can be added, using a process called concatenation, which can be done on any two strings. 
print("Spam" + 'eggs')

#Even if your strings contain numbers, they are still added as strings rather than integers.
print("2" + "2")

#Strings can also be multiplied by integers. This produces a repeated version of the original string. The order of the string and the integer doesn't matter, but the string usually comes first. 
print("spam" * 3)
print(4 * '2')

#VARIABLES

#To assign a variable, use one equals sign.
user = "James"  

#You can use variables to perform corresponding operations, just as you did with numbers and strings: 
x = 7
print(x)
print(x + 3)
print(x) 

#Variables can be reassigned as many times as you want, in order to change their value.
#In Python, variables don't have specific types, so you can assign a string to a variable, and later assign an integer to the same variable. 
x = 123.456
print(x)
x = "This is a string"
print(x + "!")

#Certain restrictions apply in regard to the characters that may be used in Python variable names. The only characters that are allowed are letters, numbers, and underscores. Also, they can't start with numbers.
#Not following these rules results in errors. 

#You can use the del statement to remove a variable, which means the reference from the name to the value is deleted, and trying to use the variable causes an error. 
#Deleted variables can be reassigned to later as normal.
foo = 2
bar = 3
del bar
bar = 8
print(foo * bar)

#The variables foo and bar are called metasyntactic variables, meaning that they are used as placeholder names in example code to demonstrate something.

#TAKING USER INPUT

#To get input from the user in Python, you can use the intuitively named input function.
#For example, a game can ask for the user's name and age as input and use them in the game.
#The input function prompts the user for input, and returns what they enter as a string (with the contents automatically escaped).
##x = input()
##print(x)

#You can provide a string to input() between the parentheses, producing a prompt message.
##name = input("Enter your name: ")
##print("Hello, " + name) 

#Let's assume we want to take the age of the user as input.
#We know that the input() function returns a string.
#To convert it to a number, we can use the int() function:
##age = int(input())
##print(age)  

#Similarly, in order to convert a number to a string, the str() function is used. This can be useful if you need to use a number in string concatenation.
age = 42
print("His age is " + str(age))  

#You can convert to float using the float() function. 
age = 42.5
print("His age is " + str(float(age)))

#You can use input() multiple times to take multiple user inputs.
#name = input()
#age = input()
#print(name + " is " + age)  

#IN-PLACE OPERATORS

#In-place operators allow you to write code like 'x = x + 3' more concisely, as 'x += 3'.
#The same thing is possible with other operators such as -, *, / and % as well. 
x = 2
print(x)
x += 3
print(x)

#These operators can be used on types other than numbers, as well, such as strings.
x = "spam"
print(x)
x += "eggs"
print(x)


#BOOLEANS AND COMPARISONS

#Another type in Python is the Boolean type. There are two Boolean values: True and False.
#They can be created by comparing values, for instance by using the equal operator ==
my_boolean = True
print(my_boolean)
#True
print(2 == 3)
#False
print("hello" == "hello")
#True

#Another comparison operator, the not equal operator (!=), evaluates to True if the items being compared aren't equal, and False if they are.
#Comparison operators are also called Relational operators.
print( 1 != 1 )
#False
print("eleven" != "seven")
#True
print(2 != 10)
#True

#Python also has operators that determine whether one number (float or integer) is greater than or smaller than another. These operators are > and < respectively.
print( 7 > 5 )
#True
print( 10 < 10 )
#False

#The greater than or equal to, and smaller than or equal to operators are >= and <=.
print(7 <= 8)
#True
print(9 >= 9.0)
#True

#Greater than and smaller than operators can also be used to compare strings lexicographically (the alphabetical order of words is based on the alphabetical order of their component letters).
print("Annie" > "Andy")
#True 

#IF STATEMENTS

#Python uses indentation (white space at the beginning of a line) to delimit blocks of code. Depending on program's logic, indentation can be mandatory. As you can see, the statements in the if should be indented.
#Notice the colon at the end of the expression in the if statement.
if 10 > 5:
   print("10 greater than 5")
print("Program ended")

#ELSE STATEMENTS

#The if statement allows you to check a condition and run some statements, if the condition is True.
#The else statement can be used to run some statements when the condition of the if statement is False.
x = 4
if x == 5:
   print("Yes")
else:
   print("No")

 #ELIF STATEMENTS
num = 3
if num == 1:
  print("One")
elif num == 2:
  print("Two")
elif num == 3: 
  print("Three")
else: 
  print("Something else")

#BOOLEAN LOGIC

#Python's Boolean operators are and, or, and not.
#The and operator takes two arguments, and evaluates as True if, and only if, both of its arguments are True. Otherwise, it evaluates to False. 
print( 1 == 1 and 2 == 2 )
#True
print( 1 == 1 and 2 == 3 )
#False
print( 1 != 1 and 2 == 2 )
#False
print( 2 < 1 and 3 >  6 )
#False

#The or operator also takes two arguments. It evaluates to True if either (or both) of its arguments are True, and False if both arguments are False.
print( 1 == 1 or 2 == 2 )
#True
print( 1 == 1 or 2 == 3 )
#True
print( 1 != 1 or 2 == 2 )
#True
print( 2 < 1 or 3 >  6 )
#False

#Unlike other operators we've seen so far, not only takes one argument, and inverts it.
#The result of not True is False, and not False goes to True.
print(not 1 == 1)
#False
print(not 1 > 7)
#True

#OPERATOR PRECEDENCE

#Operator precedence is a very important concept in programming. It is an extension of the mathematical idea of order of operations (multiplication being performed before addition, etc.) to include other operators, such as those in Boolean logic. 
#The below code shows that == has a higher precedence than or:
print( False == False or True )
#True
print( False == (False or True) )
#False
print( (False == False) or True )
#True

#You can chain multiple conditional statements in an if statement using the Boolean operators.
grade = 88
if (grade >= 70 and grade <=100):
    print("Passed!") 

#LISTS

#Lists are used to store items.
#A list is created using square brackets with commas separating items.
words = ["Hello", "world", "!"]  

#A certain item in the list can be accessed by using its index in square brackets.
words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2]) 

#An empty list is created with an empty pair of square brackets. 
empty_list = []
print(empty_list)

#Lists can also be nested within other lists. 
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

#Nested lists can be used to represent 2D grids, such as matrices. 
m = [
    [1, 2, 3],
    [4, 5, 6]
    ]
    
print(m[1][2])  

#Some types, such as strings, can be indexed like lists.
#Indexing strings behaves as though you are indexing a list containing each character in the string. 
str = "Hello world!"
print(str[6])

#The item at a certain index in a list can be reassigned.
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

#Lists can be added and multiplied in the same way as strings.
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

#To check if an item is in a list, the in operator can be used.
#It returns True if the item occurs one or more times in the list, and False if it doesn't. 
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

#To check if an item is not in a list, you can use the not operator in one of the following ways:
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#The append method adds an item to the end of an existing list. 
nums = [1, 2, 3]
nums.append(4)
print(nums)

#To get the number of items in a list, you can use the len function. 
nums = [1, 3, 5, 2, 4]
print(len(nums))

#The insert method is similar to append, except that it allows you to insert a new item at any position in the list, as opposed to just at the end.
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

#The index method finds the first occurrence of a list item and returns its index.
letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))

#max(list): Returns the list item with the maximum value
#min(list): Returns the list item with minimum value
#list.count(item): Returns a count of how many times an item occurs in a list
#list.remove(item): Removes an object from a list
#list.reverse(): Reverses items in a list.

#WHILE LOOPS

#A while loop is used to repeat a block of code multiple times.
#For example, let's say we need to process multiple user inputs, so that each time the user inputs something, the same block of code needs to execute.

#Below is a while loop containing a variable that counts up from 1 to 5, at which point the loop terminates. 
i = 1
while i <=5:
   print(i)
   i = i + 1
print("Finished!")

#You can use multiple statements in the while loop.
del str
x = 1
while x < 10:
	if x%2 == 0:
		print(str(x) + " is even")
	else:
		print(str(x) + " is odd")
	x += 1 

#To end a while loop prematurely, the break statement can be used. 
i = 0
while True:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break

print("Finished")

#Unlike break, continue jumps back to the top of the loop, rather than stopping it. Basically, the continue statement stops the current iteration and continues with the next one.
i = 1
while i<=5:
    print(i)
    i+=1
    if i==3:
      print("Skipping 3")
      continue

# FOR LOOPS

#The code below outputs each item in the list and adds an exclamation mark at the end:
words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")

#The for loop can be used to iterate over strings.
str = "testing for loops"
count = 0
for x in str:
  if(x == 't'):
    count += 1
print(count) 

#Similar to while loops, the break and continue statements can be used in for loops, to stop the loop or jump to the next iteration.
#The while loop is used in cases when the number of iterations is not known and depends on some calculations and conditions in the code block of the loop.
#For example, ending the loop when the user enters a specific input in a calculator program.
#Both, for and while loops can be used to achieve the same results, however, the for loop has cleaner and shorter syntax, making it a better choice in most cases.

#RANGE


#The range() function returns a sequence of numbers.
#By default, it starts from 0, increments by 1 and stops before the specified number.
#The code below generates a list containing all of the integers, up to 10.
numbers = list(range(10))
print(numbers)

#If range is called with one argument, it produces an object with values from 0 to that argument.
#If it is called with two arguments, it produces values from the first to the second.
numbers = list(range(3, 8))
print(numbers)
print(range(20) == range(0, 20))

#range can have a third argument, which determines the interval of the sequence produced, also called the step. 
numbers = list(range(5, 20, 2))
print(numbers)

#We can also create list of decreasing numbers, using a negative number as the third argument
numbers=list(range(20, 5, -2))
print(numbers)

#The for loop is commonly used to repeat some code a certain number of times. This is done by combining for loops with range objects.
for i in range(5):
  print("hello!")

#FUNCTIONS AND MODULES

#Yourself, or DRY, principle. We've already looked at one way of doing this: by using loops. In this module, we will explore two more: functions and modules.

#FUNCTIONS

#Any statement that consists of a word followed by information in parentheses is a function call.
#The words in front of the parentheses are function names, and the comma-separated values inside the parentheses are function arguments. 
del str
print("Hello world!")
range(2, 20)
str(12)
range(10, 20, 3)

#Here is an example of a function named my_func. It takes no arguments, and prints "spam" three times. It is defined, and then called. 
def my_func():
   print("spam")
   print("spam")
   print("spam")
my_func()

def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

#Function arguments can be used as variables inside the function definition. However, they cannot be referenced outside of the function's definition. This also applies to other variables created inside a function.
#Technically, parameters are the variables in a function definition, and arguments are the values put into parameters when functions are called.
def function(variable):
   variable += 1
   print(variable)
function(7)
#print(variable)

#
#Docstrings (documentation strings) serve a similar purpose to comments, as they are designed to explain code. However, they are more specific and have a different syntax. They are created by putting a multiline string containing an explanation of the function below the function's first line.
#Unlike conventional comments, docstrings are retained throughout the runtime of the program. This allows the programmer to inspect these comments at run time.
def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")
shout("spam")

#MODULES

#The basic way to use a module is to add import module_name at the top of your code, and then using module_name.var to access functions and values with the name var in the module.
#For example, the following example uses the random module to generate random numbers: 
# imports all objects from a module. For example: from math import. This is generally discouraged, as it confuses variables in your code with variables in the external module.

import random

for i in range(5):
   value = random.randint(1, 6)
   print(value)

#There is another kind of import that can be used if you only need certain functions from a module.
#These take the form from module_name import var, and then var can be used as if it were defined normally in your code. 
from math import pi

print(pi)

#You can import a module or object under a different name using the as keyword. This is mainly used when a module or object has a long or confusing name.
from math import sqrt as square_root
print(square_root(100))

#There are three main types of modules in Python, those you write yourself, those you install from external sources, and those that are preinstalled with Python.
#The last type is called the standard library, and contains many useful modules. Some of the standard library's useful modules include string, re, datetime, math, random, os, multiprocessing, subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.

#Tasks that can be done by the standard library include string parsing, data serialization, testing, debugging and manipulating dates, emails, command line arguments, and much more!

#Python's extensive standard library is one of its main strengths as a language.

#Some of the modules in the standard library are written in Python, and some are written in C.
#Most are available on all platforms, but some are Windows or Unix specific. 

#Many third-party Python modules are stored on the Python Package Index (PyPI).
#The best way to install these is using a program called pip. This comes installed by default with modern distributions of Python. If you don't have it, it is easy to install online. Once you have it, installing libraries from PyPI is easy. Look up the name of the library you want to install, go to the command line (for Windows it will be the Command Prompt), and enter pip install library_name. Once you've done this, import the library and use it in your code.

#Using pip is the standard way of installing libraries on most operating systems, but some libraries have prebuilt binaries for Windows. These are normal executable files that let you install libraries with a GUI the same way you would install other programs.


#EXCEPTIONS AND FILES


#to incorrect code or input. When an exception occurs, the program immediately stops.
#The following code produces the ZeroDivisionError exception by trying to divide 7 by 0. 

num1 = 7
num2 = 0
#print(num1/num2)

#Different exceptions are raised for different reasons.
#Common exceptions:
#ImportError: an import fails;
#IndexError: a list is indexed with an out-of-range number;
#NameError: an unknown variable is used;
#SyntaxError: the code can't be parsed properly;
#TypeError: a function is called on a value of an inappropriate type;
#ValueError: a function is called on a value of the correct type, but with an inappropriate value.

#Python has several other built-in exceptions, such as ZeroDivisionError and OSError. Third-party libraries also often define their own exceptions.

#To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
#The try block contains code that might throw an exception. If that exception occurs, the code in the try block stops being executed, and the code in the except block is run. If no error occurs, the code in the except block doesn't run.

try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")

#A try statement can have multiple different except blocks to handle different exceptions.
#Multiple exceptions can also be put into a single except block using parentheses, to have the except block handle all of them.
try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")

#An except statement without any exception specified will catch all errors. These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.
try:
   word = "spam"
   print(word / 0)
except:
   print("An error occurred")

#To ensure some code runs no matter what errors occur, you can use a finally statement. The finally statement is placed at the bottom of a try/except statement. Code within a finally statement always runs after execution of the code in the try, and possibly in the except, blocks.
try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")

#Code in a finally statement even runs if an uncaught exception occurs in one of the preceding blocks. 
try:
   print(1)
   print(10 / 0)
except ZeroDivisionError:
   ##print(unknown_var)
   x==1
finally:
	print("This is executed last")

#You can raise exceptions by using the raise statement. 
print(1)
##raise ValueError
print(2)

#Exceptions can be raised with arguments that give detail about them.
name = "123"
#raise NameError("Invalid name!")

#In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
try:
   ##num = 5 / 0
   num=1
except:
   print("An error occurred")
   raise

#An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program.
#An expression is tested, and if the result comes up false, an exception is raised.
#Assertions are carried out through use of the assert statement.
print(1)
assert 2 + 2 == 4
print(2)
##assert 1 + 1 == 3
print(3)

#The assert can take a second argument that is passed to the AssertionError raised if the assertion fails.
temp = -10
##assert (temp >= 0), "Colder than absolute zero!"


#OPENING FILES

#You can use Python to read and write the contents of files.
#Text files are the easiest to manipulate. Before a file can be edited, it must be opened, using the open function. 
#The argument of the open function is the path to the file. If the file is in the current working directory of the program, you can specify only its name.
myfile = open("filename.txt")

#You can specify the mode used to open a file by applying a second argument to the open function.
#Sending "r" means open in read mode, which is the default.
#Sending "w" means write mode, for rewriting the contents of a file.
#Sending "a" means append mode, for adding new content to the end of the file.
#Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

#Once a file has been opened and used, you should close it.
#This is done with the close method of the file object.
file = open("filename.txt", "w")
# do stuff to the file
file.close()

#The contents of a file that has been opened in text mode can be read using the read method. 
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

#To read only a certain amount of a file, you can provide a number as an argument to the read function. This determines the number of bytes that should be read.
#You can make more calls to read on the same file object to read more of the file byte by byte. With no argument, read returns the rest of the file. 
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

#Afer all contents in a file have been read, any attempts to read further from that file will return an empty string, because you are trying to read from the end of the file.

#To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.
file = open("filename.txt", "r")
print(file.readlines())
file.close()
['Line 1 text \n', 'Line 2 text \n', 'Line 3 text']

#You can also use a for loop to iterate through the lines in the file: 
#In the output, the lines are separated by blank lines, as the print function automatically adds a new line at the end of its output.
#The "w" mode will create a file, if it does not already exist.
file = open("filename.txt", "r")
for line in file:
    print(line)
file.close() 

#To write to files you use the write method, which writes a string to the file.
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

#When a file is opened in write mode, the file's existing content is deleted.

#The write method returns the number of bytes written to a file, if successful.
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

#It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. One way of doing this is to use try and finally.
#This ensures that the file is always closed, even if an error occurs.
try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()

#An alternative way of doing this is using with statements. This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement. 
#The file is automatically closed at the end of the with statement, even if exceptions occur within it.
with open("filename.txt") as f:
   print(f.read())

#MORE TYPES

#The None object is used to represent the absence of a value.
#It is similar to null in other programming languages.
#Like other "empty" values, such as 0, [] and the empty string, it is False when converted to a Boolean variable.
#When entered at the Python console, it is displayed as the empty string.
None == None
#True
#None
print(None)
#None

#The None object is returned by any function that doesn't explicitly return anything else.
def some_func():
  print("Hi!")
var = some_func()
print(var)

#Dictionaries are data structures used to map arbitrary keys to values.
#Lists can be thought of as dictionaries with integer keys within a certain range.
#Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

#Trying to index a key that isn't part of the dictionary returns a KeyError.
primary = {
  "red": [255, 0, 0], 
  "green": [0, 255, 0], 
  "blue": [0, 0, 255], 
  "mike":["one","two","three"],
}
print(primary["red"])
print(primary["mike"])
#print(primary["yellow"])

#Just like lists, dictionary keys can be assigned to different values.
#However, unlike lists, a new dictionary key can also be assigned a value, not just ones that already exist.
squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)

primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])

#To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

#A useful dictionary method is get. It does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead ('None', by default).
pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  None: "True",
}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

#Tuples are very similar to lists, except that they are immutable (they cannot be changed).
#Also, they are created using parentheses, rather than square brackets.
words = ("spam", "eggs", "sausages",)
print(words[0])
#words[1] = "cheese"

#List slices provide a more advanced way of retrieving values from a list. Basic list slicing involves indexing a list with two colon-separated integers. This returns a new list containing all the values in the old list between the indices.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

#If the first number in a slice is omitted, it is taken to be the start of the list.
#If the second number is omitted, it is taken to be the end.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

#List slices can also have a third number, representing the step, to include only alternate values in the slice.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

#Negative values can be used in list slicing (and normal list indexing). When negative values are used for the first and second values in a slice (or a normal index), they count from the end of the list.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

#List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
#List comprehensions are inspired by set-builder notation in mathematics.
cubes = [i**3 for i in range(5)]
print(cubes)

#A list comprehension can also contain an if statement to enforce a condition on values in the list.
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

a=[i for i in range(20) if i%3==0]
print(a)

#Fill in the blanks to create a list of numbers multiplied by 10 in the range of 5 to 9.
#a = [x*10 ___ x __ range(_, 9)]
a = [x*10 for x in range(5, 9)]
print(a)

#So far, to combine strings and non-strings, you've converted the non-strings to strings and added them.
#String formatting provides a more powerful way to embed non-strings within strings. String formatting uses a string's format method to substitute a number of arguments in the string.
#Each argument of the format function is placed in the string at the corresponding position, which is determined using the curly braces { }.
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

#String formatting can also be done with named arguments.
a = "{x}, {y}".format(x=5, y=12)
print(a)

#Python contains many useful built-in functions and methods to accomplish common tasks.
#join - joins a list of strings with another string as a separator.
print(", ".join(["spam", "eggs", "ham"]))

#replace - replaces one substring in a string with another.
print("Hello ME".replace("ME", "world"))

#startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence."))

#To change the case of a string, you can use lower and upper.
print("This is a sentence.".upper())
print("AN ALL CAPS SENTENCE".lower())

#The method split is the opposite of join, turning a string with a certain separator into a list.
print("spam, eggs, ham".split(", "))

#To find the maximum or minimum of some numbers or a list, you can use max or min.
#To find the distance of a number from zero (its absolute value), use abs.
#To round a number to a certain number of decimal places, use round.
#To find the total of a list, use sum.
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

a=min([sum([11, 22]), max(abs(-30), 2)])

#Often used in conditional statements, all and any take a list as an argument, and return True if all or any (respectively) of their arguments evaluate to True (and False otherwise).
#The function enumerate can be used to iterate through the values and indices of a list simultaneously.
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for v in enumerate(nums):
   print(v)






"""
#This is an example project, showing a program that analyzes a sample file to find what percentage of the text each character occupies.
#This section shows how a file could be open and read.
filename = input("Enter a filename: ")
with open(filename) as f:
   text = f.read()
print(text)

#This part of the program shows a function that counts how many times a character occurs in a string.
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

#This function takes as its arguments the text of the file and one character, returning the number of times that character appears in the text.
#Now we can call it for our file.
filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

print(count_char(text, "r"))

#The next part of the program finds what percentage of the text each character of the alphabet occupies.
for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))
  """

#FUNCTIONAL PROGRAMMING


#Functional programming is a style of programming that (as the name suggests) is based around functions.
#A key part of functional programming is higher-order functions. We have seen this idea briefly in the previous lesson on functions as objects. Higher-order functions take other functions as arguments, or return them as results.
def apply_twice(func, arg):
   return func(func(arg))

def add_five(x):
   return x + 5

print(apply_twice(add_five, 10))

#Functional programming seeks to use pure functions. Pure functions have no side effects, and return a value that depends only on their arguments.
#This is how functions in math work: for example, The cos(x) will, for the same value of x, always return the same result.
#Below are examples of pure and impure functions.
#Pure Function
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

#Impure Function
some_list = []

def impure(arg):
  some_list.append(arg)

#Using pure functions has both advantages and disadvantages.
#Pure functions are:
#- easier to reason about and test.
#- more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
#
#The main disadvantage of using only pure functions is that they majorly complicate the otherwise simple task of I/O, since this appears to inherently require side effects.
#They can also be more difficult to write in some situations.

#Creating a function normally (using def) assigns it to a variable automatically.
#This is different from the creation of other objects - such as strings and integers - which can be created on the fly, without assigning them to a variable.
#The same is possible with functions, provided that they are created using lambda syntax. Functions created this way are known as anonymous.
#This approach is most commonly used when passing a simple function as an argument to another function. The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, a colon, and the expression to evaluate and return.
def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)

#Lambda functions aren't as powerful as named functions.
#They can only do things that require a single expression - usually equivalent to a single line of code.
#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

#Fill in the blanks to create a lambda function that returns the square of its argument, and call it for the number 8.
a = (lambda x: x*x) (8)
print(a)

#Lambda functions can be assigned to variables, and used like normal functions.
double = lambda x: x * 2
print(double(7))


#MAP AND FILTER


#The built-in functions map and filter are very useful higher-order functions that operate on lists (or similar objects called iterables).
#The function map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument.
def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

#The function filter filters an iterable by removing items that don't match a predicate (a function that returns a Boolean).
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

#Generators are a type of iterable, like lists or tuples.
#Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
#They can be created using functions and the yield statement.
#The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.
def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1
    
for i in countdown():
  print(i)

#Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists.
#In fact, they can be infinite!
def infinite_sevens():
  while True:
    yield 7
        
##for i in infinite_sevens():
##  print(i)

#Finite generators can be converted into lists by passing them as arguments to the list function.
#Using generators results in improved performance, which is the result of the lazy (on demand) generation of values, which translates to lower memory usage. Furthermore, we do not need to wait until all the elements have been generated before we start to use them.
def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))

#Decorators provide a way to modify functions using other functions.
#This is ideal when you need to extend the functionality of functions that you don't want to modify.
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()
#We defined a function named decor that has a single parameter func. Inside decor, we defined a nested function named wrap. The wrap function will print a string, then call func(), and print another string. The decor function returns the wrap function as its result.
#We could say that the variable decorated is a decorated version of print_text - it's print_text plus something.
#In fact, if we wrote a useful decorator we might want to replace print_text with the decorated version altogether so we always got our "plus something" version of print_text.
#This is done by re-assigning the variable that contains our function:
print_text = decor(print_text)
print_text()

#In our previous example, we decorated our function by replacing the variable containing the function with a wrapped version.
def print_text():
  print("Hello world!")

print_text = decor(print_text)
#This pattern can be used at any time, to wrap any function.
#Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
#If we are defining a function we can "decorate" it with the @ symbol like:
#A single function can have multiple decorators.
@decor
def print_text():
  print("Hello world!")

#Recursion is a very important concept in functional programming.
#The fundamental part of recursion is self-reference - functions calling themselves. It is used to solve problems that can be broken up into easier sub-problems of the same type.
#A classic example of a function that is implemented recursively is the factorial function, which finds the product of all positive integers below a specified number.
#For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!.
#Furthermore, 1! = 1. This is known as the base case, as it can be calculated without performing any more factorials.
def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)
    
print(factorial(5))

#Recursive functions can be infinite, just like infinite while loops. These often occur when you forget to implement the base case.
#Below is an incorrect version of the factorial function. It has no base case, so it runs until the interpreter runs out of memory and crashes.
def factorial(x):
  return x * factorial(x-1)
    
##print(factorial(5))

#Recursion can also be indirect. One function can call a second, which calls the first, which calls the second, and so on. This can occur with any number of functions.
def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)


print(is_odd(17))
print(is_even(23))
#What is the result of this code?
def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))

#Sets are data structures, similar to lists or dictionaries. They are created using curly braces, or the set function. They share some functionality with lists, such as the use of in to check whether they contain a particular item.
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)


#What is the output of this code?
letters = {"a", "b", "c", "d"}
if "e" not in letters:
  print(1)
else: 
  print(2)

#Sets differ from lists in several ways, but share several list operations such as len.
#They are unordered, which means that they can't be indexed.
#They cannot contain duplicate elements.
#Due to the way they're stored, it's faster to check whether an item is part of a set, rather than part of a list.
#Instead of using append to add to a set, use add.
#The method remove removes a specific element from a set; pop removes an arbitrary element.
#Basic uses of sets include membership testing and the elimination of duplicate entries.
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

#Sets can be combined using mathematical operations.
#The union operator | combines two sets to form a new one containing items in either.
#The intersection operator & gets items only in both.
#The difference operator - gets items in the first set but not in the second.
#The symmetric difference operator ^ gets items in either set, but not both.
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

"""
As we have seen in the previous lessons, Python supports the following data structures: lists, dictionaries, tuples, sets.

When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot change.

Many times, a tuple is used in combination with a dictionary, for example, a tuple might represent a key, because it's immutable.
"""

#The module itertools is a standard library that contains several functions that are useful in functional programming.
#One type of function it produces is infinite iterators.
#The function count counts up infinitely from a value.
#The function cycle infinitely iterates through an iterable (for instance a list or string).
#The function repeat repeats an object, either infinitely or a specific number of times.
from itertools import count
for i in count(3):
  print(i)
  if i >=11:
    break

#There are many functions in itertools that operate on iterables, in a similar way to map and filter.
#Some examples:
#takewhile - takes items from an iterable while a predicate function remains true;
#chain - combines several iterables into one long one;
#accumulate - returns a running total of values in an iterable.
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

#There are also several combinatoric functions in itertool, such as product and permutation.
#These are used when you want to accomplish a task with all possible combinations of some items.
from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters))) 

from itertools import product
a={1, 2}
print(len(list(product(range(3), a))))



#Fill in the blanks to calculate the expression x*(x+1) using an anonymous function and call it for the number 6.

a = (lambda x: x*(x+1))(6)
print(a)

#6,1,2


#Fill in the blanks to leave only even numbers in the list.
#6,6,1
nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x%2==0, nums))
print(res)


#OBJECT_ORIENTED PROGRAMMING

"""
We have previously looked at two paradigms of programming - imperative (using statements, loops, and functions as subroutines), and functional (using pure functions, higher-order functions, and recursion).

Another very popular paradigm is object-oriented programming (OOP).
Objects are created using classes, which are actually the focal point of OOP.
The class describes what the object will be, but is separate from the object itself. In other words, a class can be described as an object's blueprint, description, or definition.
You can use the same class as a blueprint for creating multiple different objects.

Classes are created using the keyword class and an indented block, which contains class methods (which are functions).
"""
#This code defines a class named Cat, which has two attributes: color and legs.
#Then the class is used to create 3 separate objects of that class.
class Cat:
  def __init__(self, color, legs): # called when an instance (object) of the class is created.
    self.color = color             #init__ method is called the class constructor.
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

#The __init__ method is the most important method in a class.
#This is called when an instance (object) of the class is created, using the class name as a function.

#All methods must have self as their first parameter, although it isn't explicitly passed, Python adds the self argument to the list for you; you do not need to include it when you call the methods. Within a method definition, self refers to the instance calling the method.

#Instances of a class have attributes, which are pieces of data associated with them.
#In this example, Cat instances have attributes color and legs. These can be accessed by putting a dot, and the attribute name after an instance.
#In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.
#the __init__ method takes two arguments and assigns them to the object's attributes. The __init__ method is called the class constructor.
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)

#Classes can have other methods defined to add functionality to them.
#Remember, that all methods must have self as their first parameter.
#These methods are accessed using the same dot syntax as attributes.
class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self): #Classes can have other methods defined to add functionality to them.
    print("Woof!")

  def test(self):
    if self.name=="Fido":
      print("yep")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark() #These methods are accessed using the same dot syntax as attributes.
fido.test()

#Classes can also have class attributes, created by assigning variables within the body of the class. 
#These can be accessed either from instances of the class, or the class itself.
#Class attributes are shared by all instances of the class.
class Dog:
  legs = 4  #Classes can also have class attributes, created by assigning variables within the body of the class. 
            #Class attributes are shared by all instances of the class.
  def __init__(self, name, color):
    self.name = name
    self.color = color


fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)

class clInput:
  def __init__(self,Name,Description,Current_Value,Last_Change):
    self.Name=Name
    self.Description=Description
    self.Current_Value=Current_Value
    self.Last_Change=Last_Change

  def stable(self):
      if self.Current_Value==22:
        return True
      else:
        return False

AI22=clInput("AnalogInput22","Analog Input 22",22,23)
print(AI22.Description)
print(AI22.stable())

#Trying to access an attribute of an instance that isn't defined causes an AttributeError. 
#This also applies when you call an undefined method.
class Rectangle: 
  def __init__(self, width, height):
    self.width = width
    self.height = height

rect = Rectangle(7, 8)
##print(rect.color)

#Inheritance provides a way to share functionality between classes.
#Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ in some ways (only Dog might have the method bark), they are likely to be similar in others (all having the attributes color and name).
#This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality.
#To inherit a class from another class, put the superclass name in parentheses after the class name.
class Animal: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):  #Inheritance provides a way to share functionality between classes.
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

#A class that inherits from another class is called a subclass.
#A class that is inherited from is called a superclass.
#If a class inherits from another with the same attributes or methods, it overrides them.
class Wolf: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Grr...")

class Dog(Wolf):
  def bark(self): #If a class inherits from another with the same attributes or methods, it overrides them.
    print("Woof")
        
husky = Dog("Max", "grey")
husky.bark()

#Inheritance can also be indirect. One class can inherit from another, and that class can inherit from a third class.
class A:
  def method(self):
    print("A method")
    
class B(A):
  def another_method(self):
    print("B method")
    
class C(B): #Inheritance can also be indirect. One class can inherit from another, and that class can inherit from a third class.
  def third_method(self):
    print("C method")
    
c = C()
c.method()
c.another_method()
c.third_method()

#The function super is a useful inheritance-related function that refers to the parent class. It can be used to find the method with a certain name in an object's superclass.
#super().spam() calls the spam method of the superclass.
class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()  #The function super is a useful inheritance-related function that refers to the parent class. 
                    # Runs the method "spam" on the superclass
B().spam()

#Magic methods are special methods which have double underscores at the beginning and end of their names.
#They are also known as dunders.
#So far, the only one we have encountered is __init__, but there are several others.
#They are used to create functionality that can't be represented as a normal method.

#One common use of them is operator overloading.
#This means defining operators for custom classes that allow operators such as + and * to be used on them.
#An example magic method is __add__ for +.

#The __add__ method allows for the definition of a custom behavior for the + operator in our class.
#As you can see, it adds the corresponding attributes of the objects and returns a new object, containing the result.
#Once it's defined, we can add two objects of the class together.
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

"""
More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

The expression x + y is translated into x.__add__(y).
However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
There are equivalent r methods for all magic methods just mentioned.
"""
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

"""
Python also provides magic methods for comparisons.
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__.
There are no other relationships between the other operators.
"""
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

"""
There are several magic methods for making classes act like containers.
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, and __int__, __str__, and the like, for converting objects to built-in types.

We have overridden the len() function for the class VagueList to return a random number.
The indexing function also returns a random item in a range from the list, based on the expression.
"""
import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

"""
The lifecycle of an object is made up of its creation, manipulation, and destruction.

The first stage of the life-cycle of an object is the definition of the class to which it belongs.
The next stage is the instantiation of an instance, when __init__ is called. Memory is allocated to store the instance. Just before this occurs, the __new__ method of the class is called. This is usually overridden only in special cases.
After this has happened, the object is ready to be used.

Other code can then interact with the object, by calling functions on it and accessing its attributes.
Eventually, it will finish being used, and can be destroyed.

purposes.
Destruction of an object occurs when its reference count reaches zero. Reference count is the number of variables and other elements that refer to an object.
If nothing is referring to it (it has a reference count of zero) nothing can interact with it, so it can be safely deleted.

In some situations, two (or more) objects can be referred to by each other only, and therefore can be deleted as well.
The del statement reduces the reference count of an object by one, and this often leads to its deletion.
The magic method for the del statement is __del__.
The process of deleting objects when they are no longer needed is called garbage collection.
In summary, an object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary). The object's reference count decreases when it's deleted with del, its reference is reassigned, or its reference goes out of scope. When an object's reference count reaches zero, Python automatically deletes it.
"""
a = 42  # Create object <42>
b = a  # Increase ref. count  of <42> 
c = [a]  # Increase ref. count  of <42> 

del a  # Decrease ref. count  of <42>
b = 100  # Decrease ref. count  of <42> 
c[0] = -1  # Decrease ref. count  of <42>

"""
A key part of object-oriented programming is encapsulation, which involves packaging of related variables and functions into a single easy-to-use object - an instance of a class.
A related concept is data hiding, which states that implementation details of a class should be hidden, and a clean standard interface be presented for those who want to use the class.
In other programming languages, this is usually done with private methods and attributes, which block external access to certain methods and attributes in a class.

The Python philosophy is slightly different. It is often stated as "we are all consenting adults here", meaning that you shouldn't put arbitrary restrictions on accessing parts of a class. Hence there are no ways of enforcing a method or attribute be strictly private.

However, there are ways to discourage people from accessing parts of a class, such as by denoting that it is an implementation detail, and should be used at their own risk.
"""

"""
Weakly private methods and attributes have a single underscore at the beginning.
This signals that they are private, and shouldn't be used by external code. However, it is mostly only a convention, and does not stop external code from accessing them.
Its only actual effect is that from module_name import * won't import variables that start with a single underscore.

The attribute _hiddenlist is marked as private, but it can still be accessed in the outside code.
The __repr__ magic method is used for string representation of the instance.
"""
class Queue:
  def __init__(self, contents):
    self._hiddenlist = list(contents)

  def push(self, value):
    self._hiddenlist.insert(0, value)
   
  def pop(self):
    return self._hiddenlist.pop(-1)

  def __repr__(self):
    return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

"""
Strongly private methods and attributes have a double underscore at the beginning of their names. This causes their names to be mangled, which means that they can't be accessed from outside the class.
The purpose of this isn't to ensure that they are kept private, but to avoid bugs if there are subclasses that have methods or attributes with the same names.
Name mangled methods can still be accessed externally, but by a different name. The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.

Basically, Python protects those members by internally changing the name to include the class name.
"""
class Spam:
  __egg = 7
  def print_egg(self):
    print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
##print(s.__egg)

"""Methods of objects we've looked at so far are called by an instance of a class, which is then passed to the self parameter of the method.
Class methods are different - they are called by a class, which is passed to the cls parameter of the method.
A common use of these are factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor.
Class methods are marked with a classmethod decorator.

Technically, the parameters self and cls are just conventions; they could be changed to anything else. However, they are universally followed, so it is wise to stick to using them.
"""
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

"""
Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to normal functions that belong to a class.
They are marked with the staticmethod decorator.

Static methods behave like plain functions, except for the fact that you can call them from an instance of the class.
"""
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients) 
print(pizza.toppings)

"""
Properties provide a way of customizing access to instance attributes.
They are created by putting the property decorator above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead.
One common use of a property is to make an attribute read-only.
"""
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    
  @property
  def pineapple_allowed(self):
    return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
##pizza.pineapple_allowed = True

"""
Properties can also be set by defining setter/getter functions.
The setter function sets the corresponding property's value.
The getter gets the value.
To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.
The same applies to defining getter functions.
"""
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Sw0rdf1sh!":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
##pizza.pineapple_allowed = True
##print(pizza.pineapple_allowed)

"""Object-orientation is very useful when managing different objects and their relations. That is especially useful when you are developing games with different characters and features.

Let's look at an example project that shows how classes are used in game development.
The game to be developed is an old fashioned text-based adventure game.
Below is the function handling input and simple parsing.

The code above takes input from the user, and tries to match the first word with a command in verb_dict. If a match is found, the corresponding function is called.
"""
def get_input():
  command = input(": ").split()
  verb_word = command[0]
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))

def say(noun):
  return 'You said "{}"'.format(noun)

verb_dict = {
  "say": say,
}

##while True:
  ##get_input()

#The next step is to use classes to represent game objects.
class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject):
  class_name = "goblin"
  desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

#We created a Goblin class, which inherits from the GameObjects class.
#We also created a new function examine, which returns the objects description.
#Now we can add a new "examine" verb to our dictionary and try it out!
verb_dict = {
  "say": say,
  "examine": examine,
}

#Combine this code with the one in our previous example, and run the program.


#This code adds more detail to the Goblin class and allows you to fight goblins.
#This was just a simple sample.
#You could create different classes (e.g., elves, orcs, humans), fight them, make them fight each other, and so on.
class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
    self._desc = " A foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else: 
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun) 
  return msg


#REGULAR EXPERSSIONS

"""
Regular expressions are a powerful tool for various kinds of string manipulation.
They are a domain specific language (DSL) that is present as a library in most modern programming languages, not just Python.
They are useful for two main tasks:
- verifying that strings match a pattern (for instance, that a string has the format of an email address),
- performing substitutions in a string (such as changing all American spellings to British ones).

Regular expressions in Python can be accessed using the re module, which is part of the standard library.
After you've defined a regular expression, the re.match function can be used to determine whether it matches at the beginning of a string.
If it does, match returns an object representing the match, if not, it returns None.
To avoid any confusion while working with regular expressions, we would use raw strings as r"expression".
Raw strings don't escape anything, which makes use of regular expressions easier.
"""
import re

pattern = r"spamspam"

if re.match(pattern, "spamspamspam"):
   print("Match")
else:
   print("No match")

"""
Other functions to match patterns are re.search and re.findall.
The function re.search finds a match of a pattern anywhere in the string.
The function re.findall returns a list of all substrings that match a pattern.

the match function did not match the pattern, as it looks at the beginning of the string.
The search function found a match in the string.

The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.
"""
import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
   print("re.match is a Match")
else:
   print("re.match is No match")

if re.search(pattern, "eggspamsausagespam"):
   print("re.search is a Match")
else:
   print("re.search is No match")
    
print(re.findall(pattern, "eggspamsausagespam"))


#The regex search returns an object with several methods that give details about it.
#These methods include group which returns the string matched, start and end which return the start and ending positions of the first match, and span which returns the start and end positions of the first match as a tuple.
import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end())
   print(match.span())

#One of the most important re methods that use regular expressions is sub.
#re.sub(pattern, repl, string, count=0)
#This method replaces all occurrences of the pattern in string with repl, substituting all occurrences, unless count provided. This method returns the modified string.
import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)


#Metacharacters are what make regular expressions more powerful than normal string methods.
#They allow you to create regular expressions to represent concepts like "one or more repetitions of a vowel".

#The existence of metacharacters poses a problem if you want to create a regular expression (or regex) that matches a literal metacharacter, such as "$". You can do this by escaping the metacharacters by putting a backslash in front of them.
#However, this can cause problems, since backslashes also have an escaping function in normal Python strings. This can mean putting three or four backslashes in a row to do all the escaping.
#To avoid this, you can use a raw string, which is a normal string with an "r" in front of it. We saw usage of raw strings in the previous lesson.

#The first metacharacter we will look at is . (dot).
#This matches any character, other than a new line.
import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "blue"):
   print("Match 3")

#The next two metacharacters are ^ and $.
#These match the start and end of a string, respectively.
import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   print("Match 3")

#Character classes provide a way to match only one of a specific set of characters.
#A character class is created by putting the characters it matches inside square brackets.
#The pattern [aeiou] in the search function matches all strings that contain any one of the characters defined.
import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
   print("Match 1")

if re.search(pattern, "qwertyuiop"):
   print("Match 2")

if re.search(pattern, "rhythm myths"):
   print("Match 3")

#Character classes can also match ranges of characters.
#Some examples:
#The class [a-z] matches any lowercase alphabetic character.
#The class [G-P] matches any uppercase character from G to P.
#The class [0-9] matches any digit.
#Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.
import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
   print("Match 1")

if re.search(pattern, "E3"):
   print("Match 2")

if re.search(pattern, "1ab"):
   print("Match 3")

#Place a ^ at the start of a character class to invert it.
#This causes it to match any character other than the ones included.
#Other metacharacters such as $ and ., have no meaning within character classes.
#The metacharacter ^ has no meaning unless it is the first character in a class.
import re

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
   print("Match 1")

if re.search(pattern, "AbCdEfG123"):
   print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
   print("Match 3")

#Some more metacharacters are *, +, ?, { and }.
#These specify numbers of repetitions.
#The metacharacter * means "zero or more repetitions of the previous thing". It tries to match as many repetitions as possible. The "previous thing" can be a single character, a class, or a group of characters in parentheses.
#matches strings that start with "egg" and follow with zero or more "spam"s.
import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")

#The metacharacter + is very similar to *, except it means "one or more repetitions", as opposed to "zero or more repetitions".
import re

pattern = r"g+"

if re.match(pattern, "g"):
   print("Match 1")

if re.match(pattern, "gggggggggggggg"):
   print("Match 2")

if re.match(pattern, "abc"):
   print("Match 3")

#The metacharacter ? means "zero or one repetitions".
import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
   print("Match 1")

if re.match(pattern, "icecream"):
   print("Match 2")

if re.match(pattern, "sausages"):
   print("Match 3")

if re.match(pattern, "ice--ice"):
   print("Match 4")

#Curly braces can be used to represent the number of repetitions between two numbers.
#The regex {x,y} means "between x and y repetitions of something".
#Hence {0,1} is the same thing as ?.
#f the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.
#matches string that have 1 to 3 nines.
import re

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")

#A group can be created by surrounding part of a regular expression with parentheses.
#This means that a group can be given as an argument to metacharacters such as * and ?

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")

#The content of groups in a match can be accessed using the group function.
#A call of group(0) or group() returns the whole match.
#A call of group(n), where n is greater than 0, returns the nth group from the left.
#The method groups() returns all groups up from 1.
import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())

#There are several kinds of special groups.
#Two useful ones are named groups and non-capturing groups.
#Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
#Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an existing regular expression without breaking the numbering.
import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())

#Another important metacharacter is |.
#This means "or", so red|blue matches either "red" or "blue".
import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
   print ("Match 1")

match = re.match(pattern, "grey")
if match:
   print ("Match 2")    

match = re.match(pattern, "griy")
if match:
    print ("Match 3")

#There are various special sequences you can use in regular expressions. They are written as a backslash followed by another character.
#One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17. This matches the expression of the group of that number.
#Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the first group's subexpression, which is the matched expression itself, and not the regex pattern.
import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
   print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2")    

match = re.match(pattern, "abc cde")
if match:
   print ("Match 3")


pattern=r"(abc|xyz)\1"
match = re.match(pattern, "xyzxyzxyzxyzxyzxyzxyzxyz")
if match:
   print ("Test Matched This Time")
   print(match.groups())


#More useful special sequences are \d, \s, and \w.
#These match digits, whitespace, and word characters respectively.
#In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
#In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
#Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.
#(\D+\d) matches one or more non-digits followed by a digit.
import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")

if match:
   print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
   print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")


#Additional special sequences are \A, \Z, and \b.
#The sequences \A and \Z match the beginning and end of a string, respectively.
#The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
#The sequence \B matches the empty string anywhere else.
#"\b(cat)\b" basically matches the word "cat" surrounded by word boundaries.
import re

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
   print ("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
   print ("Match 2")

match = re.search(pattern, "We scattered.")
if match:
   print ("Match 3")

#To demonstrate a sample usage of regular expressions, lets create a program to extract email addresses from a string.
#Suppose we have a text that contains an email address:
str = "Please contact info@sololearn.com for assistance"
#Our goal is to extract the substring "info@sololearn.com".
#A basic email address consists of a word and may include dots or dashes. This is followed by the @ sign and the domain name (the name, a dot, and the domain name suffix).
#This is the basis for building our regular expression.
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
#[\w\.-]+ matches one or more word character, dot or dash.
#The regex above says that the string should contain a word (with dots and dashes allowed), followed by the @ sign, then another similar word, then a dot and another word.
#Our regex contains three groups:
#1 - first part of the email address.
#2 - domain name without the suffix.
#3 - the domain suffix.
#Putting it all together:
#In case the string contains multiple email addresses, we could use the re.findall method instead of re.search, to extract all email addresses.
import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
   print(match.group())


#PYTHONICNESS $ PACKAGING


import this

"""
Result:
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

Some lines in the Zen of Python may need more explanation.
Explicit is better than implicit: It is best to spell out exactly what your code is doing. This is why adding a numeric string to an integer requires explicit conversion, rather than having it happen behind the scenes, as it does in other languages.
Flat is better than nested: Heavily nested structures (lists of lists, of lists, and on and on…) should be avoided.
Errors should never pass silently: In general, when an error occurs, you should output some sort of error message, rather than ignoring it.

There are 20 principles in the Zen of Python, but only 19 lines of text.
The 20th principle is a matter of opinion, but our interpretation is that the blank line means "Use whitespace".

PEP

Python Enhancement Proposals (PEP) are suggestions for improvements to the language, made by experienced Python developers.
PEP 8 is a style guide on the subject of writing readable code. It contains a number of guidelines in reference to variable names, which are summarized here:
- modules should have short, all-lowercase names;
- class names should be in the CapWords style;
- most variables and function names should be lowercase_with_underscores;
- constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
- names that would clash with Python keywords (such as 'class' or 'if') should have a trailing underscore.

PEP 8 also recommends using spaces around operators and after commas to increase readability.

Other PEP 8 suggestions include the following:
- lines shouldn't be longer than 80 characters;
- 'from module import *' should be avoided;
- there should only be one statement per line.

It also suggests that you use spaces, rather than tabs, to indent. However, to some extent, this is a matter of personal preference. If you use spaces, only use 4 per line. It's more important to choose one and stick to it.

The most important advice in the PEP is to ignore it when it makes sense to do so. Don't bother with following PEP suggestions when it would cause your code to be less readable; inconsistent with the surrounding code; or not backwards compatible.
However, by and large, following PEP 8 will greatly enhance the quality of your code.
"""

#Python allows to have function with varying number of arguments.
#Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple args in the body of the function.
def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5)

#Named parameters to a function can be made optional by giving them a default value.
#These must come after named parameters without a default value.
#In case the argument is passed in, the default value is ignored.
#If the argument is not passed in, the default value is used.
def function(x, y, food="spam"):
   print(food)

function(1, 2)
function(3, 4, "egg")

#**kwargs (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.
#The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.
def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

#Tuple unpacking allows you to assign each item in an iterable (often a tuple) to a variable.
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

#A variable that is prefaced with an asterisk (*) takes all values from the iterable that are left over from the other variables.
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

#Conditional expressions provide the functionality of if statements while using less code. They shouldn't be overused, as they can easily reduce readability, but they are often useful when assigning variables.
#Conditional expressions are also known as applications of the ternary operator.
#The ternary operator is so called because, unlike most operators, it takes three arguments.
a = 7
b = 1 if a >= 5 else 42
print(b)

status  = 1
msg = "Logout" if status == 1 else "Login"

#The else statement is most commonly used along with the if statement, but it can also follow a for or while loop, which gives it a different meaning.
#With the for or while loop, the code within it is called if the loop finishes normally (when a break statement does not cause an exit from the loop).
#The first for loop executes normally, resulting in the printing of "Unbroken 1".
#The second loop exits due to a break, which is why it's else statement is not executed.
for i in range(10):
   if i == 999:
      break
else:
   print("Unbroken 1")

for i in range(10):
   if i == 5:
      break
else: 
   print("Unbroken 2")

#The else statement can also be used with try/except statements.
#In this case, the code within it is only executed if no error occurs in the try statement.
try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)

#Most Python code is either a module to be imported, or a script that does something.
#However, sometimes it is useful to make a file that can be both imported as a module and run as a script.
#To do this, place script code inside if __name__ == "__main__".
#This ensures that it won't be run if the file is imported.
#When the Python interpreter reads a source file, it executes all of the code it finds in the file. Before executing the code, it defines a few special variables.
#For example, if the Python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.
def function():
   print("This is a module function")

if __name__=="__main__":
   print("This is a script")  
"""
If we save the code from our previous example as a file called sololearn.py, we can then import it to another script as a module, using the name sololearn.
sololearn.py
Basically, we've created a custom module called sololearn, and then used it in another script.
"""
##import sololearn
##sololearn.function()

"""
Major 3rd-Party Libraries

The Python standard library alone contains extensive functionality.
However, some tasks require the use of third-party libraries. Some major third-party libraries:
Django: The most frequently used web framework written in Python, Django powers websites that include Instagram and Disqus. It has many useful features, and whatever features it lacks are covered by extension packages.
CherryPy and Flask are also popular web frameworks.

For scraping data from websites, the library BeautifulSoup is very useful, and leads to better results than building your own scraper with regular expressions.
While Python does offer modules for programmatically accessing websites, such as urllib, they are quite cumbersome to use. Third-party library requests make it much easier to use HTTP requests.

A number of third-party modules are available that make it much easier to carry out scientific and mathematical computing with Python.
The module matplotlib allows you to create graphs based on data in Python.
The module NumPy allows for the use of multidimensional arrays that are much faster than the native Python solution of nested lists. It also contains functions to perform mathematical operations such as matrix transformations on the arrays.
The library SciPy contains numerous extensions to the functionality of NumPy.

Python can also be used for game development.
Usually, it is used as a scripting language for games written in other languages, but it can be used to make games by itself.
For 3D games, the library Panda3D can be used. For 2D games, you can use pygame.
"""

"""
Packaging

In Python, the term packaging refers to putting modules you have written in a standard format, so that other programmers can install and use them with ease.
This involves use of the modules setuptools and distutils.
The first step in packaging is to organize existing files correctly. Place all of the files you want to put in a library in the same parent directory. This directory should also contain a file called __init__.py, which can be blank but must be present in the directory.
This directory goes into another directory containing the readme and license, as well as an important file called setup.py.

SoloLearn/
   LICENSE.txt
   README.txt
   setup.py
   sololearn/
      __init__.py
      sololearn.py
      sololearn2.py

The next step in packaging is to write the setup.py file.
This contains information necessary to assemble the package so it can be uploaded to PyPI and installed with pip (name, version, etc.).

from distutils.core import setup

setup(
   name='SoloLearn', 
   version='0.1dev',
   packages=['sololearn',],
   license='MIT', 
   long_description=open('README.txt').read(),
)

After creating the setup.py file, upload it to PyPI, or use the command line to create a binary distribution (an executable installer).
To build a source distribution, use the command line to navigate to the directory containing setup.py, and run the command python setup.py sdist.
Run python setup.py bdist or, for Windows, python setup.py bdist_wininst to build a binary distribution.
Use python setup.py register, followed by python setup.py sdist upload to upload a package.
Finally, install a package with python setup.py install.

The previous lesson covered packaging modules for use by other Python programmers. However, many computer users who are not programmers do not have Python installed. Therefore, it is useful to package scripts as executable files for the relevant platform, such as the Windows or Mac operating systems. This is not necessary for Linux, as most Linux users do have Python installed, and are able to run scripts as they are.

For Windows, many tools are available for converting scripts to executables. For example, py2exe, can be used to package a Python script, along with the libraries it requires, into a single executable.
PyInstaller and cx_Freeze serve the same purpose.
For Macs, use py2app, PyInstaller or cx_Freeze.

"""

