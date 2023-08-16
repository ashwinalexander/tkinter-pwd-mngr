from tkinter import *




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# first configure the window
window.config(padx=50, pady=50)
# email = StringVar()
# password = StringVar()


def add_entry():
    pass


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
txtWebsite = Entry(width=52,justify="left")
txtWebsite.grid(row=1,column=1,  columnspan=2)

txtUsername = Entry(width=52,justify="left")
txtUsername.grid(row=2,column=1,  columnspan=2)

txtPassword = Entry(width=33)
txtPassword.grid(row=3,column=1)

# Generate Password button
btnGen = Button(text="Generate Password", command=add_entry,justify="left")
btnGen.grid(row=3, column=2)

# Add button
btnAdd = Button(text="Add", command= add_entry, width=44)
btnAdd.grid(row=4, column=1, columnspan=2)

window.mainloop()