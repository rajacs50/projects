# Attempt at creating a generic input sanitizer
# Take in an input, check the type of it
# based on the type, perform operations

# Sample input:
# prompt = check_input('Please enter a value: ', {set of operators}, str)
''' Takes input from the user and validates it '''


def check_input(prompt, operator=None, value=None):
    '''
    Takes user input and a type for that value and validates it
    '''
    if operator is not None:
        operator = set(operator)
    while True:
        user_input = input(prompt)
        if value is not None:
            try:
                user_input = value(user_input)
            except ValueError:
                print('Invalid input. Refer to the instructions.')
                continue
        if operator is not None and user_input not in operator:
            print(f'Please enter any one of the allowed operators: {operator}')
            continue
        return user_input
