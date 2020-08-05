# importing the pynput module for validating the inputs.

from pynput import check_input

# def check_input(prompt, type_=None):
#     '''
#     Takes two inputs, a user input c, f, or k for temperature unit and a float number that needs to be converted
#     a type either str or float to validate the input
#     '''
#     temp_u = ('c', 'f', 'k')
#     while True:
#         user_input = input(prompt)
#         if type_ is not None:
#             try:
#                 user_input = type_(user_input)
#             except ValueError:
#                 print('Please enter a valid input.')
#                 continue
#         if isinstance(user_input, str) and user_input not in temp_u:
#             print("Please enter 'c', 'f', or 'k'")
#             continue
#         return user_input
temp_u = {'c', 'f', 'k'}

print('Temperature conversion utility')

base_temp = check_input("Enter c or f or k for base unit : ", operator=temp_u, value=str.lower)
convert_to = check_input("Enter c or f or k to which you wish to convert : ", operator=temp_u, value=str.lower)
temperature = check_input("Enter the unit value you wish to convert : ", value=float)

# base_temp = check_input("Enter c or f or k for base unit : ", str.lower)
# convert_to = check_input("Enter c or f or k to which you wish to convert : ", str.lower)
# temperature = check_input("Enter the unit value you wish to convert : ", float)

# three different functions that each converts from celsius, fahrenheit, or kelvin to the other
def from_c(temp, convert_from):
    if convert_from == 'f':
        return f'{temp * (9/5) + 32:.2f}'
    elif convert_from == 'k':
        return f'{temp + 273.15:.2f}'


def from_f(temp, convert_from):
    if convert_from == 'c':
        return f'{temp - 32 * (5/9):.2f}'
    elif convert_from == 'k':
        return f'{temp + 459.67 * (5/9):.2f}'


def from_k(temp, convert_from):
    if convert_from == 'f':
        return f'{temp * (9/5) - 459.67:.2f}'
    elif convert_from == 'c':
        return f'{temp - 273.15:.2f}'

# based on user input invokes the functions with correct formats
if base_temp == 'c' and convert_to == 'f':
    print(f"{temperature} degree celsius converts to {from_c(temperature, convert_to)} degree fahrenheit")
if base_temp == 'c' and convert_to == 'k':
    print(f"{temperature} degree celsius converts to {from_c(temperature, convert_to)} degree kelvin")
if base_temp == 'f' and convert_to == 'c':
    print(f"{temperature} degree fahrenheit converts to {from_f(temperature, convert_to)} degree celsius")
if base_temp == 'f' and convert_to == 'k':
    print(f"{temperature} degree fahrenheit converts to {from_f(temperature, convert_to)} degree kelvin")
if base_temp == 'k' and convert_to == 'f':
    print(f"{temperature} degree kelvin converts to {from_k(temperature, convert_to)} degree fahrenheit")
if base_temp == 'k' and convert_to == 'c':
    print(f"{temperature} degree kelvin converts to {from_k(temperature, convert_to)} degree celsius")
