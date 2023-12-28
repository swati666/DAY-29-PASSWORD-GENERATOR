from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# todo- Password Generator Project


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)


    rand_letter = [choice(letters) for _ in range(randint(8, 10))]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    rand_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    rand_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = rand_numbers + rand_symbols + rand_letter
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)
    # print(f"Your password is: {password}")
    genPas_enter.insert(0, password)
    copied = pyperclip.copy(password)
    if copied:
        messagebox.showinfo(message="Password is successfully copied to clipboard.")

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website = Label(text="Website: ")
# website.grid(column=0, row=1,)
# website_enter = Entry(width=35,)
# website_enter.grid(column=1, row=1, columnspan = 2)
#
# email = Label(text="Email/Username: ")
# email.grid(row=2, column=0,)
# email_enter = Entry(width=35)
# email_enter.grid(row=2, column=1, columnspan = 2)
#
#
# password = (Label(text="Password: "))
# password.grid(row=3, column=0,)
# genPas_enter = Entry(width=21)
# genPas_enter.grid( row=3, column=1,)
#
# gen_pass_button = Button(text="Generate Password: ", )
# gen_pass_button.grid(column=2, row=3,)
#
#
# add = Button(text="Add", width=36)
# add.grid(column=1, row=4, columnspan = 2)


# todo- LABELS
website = Label(text="Website:",)
website.grid(column=0, row=1,)

email = Label(text="Email/Username:")
email.grid(row=2, column=0,)

password = (Label(text="Password:"))
password.grid(row=3, column=0,)

# todo- ENTRIES
website_enter = Entry(width=40,)
website_enter.grid(column=1, row=1, columnspan=2)
# concept- focus() helps in pointing cursor to that specific widget
website_enter.focus()

email_enter = Entry(width=40)
email_enter.grid(row=2, column=1, columnspan=2)
# concept- insert(index(int data type), string)--- insert(..) helps in autopopulate the entry column.
email_enter.insert(0, "iistswatiyadav@gmail.com")
# email_enter.insert(1, "swatiyadavcreate333@gmail.com")

genPas_enter = Entry(width=24)
genPas_enter.grid(row=3, column=1)

# todo- BUTTONS
gen_pass_button = Button(text="Generate Password", command=password_generator)
gen_pass_button.grid(column=2, row=3, columnspan = 2)


# todo ----------------------------  DATA ADD ------------------------------- #
def save():
    website_data = website_enter.get()
    email_data = email_enter.get()
    password_data = genPas_enter.get()

    with open(file="data.txt", mode='a') as data:
        data.write(f"{website_data}  ||  {email_data}  ||  {password_data}\n")
        website_enter.delete(0, END)
        genPas_enter.delete(0, END)

    if len(website_data) < 1 and len(password_data) < 1:
        messagebox.showinfo(title="Incomplete Credentials ", message="Please fill Required Data")

    elif len(website_data) < 1:
        messagebox.showinfo(title="Incomplete Credentials ", message="Please fill Website name")

    elif len(password_data) < 1:
        messagebox.showinfo(title="Incomplete Credentials ", message="Please fill Password")

    else:
            is_ok = messagebox.askokcancel(title="Details Conformation",
                                       message=f"Is website: {website_data} , email: {email_data} ,"
                                               f" and password: {password_data} OK?")
            if is_ok:
                with open(file="data.txt", mode='a') as data:
                    data.write(f"{website_data}  ||  {email_data}  ||  {password_data}\n")
                    website_enter.delete(0, END)
                    genPas_enter.delete(0, END)


add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)







window.mainloop()