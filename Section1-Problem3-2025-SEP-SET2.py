def word_sandwich(bread, filling):
    '''
    Given two strings, `bread` and `filling`, split `bread` into two equal halves
    and insert `filling` in between to make a new word.

    Example:
        >>> bread = "topbun"
        >>> filling = "butter"
        >>> word_sandwich(bread,filling)
        'topbutterbun'

    Args:
        bread (str): The outer string (always even length).
        filling (str): The middle string to insert.

    Returns:
        str: A new string formed by inserting `filling` between the halves of `bread`.
    '''
    
    
    half = len(bread) // 2
    return bread[:half] + filling + bread[half:]


# Word Sandwich
# Given two strings, bread and filling, split bread into two equal halves and insert the filling in between them to form a new word.\

# Assume the string bread will be of even length.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> bread = "topbun"
# >>> filling = "butter"
# >>> word_sandwich(bread,filling)
# 'topbutterbun'
