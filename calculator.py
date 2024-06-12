import tkinter as tk
from tkinter import messagebox
import math

# Function to update the entry field
def click_button(item):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(item))

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to delete the last character in the entry field
def delete_last():
    current = entry.get()
    if len(current) > 0:
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])

# Function to evaluate the expression
def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")

# Function for square operation
def square():
    try:
        current = entry.get()
        result = float(current) ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")

# Function for square root operation
def sqrt():
    try:
        current = entry.get()
        result = math.sqrt(float(current))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")

# Set up the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create entry field
entry = tk.Entry(window, font=("Arial", 20), borderwidth=2, relief="solid",bg="aquamarine")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, sticky="nsew")

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
    ('.', 4, 0), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3), ('=', 4, 2),
    ('C', 5, 0), ('←', 5, 1), ('x²', 5, 2), ('√', 5, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(window, text=text, font=("Arial", 18), bg="lightblue", command=evaluate)
    elif text == 'C':
        btn = tk.Button(window, text=text, font=("Arial", 18), bg="lightcoral", command=clear_entry)
    elif text == '←':
        btn = tk.Button(window, text=text, font=("Arial", 18), bg="lightcoral", command=delete_last)
    elif text == 'x²':
        btn = tk.Button(window, text=text, font=("Arial", 18), bg="lightgreen", command=square)
    elif text == '√':
        btn = tk.Button(window, text=text, font=("Arial", 18), bg="lightgreen", command=sqrt)
    else:
        btn = tk.Button(window, text=text, font=("Arial", 18), bg="skyblue", command=lambda t=text: click_button(t))

    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Configure grid
for i in range(6):
    window.grid_rowconfigure(i,weight=1)
for i in range(4):
    window.grid_columnconfigure(i,weight=1)

# Start the Tkinter event loop
window.mainloop()
