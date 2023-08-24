from tkinter import *
import math as m

def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old + to_print)

def sc(event):
    key = event.widget
    text = key['text']
    no = e.get()
    result = ''

    if text == 'log':
        result = str(m.log10(float(no)))
    elif text == 'ln':
        result = str(m.log(float(no)))
    elif text == 'sin':
        if no:
            result = str(m.sin(m.radians(float(no))))
    elif text == 'cos':
        result = str(m.cos(m.radians(float(no))))
    elif text == 'tan':
        result = str(m.tan(m.radians(float(no))))
    elif text == 'Sqrt':
        result = str(m.sqrt(float(no)))
    elif text == 'x!':
        result = str(m.factorial(int(no)))
    elif text == '1/x':
        result = str(1 / float(no))
    elif text == 'pi':
        result = str(m.pi * float(no)) if no else str(m.pi)
    elif text == 'e':
        result = str(m.e ** float(no)) if no else str(m.e)

    e.delete(0, END)
    e.insert(0, result)

def clear():
    e.delete(0, END)

def bksps():
    current = e.get()
    e.delete(len(current) - 1, END)

def evaluate():
    ans = e.get()
    ans = eval(ans)
    e.delete(0, "end")
    e.insert(0, ans)

root = Tk()
root.title("Scientific Calculator")

e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black", font=("Helvetica", 15))
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

button_bg = "cornflowerblue"
result_bg = "White"

button_font = ("Helvetica", 12, "bold")

buttons = [
    ("log", "log"), ("ln", "ln"), ("(", "("), (")", ")"), (".", "."), ("e", "e"),
    ("^", "**"), ("sin", "sin"), ("cos", "cos"), ("tan", "tan"),
    ("Sqrt", "Sqrt"), ("%", "%"), ("mod", "mod"), ("/", "/"), ("1/x", "1/x"),
    ("-", "-"), ("+", "+"), ("pi", "pi"), ("x!", "x!"), ("*", "*"),
    ("9", "9"), ("8", "8"), ("7", "7"), ("6", "6"), ("5", "5"),
    ("4", "4"), ("3", "3"), ("2", "2"), ("1", "1"), ("0", "0"),
    ("$", "$"), ("Math", "Math"), ("Stat", "Stat"), ("Tnq", "Tnq"),
    ("sin 0°", "0"), ("sin 30°", "1/2"), ("sin 45°", "0.7071"),
    ("sin 60°", "0.8660"), ("sin 90°", "1.0000"),
    ("cos 0°", "1"), ("cos 30°", "0.8660"), ("cos 45°", "0.7071"),
    ("cos 60°", "0.5000"), ("cos 90°", "0.0000"),
    ("tan 0°", "0"), ("tan 30°", "0.5774"), ("tan 45°", "1.0000"),
    ("tan 60°", "1.7321"), ("tan 90°", "Undefined")
]


row_counter = 1
col_counter = 0

for label, value in buttons:
    button = Button(root, text=label, padx=20, pady=10, relief=RAISED, font=button_font, bg=button_bg, command=lambda v=value: button_click(v))
    button.grid(row=row_counter, column=col_counter, sticky="nsew")

    col_counter += 1
    if col_counter > 4:
        col_counter = 0
        row_counter += 1

clear_button = Button(root, text="C", padx=29, pady=10, relief=RAISED, command=clear, font=button_font, bg=button_bg)
backspace_button = Button(root, text="Bksp", padx=19, pady=10, relief=RAISED, command=bksps, font=button_font, bg=button_bg)
equal_button = Button(root, text="=", padx=29, pady=10, relief=RAISED, command=evaluate, font=button_font, bg=button_bg)

clear_button.grid(row=4, column=1, sticky="nsew")
backspace_button.grid(row=4, column=2, sticky="nsew")
equal_button.grid(row=7, column=3, sticky="nsew")

e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)
e.config(fg="Black", bg=result_bg, justify=RIGHT)

def button_click(value):
    if value.startswith("sin ") or value.startswith("cos ") or value.startswith("tan "):
        # Extract the angle from the button text
        operation, angle_text = value.split()[:2]  # Extract operation and angle text
        angle = int(angle_text[:-1])  # Extract the angle value
        # Calculate the trigonometric ratio
        if operation == "sin":
            result = m.sin(m.radians(angle))
        elif operation == "cos":
            result = m.cos(m.radians(angle))
        elif operation == "tan":
            result = m.tan(m.radians(angle))
        e.delete(0, END)
        e.insert(0, result)
    else:
        if value == "=":
            evaluate()
        elif value == "Bksp":
            bksps()
        else:
            click(value)



root.mainloop()
