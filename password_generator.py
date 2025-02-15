import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the password length.")
        return
    
    # Build the character pool based on selected options.
    pool = ""
    if lower_var.get():
        pool += string.ascii_lowercase
    if upper_var.get():
        pool += string.ascii_uppercase
    if digits_var.get():
        pool += string.digits
    if punctuation_var.get():
        pool += string.punctuation
    
    if not pool:
        messagebox.showerror("No Characters Selected", "Please select at least one character set.")
        return

    # Generate the password.
    password = ''.join(secrets.choice(pool) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        # Clear the clipboard and then append the new password.
        app.clipboard_clear()
        app.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "No password to copy. Please generate one first.")

# Create the main window.
app = tk.Tk()
app.title("Password Generator by George G.")

# Password length label and entry.
tk.Label(app, text="Password Length:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1, padx=10, pady=5)
length_entry.insert(0, "12")  # Default length.

# Checkbox options for character sets.
lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
punctuation_var = tk.BooleanVar(value=True)

tk.Checkbutton(app, text="Include Lowercase", variable=lower_var).grid(row=1, column=0, padx=10, sticky="w")
tk.Checkbutton(app, text="Include Uppercase", variable=upper_var).grid(row=1, column=1, padx=10, sticky="w")
tk.Checkbutton(app, text="Include Digits", variable=digits_var).grid(row=2, column=0, padx=10, sticky="w")
tk.Checkbutton(app, text="Include Special Characters", variable=punctuation_var).grid(row=2, column=1, padx=10, sticky="w")

# Button to generate the password.
tk.Button(app, text="Generate Password", command=generate_password).grid(row=3, column=0, columnspan=2, pady=10)

# Display the generated password.
password_var = tk.StringVar()
password_entry = tk.Entry(app, textvariable=password_var, width=40)
password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Button to copy the generated password to the clipboard.
tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=5, column=0, columnspan=2, pady=10)

app.mainloop()
