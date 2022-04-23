from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTVXYZ'
    numbers = '0123456789'
    symbols = '!@#$$%^&*()_+}{":?><,.~`-=;'

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = ''.join(password_list)
    password_field.delete(0, END)
    password_field.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_field.get()
    email = email_user_field.get()
    password = password_field.get()
    if website == '' or password == '':
        messagebox.showinfo(title='Oops', message='Please don\'t leave any fields empty!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email}'
                                                              f'\nPassword: {password} \nIs it ok to save?')
        if is_ok:
            with open('account.txt', 'a') as file:
                file.write(f'{website} | {email} | {password}\n')
                website_field.delete(0, END)
                password_field.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

Label(text='Website:').grid(column=0, row=1)
Label(text='Email/Username:').grid(column=0, row=2)
Label(text='Password:').grid(column=0, row=3)

website_field = Entry(width=35)
website_field.grid(column=1, row=1, columnspan=2)
website_field.focus()
email_user_field = Entry(width=35)
email_user_field.grid(column=1, row=2, columnspan=2)
email_user_field.insert(0, 'olaoluwaolorede8@gmail.com')
password_field = Entry(width=21)
password_field.grid(column=1, row=3, )

Button(text='Generate Password', command=generate_password, width=15).grid(column=2, row=3)
Button(text='Add', command=save, width=36).grid(column=1, row=4, columnspan=2)
window.mainloop()
