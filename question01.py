# 1.   Replacing characters in place:
# Given an array of characters, write a method to replace all the spaces with “&32”.
# You may assume that the array has sufficient slots at the end to hold the additional
# characters, and that you are given the “true” length of the array. (Please perform this
# operation in place with no other auxiliary structure).
# Example:
# Input: “User is not allowed      “, 19
# Output: “User&32is&32not&32allowed”

def array_shift_right(arr, pos):
    for i in reversed(range(pos+1, len(arr))):
        arr[i] = arr[i-1]

def array_shift(arr, pos, count):
    for i in range(count):
        array_shift_right(arr, pos)

def replace_in_place(arr, length, search, new_elements):
    new_elements_count = len(new_elements)

    # Repeat while there are still elements to replace
    while True:
        elements_added = 0
        replaced = False
        for i in range(length):
            # Item was found
            if arr[i] == search:
                replaced = True

                # Open space on the array for the new elements
                if elements_added == 0:
                    array_shift(arr, i, new_elements_count - 1)

                # Replaces search with the new elements
                if(elements_added < new_elements_count):
                    arr[i] = new_elements[elements_added]
                    elements_added += 1

        # If not replace was made, end loop
        if not replaced:
            break

def replace_spaces(text, true_length):
    # Convert text to array
    text_array = list(text)

    # Convert replacemente to array
    replacement = list("&32")

    # Call replace on place algorithm
    replace_in_place(text_array, true_length, " ", replacement)

    # Convert text array to string
    output = "".join(text_array)
    return output

result = replace_spaces("User is not allowed      ", 19)
print(result)
