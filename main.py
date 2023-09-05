# String Practice:

# Create a Python program that asks the user to input a sentence.
# Print the first and last letter of the sentence.
# Convert the entire sentence to uppercase and print the result.
# Find and print a substring from the inputted sentence.
# Replace a word in the sentence and print the updated sentence.
sentence= input("write a sentance.")
print(sentence)
print (sentence[0:1])
print(sentence[-1])
print(sentence.upper())
print(sentence[3:8])
print(sentence.replace("german", "Daniel"))
# Input Practice:

# Create a Python program that asks the user for their name, age, and favorite movie.
# Print a message back to the user with this information.
# Note: Make sure to convert the age to an integer.
nam= input("what is youre name, age and favorite movie?")
print(nam)


# F-String Practice:

# Create a Python program that asks the user for three objects in the room.
# Create variables from these objects and insert those variables into an f-string sentence.
# Print the f-string sentence.
object1= input("what is one objects in the classroom?")
object2=input("what is a second object in the room?")
object3=input("what is a third object in the room?")
print(f'3 objects in this room are {object1}, {object2}, {object3}.')

# Advanced String Practice:

# Create a Python program that reverses the words in a sentence inputted by the user.
# For example, if the user inputs "Python is fun", the program should print "fun is Python".
# Advanced Input Practice:

# Create a Python program that asks the user for the name of their favorite book, movie, and song.

# Print a message that says, "Your favorite book is [Book], your favorite movie is [Movie], and your favorite song is [Song]."


# Advanced F-String Practice:

# Create a Python program that asks the user for their name, age, and the current year.
# Use f-strings to print a message like: "Hello [Your Name], you were born in [Current Year - Your Age]."

# Type Conversion Practice:

# Create a Python program that asks the user for two numbers.
# Print the sum, difference, product, and quotient of the two numbers.
# Note: Make sure to convert the input to integers before performing any calculations.

# Summary Challenge:

# Find a summary of a movie online and create a variable called movie_summary and store the summary in this variable.
# Print the length of the summary.
# Uppercase the entire summary and print it.
# Replace a word in the summary and print the updated summary.
# Print the last word of the summary.


# Real Challenge:

# Create a Python program that asks the user for their first and last name, their age, and their favorite color.
# Using f-strings, print a message that says, "Hello [First Name] [Last Name], you are [Age] years old and your favorite color is [Favorite Color]."

name= input("what is your name?")
print(f'my name is {name}')
age= input("what is your age?")
print(f'I am {age} years old.')
color= input("what is your favorite color?")
print(f'my favorite color is {color}.')
print(f'Hello {name}, you are {age} years old and your favorite color is {color}.')