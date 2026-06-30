# Problem 1: Given a list of numbers. Write a function to turn every item of 
# a list into its square.
def square_list(my_list):
    """
    input: list of int
    returns the square of the items
    """
    new_list = [x**2 for x in my_list]
    return new_list

# test
# print(square_list([1, 2, 3, 4]))
# print(square_list([10, 12, 13]))



# Problem 2: Write a Python program to concatenate element-wise 
# three given lists of same length
# Original lists:
list1 = ['0', '1', '2', '3', '4']
list2 = ['red', 'green', 'black', 'blue', 'white']
list3 = ['100', '200', '300', '400', '500']
# Expected output : ['0red100', '1green200', '2black300', '3blue400', '4white500']

def concatenate_lists(list_a, list_b, list_c):
    """
    input: 3 lists of str with same len,
    concatenates the indexes and 
    returns the new elements
    """
    new_L = []
    for index in range(len(list_a)):
        # concatenate the indexes from 3 lists...
        combined = list_a[index] + list_b[index] + list_c[index]
        new_L.append(combined)

    return new_L
    

# test
# print(concatenate_lists(list1, list2, list3))




# Problem 3: Write a function to shift a given list to the right or left 
# direction by a specified amount. Direction, rotation amount, and a 
# list of integers should be inputs to the function.
# e.g. 
# Input list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Rotate the input list in left direction by 2:
# [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
# Rotate the input list in Right direction by 4:
# [7, 8, 9, 10, 1, 2, 3, 4, 5, 6]

# edit this to be "right" or "left"
direction = "right" 

def rotate_list(input_list, direction, shift):
    # def right or left dir
    new_L = []
    lis_copy = input_list[:]
    
    shift = shift % len(input_list)
    if direction == "left":
        new_L = lis_copy[shift:] + lis_copy[:shift]
    elif direction == "right":
        new_L = lis_copy[-shift:] + lis_copy[:-shift]
    return new_L
        

# test 
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(rotate_list(input_list, "right", 14))
print(rotate_list(input_list, "left", 4))


