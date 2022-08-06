from tkinter import *

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background="light blue")

word = Entry(root)
word.place(relx=0.5, rely=0.4, anchor=CENTER)

input_ascii = Label(root, text="Name of Ascii : ", bg= "light yellow", fg="black")
input_encrypted = Label(root, text="Encrypted name : ", bg= "snow", fg="black")
def asciiConverter():
    hey = word.get()
    
    for letter in hey:
        input_ascii["text"] += str(ord(letter)) + " "
        
def encrypted():
    hey2 = word.get()
    
    for letter in hey2:
        input_ascii["text"] += str(ord(letter)) + " "
        input_ascii = int(ord(letter))
        input_encrypted = input_ascii - 1
        input_encrypted["text"] += str(chr(encrypted))
    
btn=Button(root, text="Display the Ascii Code and Encrypted value", command=asciiConverter, bg='blue', fg='snow')
btn.place(relx=0.5,rely=0.5, anchor=CENTER)

input_ascii.place(relx=0.5, rely=0.6, anchor=CENTER)
input_encrypted.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()

