# https://github.com/israel-dryer/PyDataMath-II/blob/master/calculator_tk.py
# https://www.youtube.com/watch?v=YXPyB4XeYLA
# http://www.obeythetestinggoat.com/book/video_plug.html

# To do
# handle chain calculations i.e. 1 + 2 - 1 * 10 / 2 etc...
# Another line above the current entry?

import tkinter as tk

wyt = "#F8F8F8"
tan = "#F1EABC"
vard = {'front': [], 'back': [], 'decimal': False,
        'x_val': 0.0, 'y_val': 0.0, 'res': 0.0, 'op': ''}

root = tk.Tk()
root.title('Calculator')
root.config(bg='#272533')

display_text = tk.StringVar()
display_text.set('0')


canvas = tk.Canvas(bg='#272533', bd=0, highlightthickness=0)
canvas.pack(padx=15, pady=15)


def std_btn(text, bg, row, col, width=5, height=1, font=('Digital-7', 24)):
    btn = tk.Button(canvas, text=text, bg=bg, width=width,
                    height=height, font=font, command=lambda: event_click(text))
    return btn.grid(row=row, column=col, padx=4, pady=4)


tk.Label(canvas, text='PyDataMath', anchor='e', bg='#272533', fg='white', font=(
    'Franklin Gothic Book', 14, 'bold')).grid(row=0, columnspan=4, sticky='ew', padx=4, pady=2)
tk.Label(canvas, textvariable=display_text, anchor='e', bg='black', fg='red', font=(
    'Digital-7', 47)).grid(row=1, columnspan=4, sticky='ew', padx=4, pady=2)

# Clear entire field
std_btn('C', tan, 2, 0)
# Clear last input entry
std_btn('CE', tan, 2, 1)
std_btn('%', tan, 2, 2)
std_btn('/', tan, 2, 3)

std_btn('7', wyt, 3, 0)
std_btn('8', wyt, 3, 1)
std_btn('9', wyt, 3, 2)
std_btn('*', tan, 3, 3)

std_btn('4', wyt, 4, 0)
std_btn('5', wyt, 4, 1)
std_btn('6', wyt, 4, 2)
std_btn('-', tan, 4, 3)

std_btn('1', wyt, 5, 0)
std_btn('2', wyt, 5, 1)
std_btn('3', wyt, 5, 2)
std_btn('+', tan, 5, 3)

std_btn('0', wyt, 6, 0)
std_btn('.', wyt, 6, 1)

rtn_btn = tk.Button(canvas, text='=', bg='#ECA527', width=11, height=1, font=(
    'Digital-7', 24), command=lambda: event_click("="))
rtn_btn.focus()
rtn_btn.grid(row=6, column=2, columnspan=2, padx=4, pady=4)


# Trigger Calculate Functions based on user input
def event_click(event):
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        number_click(event)
    elif event in ['*', '/', '+', '-']:
        op_click(event)
    elif event == '.':
        vard['decimal'] = True
    elif event == '%':
        update_display(vard['result'] / 100.00)
    elif event == 'C':
        clear_click()
        update_display(0)
        vard['op'] = ''
        vard['res'] = 0
    elif event == 'CE':
        clear_click()
        update_display(0)
    elif event == '=':
        calculate_click()


# Calculate functions:
def update_display(display_value):
    # Set the calculator display
    try:
        display_text.set(f'{display_value}')
    except:
        display_text.set(display_value)


def format_number():
    # return f"{''.join(vard['front'])} . {''.join(vard['back'])}"
    return ''.join(vard['front']) + '.' + ''.join(vard['back'])

# Click Events


def number_click(event):
    # Adding digits before or after decimal based on user input
    if vard['decimal']:
        vard['back'].append(event)
    else:
        vard['front'].append(event)

    display_value = float(format_number())
    update_display(display_value)


def clear_click():
    # reset the input field and set the decimal back to False
    vard['back'].clear()
    vard['front'].clear()
    vard['decimal'] = False


def op_click(event):
    vard['op'] = event
    try:
        vard['x_val'] = float(format_number())
    except:
        vard['x_val'] = vard['res']
    clear_click()


def calculate_click():
    # Calculate the result based on the inputs
    if not vard['x_val']:
        return
    try:
        vard['y_val'] = float(format_number())
    except:
        vard['y_val'] = 0
    try:
        vard['res'] = float(
            eval(str(vard['x_val']) + vard['op'] + str(vard['y_val'])))
        update_display(vard['res'])
    except ZeroDivisionError:
        error = 'Div / 0 Error'
        vard['x_eval'] = 0
        clear_click()
        update_display(error)
    clear_click()


root.mainloop()
