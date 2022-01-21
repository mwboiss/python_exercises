# Data Types, Operators and Variables

#Problem 1
#You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?

movies =    [
            {'movie': 'The_little_mermaid', 'days': 3}, 
            {'movie': 'Brother_Bear', 'days' : 5}, 
            {'movie': 'Hercules', 'days': 1}
            ]
price_per_day = 3

cost_per_movie = [day['days'] * price_per_day for day in movies ]
print(cost_per_movie)

total_price = sum(cost_per_movie)
print(total_price)

#Problem 2
#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

current_contracts = [{'company': 'Google', 'rate': 400, 'hours': 6}, 
                        {'company': 'Amazon', 'rate': 380, 'hours': 4},
                            {'company': 'Facebook', 'rate': 350, 'hours': 10}]

pay_per_company = [pay['rate'] * pay['hours'] for pay in current_contracts]
print(pay_per_company)

total_pay = sum(pay_per_company)
print(total_pay)

#Problem 3
#A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.

class_details = [
                {'subject': 'Math','capacity': 20, 'enrolled': 15, 'day': 'Monday'}, 
                {'subject': 'Science','capacity': 20, 'enrolled': 16, 'day': 'Tuesday'},
                {'subject': 'English','capacity': 20, 'enrolled': 17, 'day': 'Wednesday'},
                {'subject': 'Art','capacity': 20, 'enrolled': 18, 'day': 'Thursday'},
                {'subject': 'History','capacity': 20, 'enrolled': 18, 'day': 'Thursday'},
                {'subject': 'Economics','capacity': 20, 'enrolled': 20, 'day': 'Friday'},
                {'subject': 'Art','capacity': 20, 'enrolled': 18, 'day': 'Saturday'},
                {'subject': 'Computer Science','capacity': 20, 'enrolled': 12, 'day': 'Friday'}
                ]

student_schedule =  [
                    {'subject': 'Math', 'day': 'Monday'}, 
                    {'subject': 'Science','day': 'Tuesday'},
                    {'subject':'English', 'day': 'Wedensday'}
                    ]

def student_should_take(classes, student):
    can_take = []
    for cap in classes: 
        if cap['capacity'] > cap['enrolled']:
            can_take.append(cap)    
    
    student_day = []    
    for day in student:
        student_day.append(day['day'])    

    student_subject = []    
    for subject in student:
        student_subject.append(subject['subject'])    

    should_take = []
    for day in classes:
        if day in can_take:        
            if day['subject'] not in student_subject:
                student_subject.append(day['subject'])
                if day['day'] not in student_day:
                    student_day.append(day['day'])
                    should_take.append(day)
                    
    return [print(f'\nClass Available for Student:\n{avail_class}\n') for avail_class in should_take]

student_should_take(class_details, student_schedule)

# Not sure why it has a list with None, None in it. I'm guessing it is has something to do with how the list comprehension is going through the list of dictionaries. 

#Problem 4
#A product offer can be applied only if people buy more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
import datetime
item_total = 3
expire_date = '01/19/22'
premium_member = False

def qualified(tot, ex, mem):
    current_date = datetime.datetime.now().strftime("%x")
    qual = True
    if current_date <= ex: 
        if mem is True:
            qual = True
        elif tot > 2:
            qual = True
        else:
            qual = False
    else:
        qual = False
    return qual

print(qualified(item_total, expire_date, premium_member))

#Problem 5
#Create a variable that holds a boolean value for each of the following conditions:
##the password must be at least 5 characters
##the username must be no more than 20 characters
##the password must not be the same as the username
##bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

valid_login = [
                len(username) >= 5, 
                len(username) <= 20, 
                username != password, 
                username.endswith(' ') & 
                password.endswith(' ') & 
                username.startswith(' ') &
                password.startswith(' ') == False
               ]

print(valid_login)