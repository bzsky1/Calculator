import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc['state'] = tk.NORMAL
    calc.delete(0, 'end')
    calc.insert(0, value + digit)
    calc['state'] = tk.DISABLED


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0, 'end')
    calc.insert(0, value + operation)
    calc['state'] = tk.DISABLED


def calculate():
    value = calc.get()
    if value[-1] in '-+/*':
        value = value + value[:-1]
    calc['state'] = tk.NORMAL
    calc.delete(0, 'end')
    try:
        calc.insert(0, eval(value))
    except NameError:
        messagebox.showinfo('Attention', 'You enter the letters but only digits allowed!')
        calc.insert(0, 0)
    except SyntaxError:
        messagebox.showinfo('Attention', 'You enter the symbols but only digits allowed!')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Attention', 'Division by zero is impossible!')
        calc.insert(0, 0)
    calc['state'] = tk.DISABLED


def clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, 'end')
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13),
                     command=lambda: add_operation(operation), fg='#4D6EF0')


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13),
                     command=calculate, fg='#4D6EF0')


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13),
                     command=clear, fg='#4D6EF0')


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '=':
        calculate()
    elif event.char == 'C':
        clear()
    elif event.char == 'c':
        clear()


win = tk.Tk()
win.geometry(f"242x270+100+200")
win.resizable(width=False, height=False)
win['bg'] = '#702E6C'
win.title('Calculator')
win.iconphoto(False, tk.PhotoImage(file='calc.png'))


win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc['state'] = tk.DISABLED
calc.configure({"disabledforeground": "black"})
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=4)

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=3, pady=3)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=3, pady=3)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=3, pady=3)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=3, pady=3)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=3, pady=3)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=3, pady=3)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=3, pady=3)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=3, pady=3)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=3, pady=3)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=3, pady=3)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=3, pady=3)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=3, pady=3)
make_operation_button('/').grid(row=3, column=3, stick='wens', padx=3, pady=3)
make_operation_button('*').grid(row=4, column=3, stick='wens', padx=3, pady=3)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=3, pady=3)
make_clear_button('C').grid(row=4, column=1, stick='wens', padx=3, pady=3)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)


win.mainloop()
