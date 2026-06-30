import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("450x450")
root.config(bg="#2C3E50")

# Title
title = tk.Label(root,
                 text="Password Complexity Checker",
                 font=("Arial",16,"bold"),
                 bg="#2C3E50",
                 fg="white")
title.pack(pady=15)

# Password label
label = tk.Label(root,
                 text="Enter Password",
                 bg="#2C3E50",
                 fg="white",
                 font=("Arial",12))
label.pack()

# Password entry
entry = tk.Entry(root,
                 width=30,
                 show="*",
                 font=("Arial",12))
entry.pack(pady=10)

# Result
result = tk.Label(root,
                  text="Strength : ",
                  bg="#2C3E50",
                  fg="yellow",
                  font=("Arial",14,"bold"))
result.pack(pady=10)

# Suggestions
suggestion = tk.Label(root,
                      text="",
                      bg="#2C3E50",
                      fg="white",
                      font=("Arial",10))
suggestion.pack()

# Check password
def check_password():
    password = entry.get()

    score = 0
    tips = ""

    # Length
    if len(password) >= 8:
        score += 1
    else:
        tips += "• Minimum 8 characters\n"

    # Uppercase
    upper = False
    for ch in password:
        if ch.isupper():
            upper = True

    if upper:
        score += 1
    else:
        tips += "• Add uppercase letter\n"

    # Lowercase
    lower = False
    for ch in password:
        if ch.islower():
            lower = True

    if lower:
        score += 1
    else:
        tips += "• Add lowercase letter\n"

    # Number
    number = False
    for ch in password:
        if ch.isdigit():
            number = True

    if number:
        score += 1
    else:
        tips += "• Add number\n"

    # Special character
    special = "@#$%&*!"
    special_found = False

    for ch in password:
        if ch in special:
            special_found = True

    if special_found:
        score += 1
    else:
        tips += "• Add special character\n"

    # Show result
    if score <= 2:
        result.config(text="Strength : Weak", fg="red")
    elif score <= 4:
        result.config(text="Strength : Medium", fg="orange")
    else:
        result.config(text="Strength : Strong", fg="green")

    suggestion.config(text=tips)

# Button
button = tk.Button(root,
                   text="Check Password",
                   command=check_password,
                   bg="blue",
                   fg="white",
                   font=("Arial",12))
button.pack(pady=20)

root.mainloop()
