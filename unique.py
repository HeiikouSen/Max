numbers = [2, 2, 3, 3, 4, 5, 7]

def get_unique_element(numbers):

    unique_element = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        unique_element.append(number)
    return unique_element

print((get_unique_element(numbers)))