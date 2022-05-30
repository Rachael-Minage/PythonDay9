import os
programming_dictionary = {"Bug":"An error in a program that prevents the program from running as expected",
"Function":"A piece of code that you can easily call over and over again",
"Loop":"The act of doing something over and over again"}

#Retrieving items from a dictionary
# print(programming_dictionary["Bug"])

#Adding items to a dictonary
programming_dictionary["List"] = " A data structure in Python that is a mutable, or changeable, ordered sequence of elements"
# print(programming_dictionary)

#Looping through dictionaries
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Grading program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key]> 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >80:
        student_grades[key]="EXceeding expectations"
    elif student_scores[key] > 70:
        student_grades[key]="Acceptable"
    else:
        student_grades[key]="Fail"


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(state,no_of_visits,cities_visited):
    new_country = {}
    new_country["country"] = state
    new_country["visits"] = no_of_visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)








#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



# Given this list of students containing age and name, 
#  students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"},
#  {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}], 
# write a function that greets each 
# student and tells them the year they were born.
#  e.g Hello Eunice, you were born in the year 2002.

students = [
{"age": 19, "name": "Eunice"}, 
{"age": 21, "name": "Agnes"}, 
{"age": 18, "name": "Teresa"},
{"age": 22, "name": "Asha"},
]

def greet(students_values):
    for student in students_values:
      student_name =  student["name"]
      yob= (2022 - student["age"])
      print(f"Hello {student_name},you were born in {yob}")

greet(students_values=students)

# Blind auction
# bid = {}
# bidding_finished = False

# def highest_bidder(bidder_record):
#   for bidder in bidder_record:



# while not bidding_finished :
#   bidder_name = input("Enter name of bidder:\n")
#   bid_price = input("Enter bid price:\n")
#   bid[bidder_name]=bid_price
#   should_continue = input("Are there any bidders? Y or N:\n")
#   if should_continue=="N":
#     bidding_finished=True
#   elif should_continue=="Y":
#     os('clear')

#Dictionaries
#  Write a Python script to sort (ascending and descending) a dictionary by value
















    







