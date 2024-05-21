def ascii_mapping(input_string):
    # Initialize an empty list to store ASCII values
    ascii_values = []
    
    # Iterate over each character in the input string
    for char in input_string:
        # Get the ASCII value of the character and append it to the list
        ascii_values.append(ord(char))
    
    # Return the list of ASCII values
    return ascii_values
def from_ascii_mapping(ascii_values):
    # Initialize an empty string to store the reconstructed string
    reconstructed_string = ""
    
    # Iterate over each ASCII value in the list
    for ascii_val in ascii_values:
        # Convert the ASCII value to its corresponding character and append it to the string
        reconstructed_string += chr(ascii_val)
    
    # Return the reconstructed string
    return reconstructed_string


# Example usage
input_string = "Criptografia"
mapped_values = ascii_mapping(input_string)
print(mapped_values)
original_string = from_ascii_mapping(mapped_values)
#print(original_string)