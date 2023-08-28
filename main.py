from tkinter import *
from tkinter import messagebox
from random  import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_lett = [choice(letters) for _ in range(randint(8, 10))]
    password_sym = [choice(symbols) for _ in range(randint(2, 4))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_lett + password_sym + password_num
    shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)
    txtPassword.delete(0,END)
    txtPassword.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# first configure the window
window.config(padx=50, pady=50)

def search_db():
    website_val = txtWebsite.get()
    if len(website_val) == 0:
        messagebox.showinfo(title="Oops", message="Which website are you searching for?")
    else:
        try:
            with open("data.json", "r") as data_file:
                # read old data
                all_data = json.load(data_file)
                web_credentials = all_data[website_val]
                email = web_credentials["email"]
                pwd = web_credentials["password"]

                messagebox.showinfo(title=website_val, message=f"Email:{email}\nPassword:{pwd}\n")
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
        except KeyError:
            messagebox.showinfo(title="Error", message="No website found")





def save_entry():
    val_website = var_website.get()
    val_email = var_email.get()
    val_pwd = var_password.get()
    new_data = {
        val_website: {
            "email": val_email,
            "password": val_pwd
        }
    }

    if len(val_website) == 0 or len(val_pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            # using with means we don't have to worry about closing the file
            # First try to read from the file we assume it exists at this point
            with open("data.json", "r") as data_file:
                # read old data
                data = json.load(data_file)
        except FileNotFoundError:
            # our assumption was incorrect and the file did not exists so let's write to it
            with open("data.json", "w") as data_file:
                # write to json
                json.dump(new_data, data_file, indent=4)

        else:
            # this is only triggered if everything within the try block is successful
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # write to json
                json.dump(data, data_file, indent=4)

        # finally delete the entries
        txtWebsite.delete(0, 'end')
        txtPassword.delete(0, 'end')


# next configure the canvas
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)

# next configure the image on the canvas
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)

# next add the Website label
lblWebsite = Label(text="Website:", padx=4, pady=4)
lblWebsite.grid(row=1,column=0)


# next add the Username label
lblUsername = Label(text="Email/Username:", padx=4, pady=4)
lblUsername.grid(row=2,column=0)

# next add the Password label
lblPassword = Label(text="Password:", padx=4, pady=4)
lblPassword.grid(row=3,column=0)

# Entries

var_website = StringVar()
txtWebsite = Entry(width=33, textvariable=var_website)
txtWebsite.focus()
txtWebsite.grid(row=1,column=1)

var_email = StringVar()
txtUsername = Entry(width=52,textvariable=var_email)
txtUsername.insert(0,'ashwin@gmail.com')
txtUsername.grid(row=2,column=1,  columnspan=2)

var_password = StringVar()
txtPassword = Entry(width=33, textvariable=var_password)
txtPassword.grid(row=3,column=1)

# Search button
btnSearch = Button(text="Search", command=search_db, bg="blue", fg="white", width=13)
btnSearch.grid(row=1, column=2)

# Generate Password button
btnGen = Button(text="Generate Password", command=gen_pwd)
btnGen.grid(row=3, column=2)

# Add button
btnAdd = Button(text="Add", command= save_entry, width=44)
btnAdd.grid(row=4, column=1, columnspan=2)



window.mainloop()