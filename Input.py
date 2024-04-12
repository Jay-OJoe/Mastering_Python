# Function to get numbers from the user
def get_numbers():
    input_strings = input("Type here: ")
    list_of_strings = input_strings.split()
    list_of_numbers = [float(num) for num in list_of_strings]
    return list_of_numbers

list_of_numbers = get_numbers()

# Function to calculate the sum of a list of numbers
def calculate_sum(any_list_of_number):
    total = sum(any_list_of_number)
    return total

total = calculate_sum(list_of_numbers)

# Function to display the sum to the user
def display_result(numbers, result):
    print('The sum of {} is {}'.format(numbers, result))

def main():
list_of_numbers = get_numbers()
total = calculate_sum(list_of_numbers)