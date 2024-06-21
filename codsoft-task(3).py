import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    char_sets = []
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_special:
        char_sets.append(string.punctuation)
    
    if not char_sets:
        raise ValueError("At least one character set must be selected.")
    
    all_chars = ''.join(char_sets)
    if length < len(char_sets):
        raise ValueError("Password length should be at least equal to the number of selected character sets.")

    password = [random.choice(char_set) for char_set in char_sets]
    password += random.choices(all_chars, k=length-len(password))
    
    random.shuffle(password)
    return ''.join(password)

def on_generate():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Length must be a positive integer.")
        
        use_upper = var_upper.get()
        use_lower = var_lower.get()
        use_digits = var_digits.get()
        use_special = var_special.get()
        
        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        result_label.config(text=password, fg='green')
    except ValueError as ve:
        messagebox.showerror("Error", f"Invalid Input: {ve}")

def copy_to_clipboard():
    password = result_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.configure(bg='#f0f0f0')

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg='#f0f0f0')
title_label.pack(pady=10)

# Length Entry
tk.Label(root, text="Enter the desired length of the password:", bg='#f0f0f0').pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Checkboxes for character sets
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper, bg='#f0f0f0').pack(pady=2)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower, bg='#f0f0f0').pack(pady=2)
tk.Checkbutton(root, text="Include Digits", variable=var_digits, bg='#f0f0f0').pack(pady=2)
tk.Checkbutton(root, text="Include Special Characters", variable=var_special, bg='#f0f0f0').pack(pady=2)

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=on_generate, bg='#4caf50', fg='white', font=("Helvetica", 12, "bold"))
generate_button.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", bg='#f0f0f0', font=("Helvetica", 14, "bold"))
result_label.pack(pady=10)

# Copy to Clipboard Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg='#2196F3', fg='white', font=("Helvetica", 12, "bold"))
copy_button.pack(pady=10)

# Run the application
root.mainloop()