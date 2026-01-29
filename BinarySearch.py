
def linear_search(arr, target):
    """
    Perform a linear search on the given array.

    Parameters:
    arr (list): The list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.

    Hear we have order of n time complexity because in worst case we have to traverse the whole array to find the target value.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

def binary_search(number_list, number_to_find):
    """
    Perform a binary search on the given sorted array.

    Parameters:
    number_list (list): The sorted list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.

    Here we have order of log n time complexity because with each comparison we halve the search space.

    """
    left_index, right_index = 0, len(number_list) - 1
    while left_index <= right_index:
        mid = (left_index + right_index) // 2
        if number_list[mid] == number_to_find:
            return mid
        elif number_list[mid] < number_to_find:
            left_index = mid + 1
        else:
            right_index = mid - 1
    return -1

def binary_search_recursive(number_list, number_to_find, left_index, right_index):
    """
    Perform a binary search on the given sorted array using recursion.

    Parameters:
    number_list (list): The sorted list to search through.
    target: The value to search for.
    left_index (int): The left boundary of the search space.
    right_index (int): The right boundary of the search space.

    Returns:
    int: The index of the target if found, otherwise -1.

    Here we have order of log n time complexity because with each comparison we halve the search space.

    """ 

    if left_index > right_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if number_list[mid_index] == number_to_find:
        return mid_index
    elif number_list[mid_index] < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(number_list, number_to_find, left_index, right_index)

 

def convert_to_sorted_list(unsorted_list):
    """
    Convert an unsorted list to a sorted list.

    Parameters:
    unsorted_list (list): The unsorted list.

    Returns:
    list: A sorted version of the input list.
    """
    return sorted(unsorted_list)

def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

if __name__ == "__main__":
    # Example usage of linear_search
    sorted_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    sorted_list = convert_to_sorted_list(sorted_list)
    result_index = linear_search(sorted_list, 5)
    if result_index != -1:
        print(f"Linear Search: Found 5 at index {result_index}.")
    else:
        print(f"Linear Search: 5 not found in the list.")

    # Example usage of binary_search
    
    number_to_find = 5
    result_index = binary_search(sorted_list, number_to_find)
    if result_index != -1:
        print(f"Binary Search: Found {number_to_find} at index {result_index}.")
    else:
        print(f"Binary Search: {number_to_find} not found in the list.")

    # Example usage of binary_search_recursive
    result_index = binary_search_recursive(sorted_list, number_to_find, 0, len(sorted_list) - 1)
    if result_index != -1:
        print(f"Binary Search Recursive: Found {number_to_find} at index {result_index}.") 
    else:
        print(f"Binary Search Recursive: {number_to_find} not found in the list.")

# Example usage of find_all_indices 
    number_to_find = 15
    result_index = find_all_occurances(sorted_list, number_to_find)
    if result_index != -1:
        print(f"Binary Search: Found {number_to_find} at index {result_index}.")
    else:
        print(f"Binary Search: {number_to_find} not found in the list.")