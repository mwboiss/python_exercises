# Function Exercises
# After creating each function specified below, write the necessary code in order to test your function.

# Problem 1: 
# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(num):
    if num == 2 or num == '2' or num == 'two':
        return True
    else:
        return False

is_two(2)
is_two('hamsandwich')

# Problem 2:
# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(vow):
    if type(vow) == str:
        if vow in ['a','e','i','o','u','y']:
            return True
        else:
            return False
    else:
        return False

vow = 'a'
nvow = 'g'
nvown = 1

is_vowel(vow)
is_vowel(nvow)
is_vowel(nvown)

# Problem 3:
# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(con):
    if type(con)
    if con.upper() in 'B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z':
        return True
    else:
        return False

con = 'b'
ncon = 'a'

is_consonant(con)
is_consonant(ncon)

# Problem 4:
# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_con(word):
    if word[0].upper() in 'B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z':
        return word.capitalize()
    else:
        return word
    
word = 'hamsandwich'
other = 'apple'
    
cap_con(word)
cap_con(other)
        
# Problem 5:
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip,bill):
    total = bill + (bill * tip)
    return total

tip = 0.3
bill = 50

calculate_tip(tip,bill)

# Problem 6:
# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage):
    after_discount = original_price - (original_price * discount_percentage)
    return after_discount

original_price = 50
discount_percentage = 0.3

apply_discount(original_price, discount_percentage)

# Problem 7:
# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(num_string):
    new_string = ''
    for digit in num_string:
        if digit != ',':
            new_string += digit
    return int(new_string)

num_string = '1,000'

handle_commas(num_string)

# Prolem 8:
# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F)

def get_letter_grade(grade):     
    if int(grade) <= 59:
        print('F')
    elif int(grade) <= 69:
        print('D')
    elif int(grade) <= 79:
        print('C')
    elif int(grade) <= 89:
        print('B')
    else:
        print('A')
        
grade = 84

get_letter_grade(grade)

# Problem 9:
# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(vowely):
    vowless = ''
    for letter in vowely:
        if letter not in 'aeiouy':
            vowless += letter
    return vowless

vowely = 'hamsandwich'

remove_vowels(vowely)

# Problem 10:
# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    # anything that is not a valid python identifier should be removed
    # leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores
    # for example:
        # Name will become name
        # First Name will become first_name
        # % Completed will become completed


######### FIX KEYWORD ISSUE

def normalize_name(name):
    new_name = name.lower().strip()
    for char in new_name:
        if char in '[@!#$%^&*_()<>?/\|}{~:]':
            new_name = new_name.replace(char,'')
    for idx, char in enumerate(new_name):
        if char in '0123456789' and idx == 0:
            new_name = new_name.replace(char,'')
    return new_name.strip().replace(' ','_')

name1 = 'Name'
name2 = ' 99First Name'
name3 = '% Comleted'
name4 = ' trying to break it '
name5 = ' _really trying to *#&$ it up        '

normalize_name(name1)
normalize_name(name2)
normalize_name(name3)
normalize_name(name4)
normalize_name(name5)

# Problem 11:
# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
    # cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    # cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(num_list):
    sum_list = []
    num_sum = 0
    for num in num_list:
        num_sum += num
        sum_list.append(num_sum)
    return sum_list

cumulative_sum([1, 1, 1])
cumulative_sum([1, 2, 3, 4])

############################################################################################################################
# Additional Functions Exercise From:
# https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886

# Comment each line of your function with an explanation of what that line is doing. Make sure to document both the type of all function parameters and the type that will be returned from the function. Also be sure to use the vocabulary we've introduced to describe your python code appropriately.

# Walk us through how the function executes using the comments you wrote and several different example inputs that demonstrate all the possible paths through your function.

# Here's an example:

# Write a function named sayhello. This function should return a message like "Hello, NAME!" Where name is the value passed to the function. If the passed value is the name of your cohort, instead return a message that says "COHORT is the name of my class!".

# # our sayhello defines a single parameter, name that is a string, and will return a string value
def sayhello(name):
    # Check to see if the passed argument is equal to our cohort name
    if name == "Darden":
        # Craft the message from the problem spec
        message = "Darden is the name of my class!"
    else:
        # Here we use the function parameter to craft a hello message if the conditional is false
        message = f"Hello, {name}!"
    # Regardless of the contents, we'll return the message variable from the function
    return message

# Walkthrough:

# When we pass "Darden", the conditional will evaluate to True and the first branch of the if statement will be followed. The message variable will be created such that it has the required message from the problem specification. The message variable is returned from the function and the return value is passed to the print function. We will see "Darden is the name of my class" printed in our console/notebook.

print(sayhello("Darden"))

# When we pass "World", the conditional will evaluate to False and the second branch of the conditional will be taken. The message variable will hold "Hello, World!" and that value will be returned from the function. The return value will be passed to the print statement and we will see "Hello, World!" in our console/notebook.

print(sayhello("World"))
############################################################################################################################

# Bonus

# Problem 1:
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

def twelveto24(time_string):
    helper_list = []
    if time_string[-2:] == 'am':
        time_string = time_string[:-2]
    elif time_string[-2:] == 'pm':
        time_string = time_string[:-2]
        helper_list = time_string.split(':')
        helper_list[0] = str(int(helper_list[0]) + 12)
        time_string = ":".join(helper_list)
    return time_string

time_string1 = '10:45am'
time_string2 = '4:30pm'

twelveto24(time_string1)
twelveto24(time_string2)

# Problem 2:
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
    # col_index('A') returns 1
    # col_index('B') returns 2
    # col_index('AA') returns 27
       
def col_index(col_name):
    col_length = len(col_name)
    col_base = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    col_sum = 0
    for idx, digit in enumerate(col_name):
        col_sum += (26 ** (col_length - (idx + 1))) * (col_base.index(digit) + 1)
    return col_sum
    

col_index('A')
col_index('BB')
col_index('AA')
col_index('AAA')
col_index('ABCDEF')