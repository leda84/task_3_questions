#Question 1 
#Write a function to print "hello_USERNAME!"
#USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(username):
    """Greet your user."""
    print("Hello, " + username.upper() + "!")

hello_name('laura')



#Question 2
#Print first 100 odd numbers in Python.

for n in range(1,100):
    if n %2 != 0:
        print(n)



#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
#The first line of the code has been defined as below.
def max_num_in_list(a_list):
    """Return max number of a given list"""
    print(max(a_list))
        
numbers=[23,57,1,5,32]
max_num_in_list(numbers)
ages=[78,17,93,27,38]
max_num_in_list(ages)



#Question 4
#Write a function to return if the given year is a leap year.
#A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean Type (true/false).

def leap_year_or_not(year):
    """Figure out if a given year is a leap year"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
leap_year_or_not(2000)

#year % 4 == 0 to show that it would be divisible by 
#and to show that it will also need the following condition
# year % 100 != 0 to show that it wouldnt be divisible by 100(there would be a remainder)
#year % 400 == 0 to show that the year could be divided by 400 (there would be no remainder)
#or to show the unless condition

#year % 100 != 0 or year % 400 == 0



#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type.

def is_consecutive(a_list):
    """Figure out if all numbers in a list are consecutive numbers"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

check_list = [2,6,3,5,4]
is_consecutive(check_list)

#numbers = [4,7,2,9,3]
#is_consecutive(numbers)    this returns false
    
#sorted(a_list) can help check if the numbers are consecutive by putting them in order first
#range() can help to check the numbers from start to finish of the sorted list
#since we do not know the numbers that will be in the list, min() & max() can help
# use +1 to show that each consecutive number will be the number before plus one more(all return false w/o this)
