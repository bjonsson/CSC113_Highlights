# Brenda Jonsson 10/23/22
# Assignment 6

# This assignment focuses on the design, implementation and testing of a library of Python functions
# to manipulate character strings, as described below.

# 1. The library module will contain three constants and a main function and FOUR other function definitions.
# 2. Note: There are 7 functions described below, complete FOUR of your choice.

#       a) It will include the following constants:
#       ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
#       ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#       DECIMAL_DIGITS  = "0123456789"
#
#       b)  It will include the following functions:
# 	        main – which calls each of the following functions:
#           is_alpha( str ) -> bool
#           is_digit( str) -> bool
#           to_lower( str ) -> str
#           to_upper( str ) -> str
#           find_chr( str, str ) -> int
#           find_str( str, str ) -> int
#           replace_chr( str, str, str ) ->str
#
#       c) Function descriptions

#       Function is_alpha has one parameter (a string).  It returns True if all of the characters
#       in the string are upper case or lower case ASCII letters (it returns False otherwise). In your
#       main function create a list of test data. Iterate thru the list, calling is_alpha with the next
#       item in the list.  Example the list: checkList = ['dog', 'Dog', 'DOG', '1dog', 'do---g', 'DOG1?']
#       should produce the following output:

#       Checking alpha...
# 	        dog is Alpha
# 	        Dog is Alpha
# 	        DOG is Alpha
# 	        1dog is NOT Alpha
# 	        do---g is NOT Alpha
# 	        DOG1? is NOT Alpha
#
#       Function is_digit has one parameter (a string).  It returns True if all of the characters in the
#       string are ASCII decimal digits (it returns False otherwise). Create test data as directed in is_alpha
#       function description.
#
#       Function to_lower has one parameter (a string).  It returns the string which is a copy of the
#       parameter, but where all of the upper case ASCII letters have been converted to lower case ASCII letters.
#       Create test data as directed in is_alpha function description.
#
#       Function to_upper has one parameter (a string).  It returns the string which is a copy of the
#       parameter, but where all of the lower case ASCII letters have been converted to upper case ASCII
#       letters. Create test data as directed in is_alpha function description.
#
#       Function find_chr has two parameters (both strings), where the second parameter must be of length 1.
#       It returns the lowest index where the second parameter is found within the first parameter
#       (it returns -1 if the second parameter is not found within the first parameter).  Create a list of
#       test data. For this one, you will need a list of lists,
#
#       Example the list:
#       checkList = [['hello', 'l'], ['hello', 'e'], ['hello', 'x']]
#       should produce the following output:
#
#       Checking character l in hello
#       2
#       Checking character e in hello
#       1
#       Checking character x in hello
#       -1
#
#       Function find_str has two parameters (both strings).  It returns the lowest index where the
#       second parameter is found within the first parameter (it returns -1 if the second parameter
#       is not found within the first parameter).  Create test data as directed in find_chr function description.
#
#       Function replace_chr has three parameters (all strings), where the second and third parameters
#       must be of length 1.  It returns the string which is a copy of the first parameter, but where
#       all occurrences of the second parameter have been replaced by the third parameter (it returns
#       the empty string if the second or third parameter are not of length 1).  Create test data as
#       directed in find_chr function description (this time, 3 items in each list)
#
#       d)  The library module will not use any of the string methods listed in Section 4.7.1 of the
#       Python Standard Library:
#       http://docs.python.org/3.3/library/stdtypes.html#string-methods
#
#       e) The library module will not contain any import statements.
#       f) The program will not perform any input operations (it will not call function input).  All
#       test data is built into the program. Be sure to test all variations of data.

# START OF LIBRARY

# 3 constants
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS  = "0123456789"

# Test string
check_list = ['ASDLKkjsd12', 'cat', 'Cat', 'CAT', '2cat', 'ca---T', 'CaT2!', '123423', '123214324!']

# Main function
def main(check_list):

    for test_val in check_list: #Feeding the list into result as a for loop changes everything. It feeds individual strings, not a whole list.
        result = is_alpha(test_val)
        if result == True:
            print(test_val + " consists of only letters of the alphabet.")
        else:
            print(test_val + " does not consist of only letters of the alphabet.")

    for test_val in check_list:
        result = is_digit(test_val)
        if result == True:
            print(test_val + " is purely numeric.")
        else:
            print(test_val + " does not consist of only numbers.")

    for test_val in check_list:
        result = to_lower(test_val)
        print(result)

    for test_val in check_list:
        result = to_upper(test_val)
        print(result)


#First function
def is_alpha(check_list):
    flag = 0
    for each in check_list:
        for character in each: #This line is probably redundant, because only a single string is passed from the list because main() feeds the list through a for loop.
            if character in ASCII_LOWERCASE or character in ASCII_UPPERCASE:
                flag = True
            else:
                return False #Returning false exits the function, whereas break would only exit one for loop.

    return flag

#Second function
def is_digit(check_list):
    flag = 0
    for each in check_list:
        for character in each:
            if character in DECIMAL_DIGITS:
                flag = True
            else:
                return False #Returning false exits the function, whereas break would only exit one for loop.

    return flag


#Third function
def to_lower(check_list):

    cup = "" #I watched a video once that said if you want to transfer two cups of coffee from one cup to another,
             # you need a third cup. And I'm transferring uppercase to lowercase.
    final_string = ""

    count = 0
    while count < len(check_list): #Iterating through each character of a string. The arguments come through as strings,
                                   # not lists since main() feeds the list in a for loop.

        if check_list[count] in ASCII_UPPERCASE: #Checking if an individual character is uppercase.
            x = 0
            while x < len(ASCII_LOWERCASE):
                if check_list[count] == ASCII_UPPERCASE[x]: #This ends naturally because checklist[count] is singular.
                    cup = ASCII_LOWERCASE[x]
                    final_string = final_string + cup
                    x += 1
                else:
                    x += 1

            count += 1 #The program will break if this is not indented right here. It must iterate after we've gone through all x.

        else:
            final_string = final_string + check_list[count] #If the character isn't uppercase, we stick
                                                            # the letter at the end of the final string and move
                                                            # on to the next character.
            count += 1

    return final_string


#Third function
def to_upper(check_list):

    cup = ""
    final_string = ""

    count = 0
    while count < len(check_list):

        if check_list[count] in ASCII_LOWERCASE: #Just switching upper and lower case for the new function.
            x = 0
            while x < len(ASCII_LOWERCASE):
                if check_list[count] == ASCII_LOWERCASE[x]:
                    cup = ASCII_UPPERCASE[x]
                    final_string = final_string + cup
                    x += 1
                else:
                    x += 1

            count += 1

        else:
            final_string = final_string + check_list[count]
            count += 1

    return final_string

# Calling main
main(check_list)
