"""
    CSC 309 SFSU Spring 2023
    Project #2
    Created on Fri Feb  9 22:53 2024
    Last Updated Mon Feb 12  22:57
    @author: scottquashen
    
    


    Description: 
        This program creates a list of pseudo-random numbers based on a seed value.
        User is prompted to specify 1) the amount of numbers in the list, and
        2) a seed value, which is used for creating pseudo-random numners.
        The program then uses the two user-inputs to print a list of numbers in two formats.
        
    Notes: This project goes beyond the requirements of the project by using:
        1) Better (safer) input function
        2) Enum to sort the list (safer)
        3) Min and max values passed into to random number function (expanded functionality)
        4) Various techniques of loops to iterate (learning new techniques)
    

    Inputs: 
        L: List where random numbers are stored
        M: Int representing amount of items per line to print
        Enum for printing correct labels in console 
        S: User input, int (seed value)
        N: User input, int (amount of items in L)
        Min and Max: int values for creating random number range

    Outputs: 
        Print: List in console, with two formats
        Print: Label in console
        Print: Dev name and current date/ time in console
        Output: Pseudo-random numbers based on seed value (S) in range min..max
        Output: Update list values sorted from low to high

        
        Return: Int from user input: num, used to set values for S and N
        Return: List of those random numbers with N amount of items
       

    Dependencies: Time, Random, Enum

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.2.1
"""


# Imports Section--------------------------------------------------

import time
import random
# Enum makes the code easier to read and safer when using conditionals with strings
from enum import Enum



# Declarations Section--------------------------------------------------

orderingFormat = Enum('Ordering', ['isOrdered', 'notOrdered'])

# Write a function to print the Python List.
# We'll handle this with a for loop using built in enumerate() function so that we can track the index
def printList(someList, M, sortStyle):
    """ 

This function iterates an inputed list and prints all items of that list with M items per row.
The function determines if a new line should be printed by checking if the index mod M == 0.
If the length of the list % M != 0, then the final printed row will have less than M items.
The list will be printed in one of two ways based on the input 'sortStyle', 
which expects an Enum called orderingFormat -- This enum also determines the label printed in the console. 

Inputs: A numeric argument: M, an Enum to sort the list: sortStyle, and a list of type int: someList

Output: Prints list of type int in console

Returns: Nothing

Usage: printList(L, 8, orderingFormat.notOrdered)

    """
    if(sortStyle == orderingFormat.notOrdered):
        print("\n\n\nHere is the unordered list with " + str(M) + " items per row:")
    else:
        print("\n\n\nAnd below is the ordered list with " + str(M) + " items per row:")
    for index, i in enumerate((someList)):
        if(index % M == 0):
            print("\n")
        print(i, end= ", ")
                  
# Print name and current date/time (via time module)
print("Scott Quashen " + time.asctime())


# Prompt user for two int values, N for length of the list, and S for seed value (for generating pseudo-random numbers)
# By using this code from PC input, we can avoid potential runtime type errors based on user inputs
def getInteger(prompt):
    """ 

This function requests user input AND asks user to try again IF they don't input a value of type int.

Inputs: Prompt: the (string) message that we will pass into the built-in input function

Output: Each time user inputs incorrect value type they will be prompted to try again, the loop restarts     

Returns: If the user's input is of type int, then that value is returned as: num
         note: The return statement ends the loop, which moves the program forward

Usage: N = getInteger("input your N value: ")

    """
    
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print( "That is not an integer -- please try again" )
            continue
        return num
    
# Prompt the user for two values, N and S. 
N, S = getInteger("Please enter an integer N (list size): "), getInteger("Please enter an integer S (random number seed): ")

# Create a Python list (L) of N random numbers in the range [0..99] using the random seed value S.
# Declare the list with global scope
L = []

# Within our range, Create N amount of pseudo-random numbers based on seed value, then
# Add those values to our list, then
# Return the list
def randomNumbers(min, max):
    """ 

This function creates N amount of pseudo-random numbers within a given range
and adds those to a list, then returns the completed list.

Inputs: Min: int, max: int
        S: previous user input
        N: previous user input

Output: Nothing to console

Returns: The list that contains the newly created numbers

Usage: randomNumbers(0, 99)

    """
    random.seed(S, int)
    while (len(L) < N):
        L.append(random.randint(min, max))
    return L





# Function Calls Section--------------------------------------------------

# Call randomNumbers to generate the list
randomNumbers(0, 99)  

# Call your print function, passing in your list L and use a value of M=8
printList(L, 8, orderingFormat.notOrdered)

# Use the built-in Python list sort() method to sort the list in ascending order (low to high)
L.sort()

# Call print function again, passing in the (updated) sorted list L and use a value of M=10
printList(L, 10,  orderingFormat.isOrdered)















