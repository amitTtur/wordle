from math import *
# inclusive
# does not support scientific constants (e.g., pi, e, K, etc.)

# Prompts the user to enter a number within a given range.
# Returns the number if valid, otherwise keeps asking.
def getNumberInput(min=0, max=0):
    # If max is greater than min, return 0 (likely meant to be min > max for validity check?)
    if min > max: return 0

    # Calculate the max number of digits needed for input validation
    maxNumOfLetters = _getNumberLength(min) if _getNumberLength(min) > _getNumberLength(max) else _getNumberLength(max)

    f = 1
    while f:
        # Ask user to enter a number within the given range
        inp = input(f"Please enter a number ({min}-{max}): ")

        # Check if the input is shorter than the expected number length
        if inp.__len__() < maxNumOfLetters:
            res = isNumber(inp)  # Validate if the input is a valid number
            if res[0]:
                # Check if number is within range
                if (res[1] <= max and res[1] >= min):
                    return res[1]
                else:
                    print("Number is not in the asked range...\nTry again.")
            else:
                print("Input is not a valid number...\nTry again.")
        else:
            print("Invalid input...\nTry again.")


# Checks if a string represents a valid integer number (including optional leading '-').
# Returns a tuple:
#   ret[0] = True/False (whether input is a valid number)
#   ret[1] = the integer value if valid, 0 otherwise
def isNumber(str=""):
    ret = [0, 0]        # Default: invalid number, value = 0
    negFlag = 0         # Flag for negative number
    isNum = 1           # Assume it's a number until proven otherwise
    tmpNum = 0          # Temporary number being built
    numLen = 0          # Keeps track of how many digits seen (for powers of 10)

    for i in range(0, str.__len__()):
        if i == 0 and str[0] == '-':
            negFlag = 1  # Allow a negative sign at the beginning
        elif str[i].isdigit():
            # Build the number from digits, multiplying existing by powers of 10
            tmpNum = tmpNum * pow(10, numLen) + int(str[i])
            numLen += 1
        else:
            isNum = 0  # Found a non-digit character => invalid number
            break

    # Convert result to negative if needed
    ret[0] = isNum
    if isNum:
        tmpNum = tmpNum * -1 if negFlag else tmpNum
        ret[1] = int(tmpNum)
    return ret


# Calculates how many digits are in a number (accounting for sign)
# Returns 1 for 0, or number of digits + 1 if negative
def _getNumberLength(num=0):
    n = 0 if num > 0 else 1  # Start at 1 if negative to count the '-' sign

    while num:
        n += 1
        num /= 10  # Integer division would be better here (//)

    return 1 if n == 0 else n

# Calculates how many digits are in a number (accounting for sign)
# Returns 1 for 0, or number of digits + 1 if negative
def _getNumberLength(num=0):
    n = 0 if num > 0 else 1  # Start at 1 if negative to count the '-' sign

    while num:
        n += 1
        num /= 10  # Integer division would be better here (//)

    return 1 if n == 0 else n
