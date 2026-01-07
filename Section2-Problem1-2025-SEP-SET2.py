
def average_of_negative_evens(nums: list) -> float:
    '''Return the average of all negative even numbers in the list.'''
    
    
    negative_evens = [n for n in nums if n < 0 and n%2==0]
    if not negative_evens:
        return 0
    return sum(negative_evens) / len(negative_evens)
    

# #Another Method:


# def average_of_negative_evens(nums: list) -> float:
#     '''Return the average of all negative even numbers in the list.'''
    
    
#     z=list(filter(lambda x: x<0 and x%2==0 ,nums))
#     if len(z)==0:
#         return 0
#     else:
#         return sum(z)/len(z)

#   Average of Negative Even Numbers
# Write a function average_of_negative_evens that takes a list of integers nums and returns the average of all negative even numbers in the list.
# If there are no negative even numbers, return 0.

# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> nums = [1, -2, -3, 0, 4, -5, -6]
# >>> average_of_negative_evens(nums)
# -4.0
Explanation: Negative numbers: -2, -6 Average = (-2 + -6) / 2 = -8/2 = -4.0
