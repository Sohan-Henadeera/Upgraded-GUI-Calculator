import tkinter as tk
from tkinter import ttk

#Display
def press_key(key):
    if key == "C":
        display_var.set("")
    elif key == "=":
        try:
            result = eval(display_var.get())
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    else:
        current_text = display_var.get()
        display_var.set(current_text + key)

#Main
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.configure(bg="#3f4042")

operator_color = "#33e3d9" 
clear_color = "#f90000"
equal_color = "#33e3d9"
display_bg_color = "#8da2a1"

# ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 14), padding=10)

# Display
display_var = tk.StringVar()
display_entry = tk.Entry(
    root, textvariable=display_var, font=("Helvetica", 24), justify="right", bg=display_bg_color, relief="ridge"
)
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

#buttons
buttons = [
    ("7", None), ("8", None), ("9", None), ("/", operator_color),
    ("4", None), ("5", None), ("6", None), ("*", operator_color),
    ("1", None), ("2", None), ("3", None), ("-", operator_color),
    ("C", clear_color), ("0", None), ("=", equal_color), ("+", operator_color)
]

#Placement
row = 1
col = 0
for button, color in buttons:
    btn = tk.Button(
        root,
        text=button,
        command=lambda key=button: press_key(key),
        font=("Helvetica", 14),
        bg=color if color else "#ffffff",
        relief="ridge"
    )
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

#Configure rows and columns
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
