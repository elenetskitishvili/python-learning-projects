import tkinter as tk

calculation = ''

# Add a symbol (number or operator) to the calculation


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)

# When the equals button is pressed


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, 'Error')

# Clears the current calculation


def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')


# Set up the main window for the application
root = tk.Tk()
root.geometry('300x275')
root.minsize(width=300, height=275)  # Set a minimum window size
root.resizable(True, True)  # Allow window resizing

text_result = tk.Text(root, height=2, width=16, font=('Arial', 24))
text_result.grid(columnspan=5, sticky="nsew")

# Button symbols in a grid
buttons = [
    ('1', 2, 1), ('2', 2, 2), ('3', 2, 3), ('+', 2, 4),
    ('4', 3, 1), ('5', 3, 2), ('6', 3, 3), ('-', 3, 4),
    ('7', 4, 1), ('8', 4, 2), ('9', 4, 3), ('*', 4, 4),
    ('(', 5, 1), ('0', 5, 2), (')', 5, 3), ('/', 5, 4),
]

# Create buttons using a loop
for (symbol, row, col) in buttons:
    btn = tk.Button(root, text=symbol, command=lambda s=symbol: add_to_calculation(
        s), font=('Arial', 14))
    btn.grid(row=row, column=col, sticky="nsew")

# Configure grid to expand
for i in range(1, 5):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

# Clear and Equals buttons
btn_clear = tk.Button(root, text='C', command=clear_field, font=('Arial', 14))
btn_clear.grid(row=6, column=1, columnspan=2, sticky="nsew")
btn_equals = tk.Button(
    root, text='=', command=evaluate_calculation, font=('Arial', 14))
btn_equals.grid(row=6, column=3, columnspan=2, sticky="nsew")

# Start the Tkinter main loop to keep the app running
root.mainloop()
