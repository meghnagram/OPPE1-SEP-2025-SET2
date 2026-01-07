def extract_middle_elements(lst:list):
    """
    Extracts the middle element(s) from a list of integers.

    Args:
        lst (list): The list of integers.

    Returns:
        list: A list containing either the middle element (if odd length) or 
        the two middle elements (if even length).
    """
    
    
    n = len(lst)
    if n % 2 == 1:  # Odd length
        return [lst[n // 2]]
    else:  # Even length
        return [lst[(n // 2) - 1], lst[n // 2]]
    

# Middle element from list
# Write a function extract_middle_elements(lst:list) that takes a list of integers and returns a new list containing only the middle element if the list has an odd length, or the two middle elements if the list has an even length.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Examples

# extract_middle_elements([7, 8, 9, 10, 11, 12, 13]) -> [10]
# Explanation: The list has an odd length (7), so the middle element is 10.
# extract_middle_elements([3, 6, 9, 12, 15, 18]) -> [9, 12]
Explanation: The list has an even length (6), so the two middle elements are 9 and 12.
