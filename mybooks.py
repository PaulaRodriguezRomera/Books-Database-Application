from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox
from mysql_config import dbConfig
import mysql.connector as pyo

root = Tk()

#ROOT
root.title("My Books Database Application")
root.configure(background="light green")
root.geometry("850x500")
root.resizable(width=False, height=False)

#TITLE
title_label = Label(root,text="Title", background="light green", font=("TkDefaultFont", 16))
title_label.grid(row=0, column=0, sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(root, width=15, textvariable=title_text)
title_entry.grid(row=0, column=1, sticky=W)

#AUTHOR
author_label = Label(root,text="Author", background="light green", font=("TkDefaultFont", 16))
author_label.grid(row=0, column=2, sticky=W)
author_text = StringVar()
author_entry = ttk.Entry(root, width=15, textvariable=author_text)
author_entry.grid(row=0, column=3, sticky=W)

#ISBN
isbn_label = Label(root,text="ISBN", background="light green", font=("TkDefaultFont", 16))
isbn_label.grid(row=0, column=4, sticky=W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width=15, textvariable=isbn_text)
isbn_entry.grid(row=0, column=5, sticky=W)

#BUTTON
add_btn = Button(root, text="Add Book", bg="blue", fg="black", font="helvetica 10 bold", command="")
add_btn.grid(row=0, column=6, sticky=W)

#LIST
list_bx = Listbox(root, height=16, width=40, font="helvetica 13", bg="light blue")
list_bx.grid(row=3, column=1, columnspan=14, sticky=W + E, pady=40, padx=15)

#SCROLL BAR
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1,column=8,rowspan=14,sticky=W)

list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)

#BUTTONS SELECTION
modify_btn = Button(root, text="Modify Record", bg="purple", fg="black", font="helvetica 10 bold", command="")
modify_btn.grid(row=15, column=4)

delete_btn = Button(root, text="Delete Record", bg="purple", fg="black", font="helvetica 10 bold", command="")
delete_btn.grid(row=15, column=5)

view_btn = Button(root, text="View all records", bg="purple", fg="black", font="helvetica 10 bold", command="")
view_btn.grid(row=15, column=1)

clear_btn = Button(root, text="Clear Screen", bg="purple", fg="black", font="helvetica 10 bold", command="")
clear_btn.grid(row=15, column=2)

exit_btn = Button(root, text="Exit Application", bg="purple", fg="black", font="helvetica 10 bold", command="")
exit_btn.grid(row=15, column=3)

root.mainloop()