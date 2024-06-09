#importing library for gui
from tkinter import *
import string
import random
import pyperclip

def Generator():
    small_alphabet=string.ascii_lowercase
    capital_Alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation
    all=small_alphabet+capital_Alphabets+special_characters+numbers

    password_length=int(length_Box.get())
    # password=random.sample(all,password_length)
    # passwordField.insert(0,password)
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabet,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabet+capital_Alphabets,password_length))
    if choice.get() == 3:
        passwordField.insert(0, random.sample(all, password_length))
    print(password_length)

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

#creating instance for Library class
root =Tk()

#for changing background colour
root.config(bg='gray20')
choice=IntVar()
Font=('arial',13,'bold')
#for header
passwordLabel =Label(root,text='Pasword Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.grid()


#radio buttons
weakRadioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakRadioButton.grid(pady=5)
meduimRadioButton=Radiobutton(root,text='Meduim',value=2,variable=choice,font=Font)
meduimRadioButton.grid(pady=5)
strongRadioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongRadioButton.grid(pady=5)
lengthLabel =Label(root,text='Pasword Length',font=('times new roman',20,'bold'),bg='gray20',fg='white')
lengthLabel.grid(pady=10)
length_Box = Spinbox(root,from_=3,to_=10,width=5,font=Font)
length_Box.grid(pady=6)
generateButton= Button(root,text='Generate',font=Font,command=Generator)
generateButton.grid(pady=6)
passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=7)
CopyButton= Button(root,text='Copy',font=Font,command=copy)
CopyButton.grid(pady=6)
#To keep our window in loop
root.mainloop()
