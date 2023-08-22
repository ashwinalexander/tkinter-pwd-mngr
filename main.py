from tkinter import *
from tkinter import messagebox




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# first configure the window
window.config(padx=50, pady=50)

def save_entry():
    val_website = var_website.get()
    val_email = var_email.get()
    val_pwd = var_password.get()

    if len(val_website) == 0 or len(val_pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")

    else:
        is_okay = messagebox.askokcancel(title=val_website,
                                     message=f"These are the details entered: \n Email:{val_email}\n Password:{val_pwd}\n Shall we go ahead and save? ")

        if is_okay:
            # using with means we don't have to worry about closing the file
            with open("data.txt", "a") as data_file:
                data_file.write(f"{val_website} | {val_email} | {val_pwd} \n")

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
txtWebsite = Entry(width=52,justify="left", textvariable=var_website)
txtWebsite.focus()
txtWebsite.grid(row=1,column=1,  columnspan=2)

var_email = StringVar()
txtUsername = Entry(width=52,textvariable=var_email)
txtUsername.insert(0,'ashwin@gmail.com')
txtUsername.grid(row=2,column=1,  columnspan=2)

var_password = StringVar()
txtPassword = Entry(width=33, textvariable=var_password)
txtPassword.grid(row=3,column=1)

# Generate Password button
btnGen = Button(text="Generate Password", command=save_entry)
btnGen.grid(row=3, column=2)

# Add button
btnAdd = Button(text="Add", command= save_entry, width=44)
btnAdd.grid(row=4, column=1, columnspan=2)

window.mainloop()