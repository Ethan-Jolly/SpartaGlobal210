# Python Basic Doc

This file will contain the basic documentation for the foundational basis of knowledge in Python.

## Data Types
* The main data types in Python are:
  * Integers
  * Floats
  * Strings
  * Boolean

### Numbers (i.e Ints and Floats)
* You can perform standard mathematical operations on ints and floats in Python, as well as modulo ```%``` on integers.
```Python
x = 5
y = 5.1583
z = 5 * 6
w = 10 % 4
```
### Strings
* Strings in python are a collection of unicode characters, can be manipulated, indexed and used in many different ways. Especially by making use of in-built functions to handle strings.
* Some examples of this are:
```Python
first_name = "ethan"
last_name = "jolly"

print(first_name[0]) # Indexing
print(first_name[2:4]) # Slicing
print(first_name[-1]) # Find end of string
print(len(first_name)) # Length of string

print(first_name + ' ' + last_name) # Concatenation
print("This is a test \"Escape Characters \"") # Escape Characters

print(first_name.capitalize()) # Capitalize first letter of string
print(first_name.upper()) # Convert string to uppercase
print(first_name.replace('a', 'aaaaaaaaa')) # Replace all instances of substring with new substring
```
### Boolean
* Boolean values are used to indicate if something is True or False, used as the result of conditional operations, i.e checking if something is less than something.
```Python
check = False
value = True
print(check == value)
```
### IF Statements
* IF statements use the results of conditional operations to perform some action. The syntax path for this in Python is:
```buildoutcfg
if <condition>:
    do_something()
elif <condition>:
    do_something_else()
else:
    perform_default_action()
```
### Lists
* Lists are used to contain multiple variables in a single operation which you can index or iterate through. You can also use many different in-built functions in Python for lists. Some examples are:
```Python
# Lists can contain multiple types, but you tend to want to keep the type consistent
lst = [1,2,3,4,5,6]
print(lst[3])
print(len(lst)) # Returns number of items in list
lst.append(7) # Adds item to end of the list
print(lst)
print(lst.index(3)) # Returns the index of the item you passed in
```
### Dictionaries
* Dictionaries are a key-value pair data structure, similar to JSON. An example of a dictionary and some operations in Python is:
```Python
contact_list = {
    "jane": "0901391203"
}

print(contact_list["jane"])
contact_list["bob"] = "07471464348"
print(contact_list.keys())
print(contact_list.values())
```
### Loops
* Loops are used to iterate through a list of items and perform some action on each iteration. In Python there are two cases of loops, while and for.
  * ***While Loops***: Repeat action in loop until condition in while returns False
  * ***For Loops***: Repeat action in loop until items in loop condition have been iterated through.
```Python
# While loop

condition = 0
while condition < 5:
    print('hello')
    condition += 1

print('-------------')
# For Loop

for i in range(5):
    print('hello')
```
### Functions
* Functions are used to be able to define a closed off block of code which only runs which called. You can pass parameters in to functions, and functions can return results from them.
* An example of a function and how you would call it:
```Python
def calculate_percent(value, percent):
    return (percent/100)*value
    
calculate_percent(60,10)
```