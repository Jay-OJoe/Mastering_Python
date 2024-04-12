#function get_numbers()
def get_numbers():
    # Ask the user for input using the input() method
    # Save it in the input_string variable
    input_string = input("Type your numbers here:")
    # Convert the input_string 2to a list of strings by splitting it into separate strings using split()
    # Save it in the list_of_strings vatriable
    list_of_strings = input_string.split()
    # Converts the list of strings to a list of numbers by using the int() method
    # Save it in the numbers variable
    numbers = [int(num) for num in list_of_strings]
    # return the list of numbers
    return numbers
  
get_numbers()
   