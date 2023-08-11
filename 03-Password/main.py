from tkinter import *
from random import randint

root  = Tk()
root.title('Password Generator App')
root.iconbitmap('Python\\03-Password\password.ico')
root.geometry("500x300")

# Main Code:
def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())

    my_password = ''
    for x in range(pw_length):
        my_password += chr(randint(33,126))
    pw_entry.insert(0, my_password)


def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())

# Label Frame
lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

# Entry Box
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

#Output Box
pw_entry = Entry(root, text="", font=("Helvetica", 24), bd=0, bg="systembuttonface") 
pw_entry.pack(pady=20)

# Frame for Buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

# Buttons
my_buttons = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_buttons.grid(row=0, column=0, padx=10)

clip_buttons = Button(my_frame, text="Copy To Clipboard", command=clipper)
clip_buttons.grid(row=0, column=1, padx=10)

root.mainloop()