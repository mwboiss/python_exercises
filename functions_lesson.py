#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~                            Python Functions                            ~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Topics Covered:
# - Using Functions
# - Defining Functions
# - Function Scope
# - Lambda Function Expressions

############################### Using Functions ###############################

# Function Vocabulary
#
# - run / invoke / call
# - argument
# - return value

# We've already used some built-in functions

type('abc')
print('Hey there!')

# TODO: take a look at the code snippet below:
max([1, 2, 3])

# What is the function name?
# Answer: max

# Where is the function invocation?
# Answer: At the beginning - max()

# What is the return value?
# Answer: 3

# TODO: What will the output of the following code be? Why? Explain step-by-step
type(max([1, 2, 3]))
# Answer: 
# Output: <class 'int'> 
# The code will run the max function and then check the type of the output of the max function. 

# TODO: What will the output of the following code be? Why?
type(max)
# Answer: 
# <class 'builtin_function_or_method'>
# It is looking for the type of its input which is just max which is a built in function.

# What other built-in functions do you know?
# Answer: min, len, abs, pow

############################## Defining Functions ##############################

# Function Vocabulary
#
# - Function Definition
# - Function Name
# - Parameter
# - Function Body

def increment(n):
    return n + 1

# TODO: What is the difference between the increment function above and the one below?
def increment(n):
    print(n + 1)
# Answer: The first returns a value that can be used. The second prints the value to a console

# TODO: define a function named is_weekend. This function should accept a string and return true if the string is either saturday or sunday, false otherwise.

def is_weekend(day):
    if day.lower() == 'saturday' or day.lower() == 'sunday':
        return True
    else:
        return False

# TODO: test out your is_weekend function with various values.

print(is_weekend('monday'))
print(is_weekend('saturday'))

# TODO: Use your is_weekend function in combination with input() and an if statement to prompt the user for a day of the week and tell them whether or not it is a weekend.
user_input = input('What day is it? ')
if is_weekend(user_input):
    print('Is weekend.')
else: 
    print('Is not on a weekend')
    
# TODO: Create a function named nonzero. It should accept a number and return true if the number is anythong other than zero, false otherwise.
def nonzero(num):
    if num == 0:
        return False
    else:
        return True

# TODO: Use your nonzero function in combination with the built-in input function and an if statement to prompt the user for a number and print a message displaying whether or not the number is zero.
user_num = int(input('Input a number: '))
if nonzero(user_num):
    print('Is not a zero')
else:
    print('This is a zero')
    
# TODO: Transfer the work you have done into a function named explain_nonzero. Calling this function should prompt the user and display the message as before.
def explain_nonzero():
    user_num = int(input('Input a number: '))
    if nonzero(user_num):
        print('Is not a zero')
    else:
        print('This is a zero')
explain_nonzero()    
## Default Parameter Values and Keyword Arguments ##

# - Positional Argument
# - Keyword Argument

def add(x, y):
    return x + y

add(3, 4) # positional arugment
add(x=3, y=4) # 2 keyword arguments
add(y=4, x=3) # order doesn't matter
add(3, y=4) # we can mix and match postitional and keyword
add(x=3, 4) # error postion aruments com first

def sayhello(name="Innis"):
    return f"Hello, {name}!"

# TODO: call the say hello function and don't pass any arguments
sayhello()

# TODO: call the say hello function and pass your name as a string argument both positionally and as a keyword argument.
sayhello(name='Mathias')
sayhello('Mathias')

## Docstrings ##
def sayhello(name="Innis"):
    "Provides a friendly greeting."
    return f"Hello, {name}!"

sayhello('Mathias')

# Aside: built-in help with help() (or ? in ipython)


################################ Function Scope ################################
#
# - scope refers to defining variables inside/outside of functions
# - scope defines where a variable can be referenced
# - global and local scope

# TODO: look at the example below. What do you expect will happen when you run it?
def f():
    x = 123
f()
print(x)

#Answer: I would expect it to return 123. local variable.

# TODO: look at the example below. What do expect will happen when you run it?
x = 123
def f():
    print(x)
f()

#Answer: Same as above. Global variable

# TODO: look at the example below. What do expect will happen when you run it?
x = 123
def f(x):
    return x + 1
print(f(12))

#Answer: 13. change a global

# TODO: What is the difference between local and global scope? Which is preferred?

#Answer: local is used within the scope of a specific function or peice of the code. Global is used throughout the file we are using.

# TODO: Take a look at the code below. Before running it, think about what you would expect to happen. Explain step by step how the python code is executing.
def changeit(x):
    x = x + 1

x = 42
print(x)
changeit(x)
print(x)

# We are calling a function changeit. Then we are declaring the variable x, printing it, then running x through changeit, and then reprinting x which stays the same because it is a global vairable.

## Function Scope Example ##
def fill_nulls(df):
    return df.fillna(0)

def drop_outliers(df):
    outlier_cutoff = 3
    return df[df.zscore().abs() < outlier_cutoff]

def prep_dataframe(df):
    df = fill_nulls(df)
    df = drop_outliers(df)
    return

# Data Prep example: https://github.com/CodeupClassroom/darden-nlp-exercises/blob/main/nlp_prepare.py
# The specifics here aren't important right now, just pay attention to the overall shape of functions and how local scope is used.

############################### Lambda Functions ###############################
#
# - A function as an expression
# - used for "throw away", or one-off, functions

def increment(n):
    return n + 1
# same as
increment = lambda n: n + 1

# lambda structure
# lambda
# the thing
# :
# what the thing should do

# Use case: sorting (min, max)
#
# Python doesn't know how to compare dictionaries, but it does know how to compare strings or numbers

students = [
    {"name": "Ada Lovelace", "grade": 87},
    {"name": "Thomas Bayes", "grade": 89},
    {"name": "Christine Darden", "grade": 99},
    {"name": "Annie Easley", "grade": 94},
    {"name": "Marie Curie", "grade": 97},
]

# sort by name
sorted(students, key=lambda s: s["name"])

# TODO: write the code necessary to sort by grade
sorted(students, key=lambda s: s["grade"])

# TODO: Write the code necessary to sort the list of student dictionaries by student <em>last</em> name.
# Hint: You will need to write a function that takes in a student dictionary and returns just the last name.
# Hint: You can use the <code>.split</code> string method to seperate the first name and the last name.

# first name
sorted(students, key=lambda s: s['name'].split())

# last name
sorted(students, key=lambda s: s['name'].split()[1])
