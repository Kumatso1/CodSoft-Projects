import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be greater than zero.")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))
        return

    complexity = complexity_var.get()
    characters = string.ascii_letters  # Basic complexity: letters

    if complexity == "medium":
        characters += string.digits  # Add digits for medium complexity
    elif complexity == "high":
        characters += string.digits + "!@$&"  # Add digits and only !, @ for high complexity

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=f"Generated Password: {password}")

# Set up the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.config(bg="gold")
# Create widgets
instructions_label = tk.Label(root, text="Enter the desired length of the password:",bg="orange",fg="white")
instructions_label.pack()

length_entry = tk.Entry(root,bg="aquamarine")
length_entry.pack()

complexity_var = tk.StringVar(value="basic")
complexity_frame = tk.LabelFrame(root, text="Complexity",bg="brown",fg="white")
complexity_frame.pack(padx=10, pady=10)

basic_radio = tk.Radiobutton(complexity_frame, text="Basic (Letters only)",bg="silver",fg="blue", variable=complexity_var, value="basic")
basic_radio.pack(anchor="w")
medium_radio = tk.Radiobutton(complexity_frame, text="Medium (Letters and digits)",bg="silver",fg="blue", variable=complexity_var, value="medium")
medium_radio.pack(anchor="w")
high_radio = tk.Radiobutton(complexity_frame, text="High (Letters, digits, and allowable punctuation",bg="silver",fg="blue", variable=complexity_var, value="high")
high_radio.pack(anchor="w")

generate_button = tk.Button(root, text="Generate Password",bg="brown",fg="white", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="", bg="green",fg="white")
password_label.pack()

# Run the application
root.mainloop()
