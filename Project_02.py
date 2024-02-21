"""
    Scott Quashen
    CSC 309 SFSU Spring 2024
    Project #2
    Created on Fri Feb 9 22:53 2024
    Last Updated Tues Feb 20  15:59 2024
  
    
    


    Description: 
        The program request two user-inputs (size and seed) to print a list of random numbers in order, and unordered,
        with M amount of items per row.
        
    Notes: featuring
        1) Better (safer) input function
        3) Min and max values passed into to random number function (expanded functionality)
    

    Inputs: 
        L: List where random numbers are stored
        M: Int representing amount of items per line to print
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
       

    Dependencies: Time, Random

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.2.1
"""


# Imports Section--------------------------------------------------

import time
import random


# Declarations Section--------------------------------------------------



def printList(someList, M):
    """
    
    Description
    ----------
    printList() iterates an inputed list and prints all items of that list with M items per row.
    
    Parameters
    ----------
    someList : List<Int>
        This is our list of numbers.
    M : Int
        How many items per row to be printed.
   
    Returns
    -------
    None.

    """

    for i in range((len(someList))):
        if(i % M == 0):
            print("\n")
        print(someList[i], end= ", ")      
        
# end of printList() function
                  


def getInteger(prompt):
    """
    
    Description
    ----------
    getInteger() requests user input AND asks user to try again IF they don't input a value of type int.

    Parameters
    ----------
    prompt : String
        The message presented to the user when requesting an int in the console.

    Returns
    -------
    None.

    """
    
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print( "That is not an integer -- please try again" )
            continue
        return num
    
# end of getInteger() function
    



def randomNumbers(size, seed, min, max):
    """
    
    Description
    ----------
    randomNumbers() creates N amount of pseudo-random numbers within a given range adds those to a list, then returns the completed list.

    Parameters
    ----------
    min : TYPE
        DESCRIPTION.
    max : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    L = []
    random.seed(S, int)
    while (len(L) < N):
        L.append(random.randint(min, max))
    return L

# end of randomNumbers() function


# end of function definitions section -------



# Function Calls Section--------------------------------------------------



# Prompt the user for two values, N and S, we'll pass these in to our randomNumbers() function 
N, S = getInteger("Please enter an integer N (list size): "), getInteger("Please enter an integer S (random number seed): ")

# Print name and current date/time (via time module)
print("Scott Quashen " + time.asctime())



# Call randomNumbers to generate the list, save it to a variable to pass into our printList() function 
myList = randomNumbers(N, S, 0, 99) 


# Call your print function, passing in your list L and use a value of M=8
print('\n\nhere is the unordered list:')
printList(myList, 8)

# Use the built-in Python list sort() method to sort the list in ascending order (low to high)
myList.sort()

# Call print function again, passing in the (updated) sorted list L and use a value of M=10
print('\n\n\n\nhere is the ordered list:')
printList(myList, 10)




# end of function calls section




