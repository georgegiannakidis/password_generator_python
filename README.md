# Tkinter Password Generator

A simple, secure password generator with a graphical user interface built using Python's Tkinter library.

![image](https://github.com/user-attachments/assets/e60b9220-a331-4b34-b1c7-9a95b7adf43c)

## Overview

This project provides a user-friendly GUI that lets you generate a secure password with customizable options:
- **Password Length:** Specify the number of characters.
- **Character Sets:** Choose whether to include lowercase, uppercase, digits, and special characters.
- **Copy Functionality:** Easily copy the generated password to your clipboard with a click.

The application leverages Python's built-in `secrets` module for cryptographically secure password generation.

## Features

- **Simple GUI:** Easy-to-use interface built with Tkinter.
- **Customizable Options:** Adjust the length and types of characters included.
- **Clipboard Integration:** Copy the generated password to the clipboard with a single button click.
- **Error Handling:** Alerts for invalid input or when no character set is selected.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/tkinter-password-generator.git
   cd tkinter-password-generator

2. **Run the Application:**
Ensure you have Python installed (Python 3.x recommended).
   ```bash
   python password_generator_ui.py
Note: Tkinter comes bundled with most Python installations. If you're on Linux and encounter issues, you might need to install it (e.g., sudo apt-get install python3-tk).
