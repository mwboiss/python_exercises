# Control Structures Exercises
# Problem 1: Conditional Basics
#A: prompt the user for a day of the week, print out whether the day is Monday or not

day = input('Input a day of the week:')
if day.lower() == 'monday':
    print('You chose Monday')
else:
    print('You didn\'t choose monday')

#B: prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_type = input('Input a day of the week:')
if day_type.lower() == 'saturday' or 'sunday':
    print('You chose a day that falls on a weekend.')
else:
    print('You chose a weekday.')

#C: create variables and make up values for:
    # the number of hours worked in one week
    # the hourly rate
    # how much the week's paycheck will be
    # write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

week_days_worked = 5
hours_worked_daily = 8
hours_worked_weekly = week_days_worked * hours_worked_daily
print(f'Typical weekly hours worked: {hours_worked_weekly}')

hourly_pay_rate = 100
weekly_paycheck = hours_worked_weekly * hourly_pay_rate
print(f'Working 40 hours at a pay rate of {hourly_pay_rate} in a week you would make ${weekly_paycheck}')

actual_hours_worked = 50
if actual_hours_worked > 40:
    pay = (actual_hours_worked * hourly_pay_rate) + ((actual_hours_worked - 40) * (hourly_pay_rate / 2))
else: 
    pay = actual_hours_worked * hourly_pay_rate

print(f'Working {actual_hours_worked} you would make ${pay}')

#Problem 2: Loop Basics
#A: While
    # Create an integer variable i with a value of 5.    
    # Create a while loop that runs so long as i is less than or equal to 15    
    # Each loop iteration, output the current value of i, then increment i by one.    
    # Your output should look like this:
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15

i = 5
while i <= 15:
    print(i)
    i += 1
    
    # Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2
    
    # Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5
    
    # Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
# 2
# 4
# 16
# 256
# 65536
        
i = 2
while i < 1_000_000:
    print(i)
    i **= 2
    
    # Write a loop that uses print to create the output shown below.

# 100
# 95
# 90
# 85
# 80
# 75
# 70
# 65
# 60
# 55
# 50
# 45
# 40
# 35
# 30
# 25
# 20
# 15
# 10
# 5

i = 100
while i >= 5:
    print(i)
    i -= 5

#B For Loops
    # Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
    # For example, if the user enters 7, your program should output:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
   
i = int(input('Pick a number:'))
for n in range(1, 11):
    k = n * i
    print(f'{i} x {n} = {k}') 
    
    # Create a for loop that uses print to create the output shown below.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for n in range(1,10):
    print(f'{n}' * n)
    
#C: break and continue
    # Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered. 
    # Your output should look like this:
# Number to skip is: 27

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49

input_correct = True

while input_correct == True:
    x = input('What is an odd number between 1 and 50? ')
    if x.isdigit() and int(x) % 2 != 0 and int(x) < 50 and int(x) > 0:
        print(f'Number to skip is: {x}\n')
        i = 1
        while i < 50:
            if i == int(x):
                print(f'Yikes! Skipping number: {x}')
                i += 2
                continue
            else:
                print(f'Here is an odd number: {i}')
                i += 2
        break
    else:
        print('Try again')

#D: The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

input_correct = True

while input_correct == True:
    x = input('Input a positive number: ')
    if x.isdigit() and int(x) > 0:
        i = 0
        while i <= int(x):
            print(i)
            i += 1
        break
    else:
        print('Try again')

#E: Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

input_correct = True

while input_correct == True:
    x = input('Input a positive number: ')
    if x.isdigit() and int(x) > 0:
        i = int(x)
        while i >= 1:
            print(i)
            i -= 1
        break
    else:
        print('Try again')

#Problem 3: Fizzbuzz
#One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
    #Write a program that prints the numbers from 1 to 100.
    #For multiples of three print "Fizz" instead of the number
    #For the multiples of five print "Buzz".
    #For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
        
#4: Display a table of powers.
    # Prompt the user to enter an integer.
    # Display a table of squares and cubes from 1 to the value entered.
    # Ask if the user wants to continue.
    # Assume that the user will enter valid data.
    # Only continue if the user agrees to.
    # Example Output:
# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125

wants_to_continue = True

while wants_to_continue == True:
    x = input('What number would you like to go up to? ')
    print(f'\nHere is your table!\n')
    print(f'number | squared | cubed')
    print(f'------ | ------- | -----')
    i = 1
    while i <= int(x):
        print(f'{i}      | {i**2}       | {i**3}')
        i += 1
    keepitgoing = input('Enter \'Yes\' if you want to continue? ')
    if keepitgoing == 'Yes':
        wants_to_continue = True
    else:
        wants_to_continue = False

#Bonus: Research python's format string specifiers to align the table

# work in progress

wants_to_continue = True

while wants_to_continue == True:
    x = input('What number would you like to go up to? ')
    print(f'\nHere is your table!\n')
    print(f'number | squared | cubed')    
    print(f'------ | ------- | -----')
    i = 1
    while i <= int(x):
        i_squared = i ** 2
        i_cubed = i ** 3
        print('{0:<6} | {1:<7} | {2:<6}'.format(i, i_squared, i_cubed))
        i += 1
    keepitgoing = input('Enter \'Yes\' if you want to continue? ')
    if keepitgoing == 'Yes':
        wants_to_continue = True
    else:
        wants_to_continue = False

#Problem 5: Convert given number grades into letter grades.
    # Prompt the user for a numerical grade from 0 to 100.
    # Display the corresponding letter grade.
    # Prompt the user to continue.
    # Assume that the user will enter valid integers for the grades.
    # The application should only continue if the user agrees to.
    # Grade Ranges:
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
keep_going = True

while keep_going == True:
    grade = input('Enter numerical grade from 0 to 100: ')
    if int(grade) <= 59:
        print('F')
    elif int(grade) <= 66:
        print('D')
    elif int(grade) <= 79:
        print('C')
    elif int(grade) <= 87:
        print('B')
    else:
        print('A')
    should_i = input('Input "Yes" if you would like to continue: ')
    if should_i == 'Yes':
        keep_going = True
    else:
        keep_going = False
        
    # Bonus: Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

keep_going = True

while keep_going == True:
    grade = input('Enter numerical grade from 0 to 100: ')
    if int(grade) <= 59:
        print('F')
    elif int(grade) <= 62:
        print('D-')
    elif int(grade) <= 66:
        print('D')
    elif int(grade) <= 69:
        print('D+')
    elif int(grade) <= 72:
        print('C-')
    elif int(grade) <= 76:
        print('C')        
    elif int(grade) <= 79:
        print('C+')
    elif int(grade) <= 82:
        print('B-')
    elif int(grade) <= 86:
        print('B')
    elif int(grade) <= 89:
        print('B+')
    elif int(grade) <= 92:
        print('A-')
    elif int(grade) <= 96:
        print('A')
    else:
        print('A+')
    should_i = input('Input "Yes" if you would like to continue: ')
    if should_i == 'Yes':
        keep_going = True
    else:
        keep_going = False

#Problem 6: Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

books_read = [{'title':'Zen Mind, Beginner\'s Mind','author':'Shunryu Suzuki','genre':'Zen'},
              {'title':'Gravitas','author':'Caroline Goyder','genre':'Communication'},
              {'title':'What Color Is Your Parachute?','author':'Richard Bolles','genre':'Professional Development'},
              {'title':'Difficult Conversations','author':'Douglas Stone','genre':'Communication'},
              {'title':'The Data Science Handbook','author':'Carl Shan','genre':'Professional Development'},
              {'title':'Naked Statistics','author':'Charles Wheelan','genre':'Education'},
              {'title':'How Charts Lie','author':'Alberto Cairo','genre':'Education'}
              ]

for book in books_read:
        print('Books in list:\n\nTitle:  ', book['title'], '\nAuthor: ', book['author'], '\nGenre:  ', book['genre'], '\n--------------')
        
    
    # Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

genre_pref = input('Pick a genre between Zen, Communicaiton, Professional Development, Education: ')

for book in books_read:
    if genre_pref == book['genre']:
        print(f'Book in Genre {genre_pref}:\n', book['title'],'\n')  