def remove_chars(input_string, n):
    # Check if n is less than the length of the string
    if n < len(input_string):
        # Remove characters from the start up to n and return the new string
        result = input_string[n:]
        return result
    else:
        # If n is greater than or equal to the length, return an error message
        return "Error: n must be less than the length of the string."

# Test cases
result1 = remove_chars("pynative", 4)
print(result1)  # Output: tive

result2 = remove_chars("pynative", 2)
print(result2)  # Output: native

result3 = remove_chars("pynative", 10)
print(result3)  # Output: Error: n must be less than the length of the string.
