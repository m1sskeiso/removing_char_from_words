# Define a function remove characters
def remove_chars(input_string, n):

    
    # Check if n is less than the length of the string
    if n < len(input_string)

# Remove characters from the start up to n and return the new string
        result = input_string[n:]
        return result

# If n is greater than or equal to the length, return an error message
    else:
         return "Error: n must be less than the length of the string."
# Test cases


