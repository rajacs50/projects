# importing the pynput module for validating the inputs.

from pynput import check_input


# def check_input(prompt, value=None):
#     '''
#     Takes the user input and validates it.
#     Accepts floats and one of the arithmetic operators
#     '''
#     print()
#     print('prompt: ', prompt, 'value: ', value)
#     print()
#     op = ['+', '-', '/', '*']
#     while True:
#         user_input = input(prompt)
#         if value is not None:
#             try:
#                 user_input = value(user_input)
#             except ValueError:
#                 print('Invalid input. Refer to the instructions.')
#                 continue
#         if isinstance(user_input, str) and user_input not in op:
#             print('Please enter any one of the allowed operators: +, -, /, *')
#             continue
#         return user_input
ope = ['+', '-', '/', '*']


def instructions():
    print('''Instructions:
        Enter the numbers that you want to operate on, and the symbol of the operation.
        e.g. 1 2 +
        Allowed operators: +, -, /, *''')


def calc(a, b, op):
    '''Input a number another number and then the arithmetic operator'''
    if op == '+':
        return f"{a} plus {b} equals {a + b}"
    elif op == '-':
        return f"{a} minus {b} equals {a - b}"
    elif op == '/':
        return f"{a} divided by {b} equals {a / b}"
    elif op == '*':
        return f"{a} multiplied by {b} equals {a * b}"
    else:
        return '(Inside calc) Invalid input. Refer to the instructions.'


# def user_input_func():
#     instructions()
#     a = check_input('Enter the first number: ', float)
#     b = check_input('Enter the second number: ', float)
#     op = check_input('Enter the operator: ', str)
#     print(calc(a, b, op))


def user_input_func():
    instructions()
    a = check_input('Enter the first number: ', value=float)
    b = check_input('Enter the second number: ', value=float)
    op = check_input('Enter the operator: ', operator=ope, value=str)
    print(calc(a, b, op))


user_input_func()
