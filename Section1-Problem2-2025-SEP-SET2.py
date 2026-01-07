def get_first_last_chars_sorted(t: tuple) -> str:
    '''
    Takes a tuple of at least two strings and returns a string formed by
    the first character of the first string and the last character
    of the last string, arranged in alphabetical order.

    Args:
        t (tuple): A tuple containing at least two strings.

    Returns:
        str: Two characters in alphabetical order.
    '''
    
    
    a, b = t[0][0],t[-1][-1]
    return a+b if a<b else b+a
    

# Get First and Last Characters Sorted
# Write a function get_first_last_chars_sorted(t) that takes a tuple of strings (with at least two strings) as input and returns a new string formed by:

# taking the first character of the first string, and
# the last character of the last string,
# Then, return these two characters arranged in alphabetical order.
# (Assume all strings are in lowercase.)

# Hint: Alphebetical order can be determined by comparing two chars using comparision operators.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Examples

# get_first_last_chars_sorted(("apple", "banana", "cherry")) -> "ay"
# First char of "apple" -> 'a', last char of "cherry" -> 'y'
# Sorted alphabetically -> "ay"
# get_first_last_chars_sorted(("moon", "sun")) -> "mn"
# First char of "moon" -> 'm', last char of "sun" -> 'n'
# Sorted alphabetically -> "mn"
# get_first_last_chars_sorted(("land", "cab")) -> "bl"
# First char of "land" -> 'l', last char of "cab" -> 'b'
# Sorted alphabetically -> "bl"
