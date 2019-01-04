# Created by:   Patrick Archer
# Date:         21 December 2018
# Copyright to the above author. All rights reserved.

"""

Directions - COMPLETE:
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that
reads the same forwards and backwards.)

"""

import string

# ################################################# start_funcs

def checkIfPalindrome(passedString):

    # build new string from reversed initially-passed string
    reversedStr = passedString[::-1]
    print("\nOriginal String (all characters lowercased):\n\"" + passedString.lower() + "\"")
    print("\nReversed String (all characters lowercased):\n\"" + reversedStr.lower() + "\"")

    if (passedString.lower() == reversedStr.lower()):
        print("\nThus, because the original string IS the same as its reversed self, \n"
              "the string IS a palindrome.\n")
        return True
    else:
        print("\n--> Thus, because the original string is NOT the same as its reversed self, \n"
              "\tthe string is NOT a palindrome. <--\n")
        return False

# ################################################# end_funcs/start_main

userString = str(input("\nPlease enter any random string.\n--> Press \"Enter\" when you are ready to check if "
                   "the string you entered is a palindrome.\n"))

# bool to check if string is palindrome
isPal = checkIfPalindrome(userString)
print("<CONSOLE>: Returned isPalindrome result: " + str(isPal))
print("<CONSOLE>: Program now exiting.")

# ################################################# end_main









