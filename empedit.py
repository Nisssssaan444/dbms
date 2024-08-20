from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox
import string
import random

root = Tk()
root.title("Search Employee")
root.geometry("900x500+200+100")
root.resizable(False, False) 
global root_window
root_window = root

def on_closing():
    root_window.destroy()

def search():
    option = dropdown.get()
    search_input = searchInput.get()
    db = mysql.connector.connect(host="localhost", port=3306, user="root", password="NISsan123@", database="pulchowkcampus")
    mycursor = db.cursor()
    if search_input == "":
        mycursor.execute("SELECT * FROM employee_table")
    elif option == "Name":
        mycursor.execute("SELECT * FROM employee_table WHERE name = '" + str(search_input).upper() + "'")
    elif option == "UID":
        mycursor.execute("SELECT * FROM employee_table WHERE id = '" + str(search_input) + "'")
    elif option == "Designation":
        mycursor.execute("SELECT * FROM employee_table WHERE designation = '" + str(search_input).upper() + "'")
    elif option == "Department":
        mycursor.execute("SELECT * FROM employee_table WHERE dept = '" + str(search_input).upper() + "'")
    else:
        return
    rows = mycursor.fetchall()
    data_table.delete(*data_table.get_children())
    if not rows:
        note_text['text'] = "Data: 0 Rows"
        return 
    note_text['text'] = "Data: "+str(len(rows))+" Rows"
    for row in rows:
        data_table.insert('', END, values=row)
    db.commit()
    db.close()

def show():
    db = mysql.connector.connect(host="localhost", port=3306, user="root", password="NISsan123@", database="pulchowkcampus")
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM employee_table")
    rows = mycursor.fetchall()
    if len(rows) != 0:
        data_table.delete(*data_table.get_children())
    for row in rows:
        data_table.insert('', END, values=row)
    db.commit()
    db.close()

def getdata(event):
    currow = data_table.focus()
    contents = data_table.item(currow)
    row = contents['values']
    updatebt.configure(state="normal")
    deletebt.configure(state="normal")
    IdEntry.configure(state='normal')
    IdEntry.delete(0, END)
    NameEntry.delete(0, END)
    DesignationEntry.delete(0, END)
    DepartmentEntry.delete(0, END)
    IdEntry.insert(0, row[0])
    IdEntry.configure(state='readonly')
    NameEntry.insert(0, row[1])
    DesignationEntry.insert(0, row[2])
    DepartmentEntry.insert(0, row[3])
    addbt.configure(state='disabled')

def add():
    if IdEntry.get() == "" or NameEntry.get() == "" or DesignationEntry.get() == "" or DepartmentEntry.get() == "":
       messagebox.showerror("Error", "All fields are required")
    else:
        iD = IdEntry.get()
        name = NameEntry.get()
        desg = DesignationEntry.get()
        dept = DepartmentEntry.get()
        db = mysql.connector.connect(host="localhost", port=3306, user="root", password="NISsan123@", database="pulchowkcampus")
        mycursor = db.cursor()
        try:
           mycursor.execute("INSERT INTO employee_table (id, name, designation, dept) VALUES ('" + str(iD) + "', '" + str(name).upper() + "', '" + str(desg).upper() + "', '" + str(dept).upper() + "')")
           db.commit()
           messagebox.showinfo("information", "Record Inserted successfully")
           search()
           clear()
        except Exception as e:
           print(e)
           db.rollback()
           db.close()

def update():
    iD = IdEntry.get()
    name = NameEntry.get()
    desg = DesignationEntry.get()
    dept = DepartmentEntry.get()
    db = mysql.connector.connect(host="localhost", port=3306, user="root", password="NISsan123@", database="pulchowkcampus")
    mycursor = db.cursor()
    mycursor.execute("UPDATE employee_table SET name = '" + str(name).upper() + "', designation = '" + str(desg) + "', dept = '" + str(dept).upper() + "' WHERE id = '" + str(iD) + "'")
    db.commit()
    messagebox.showinfo("information", "Record Updated successfully")
    IdEntry.delete(0, END)
    NameEntry.delete(0, END)
    DesignationEntry.delete(0, END)
    DepartmentEntry.delete(0, END)
    search()
    clear()

def delete1():
    iD = IdEntry.get()
    db = mysql.connector.connect(host="localhost", port=3306, user="root", password="NISsan123@", database="pulchowkcampus")
    mycursor = db.cursor()
    sql = "DELETE FROM employee_table WHERE id='" + str(iD) + "'"
    mycursor.execute(sql)
    db.commit()
    messagebox.showinfo("information", "Record Deleted successfully")
    IdEntry.delete(0, END)
    NameEntry.delete(0, END)
    DesignationEntry.delete(0, END)
    DepartmentEntry.delete(0, END)
    search()
    clear()

def clear():
    updatebt.configure(state="disabled")
    deletebt.configure(state="disabled")
    IdEntry.configure(state='normal')
    IdEntry.delete(0, END)
    IdEntry.insert(0, random_string())
    NameEntry.delete(0, END)
    DesignationEntry.delete(0, END)
    DepartmentEntry.delete(0, END)
    NameEntry.focus_set()
    addbt.configure(state='normal')

def random_string():
    count = 1
    S = 5
    while(count != 0):
        ran = ''.join(random.choices(string.ascii_letters + string.digits, k = S))
        db = mysql.connector.connect(host="localhost", port=3306, user="root", password="NISsan123@", database="pulchowkcampus")
        mycursor = db.cursor()
        mycursor.execute("SELECT COUNT(id) FROM employee_table WHERE id = '" + str(ran) + "'")
        rows = mycursor.fetchone()
        count = rows[0]
    return ran

# Header
header = Frame(root, bg="brown", bd=0)
header.place(x=0, y=0, width=900, height=75)

# Heading label
pc = Label(header, text="IOE PULCHOWK CAMPUS", font=("Helvetica", 28, "bold"), bg="brown", fg="#eae2b7")
pc.place(x=0, y=10, width=900)

# Profile frame
frame2 = Frame(root, bg="#fbb1bd")
frame2.place(x=0, y=75, width=900, height=50)
welcome_text = Label(frame2, text="View/Edit Employee (by Name OR UID)", font=("Minion Pro Regular", 16), bg="#fbb1bd")
welcome_text.place(x=20, y=10)
close = Button(frame2, text="Close", command=on_closing, bd=0, font=("Minion Pro Regular", 16), bg="#fff", fg="#000")
close.place(x=830, y=0, height=50, width=70)

# Left box
leftbox = Frame(root, bd=0, bg="brown")
leftbox.place(x=10, y=140, width=300, height=350)

# Inside left box
leftbox_title = Label(leftbox, text="Manage Database", font=("Helvetica", 20, "bold"), fg="#eae2b7", bg="brown")
leftbox_title.place(x=30, y=10)
IdLabel = Label(leftbox, text="ID", font=("Helvetica", 15), fg="#eae2b7", bg="brown")
IdLabel.place(x=10, y=50)
IdEntry = Entry(leftbox, font=("Helvetica", 15), bd=0)
IdEntry.insert(0, random_string())
IdEntry.place(x=200, y=50, width=80)
NameLabel = Label(leftbox, text="Name", font=("Helvetica", 15), fg="#eae2b7", bg="brown")
NameLabel.place(x=10, y=100)
NameEntry = Entry(leftbox, font=("Helvetica", 15), bd=0)
NameEntry.place(x=80, y=100, width=200)
DesignationLabel = Label(leftbox, text="Designation", font=("Helvetica", 15), fg="#eae2b7", bg="brown")
DesignationLabel.place(x=10, y=150)
DesignationEntry = Entry(leftbox, font=("Helvetica", 15), bd=0)
DesignationEntry.place(x=130, y=150, width=150)
DepartmentLabel = Label(leftbox, text="Department", font=("Helvetica", 15), fg="#eae2b7", bg="brown")
DepartmentLabel.place(x=10, y=200)
DepartmentEntry = Entry(leftbox, font=("Helvetica", 15), bd=0)
DepartmentEntry.place(x=130, y=200, width=150)

addbt = Button(leftbox, text="Add", font=("Helvetica", 15), bd=0, command=add)
addbt.place(x=10, y=250, width=100, height=35)
updatebt = Button(leftbox, text="Update", font=("Helvetica", 15), bd=0, command=update, state='disabled')
updatebt.place(x=110, y=250, width=100, height=35)
deletebt = Button(leftbox, text="Delete", font=("Helvetica", 15), bd=0, command=delete1, state='disabled')
deletebt.place(x=210, y=250, width=100, height=35)
clearbt = Button(leftbox, text="Clear", font=("Helvetica", 15), bd=0, command=clear)
clearbt.place(x=110, y=290, width=100, height=35)

# Right box
rightbox = Frame(root, bd=0)
rightbox.place(x=320, y=140, width=570, height=350)
rightbox_title = Label(rightbox, text="Employee Records", font=("Helvetica", 20, "bold"))
rightbox_title.pack(side=TOP, fill=X)
searchframe = Frame(rightbox, bd=0)
searchframe.pack(side=TOP, fill=X)
dropdown = ttk.Combobox(searchframe, values=["Name", "UID", "Designation", "Department"], font=("Helvetica", 15))
dropdown.pack(side=LEFT, padx=10, pady=10)
dropdown.current(0)
searchInput = Entry(searchframe, font=("Helvetica", 15), bd=0)
searchInput.pack(side=LEFT, padx=10, pady=10)
searchbt = Button(searchframe, text="Search", font=("Helvetica", 15), bd=0, command=search)
searchbt.pack(side=LEFT, padx=10, pady=10)
showbt = Button(searchframe, text="Show All", font=("Helvetica", 15), bd=0, command=show)
showbt.pack(side=LEFT, padx=10, pady=10)
note_text = Label(searchframe, text="Data: 0 Rows", font=("Helvetica", 15))
note_text.pack(side=RIGHT, padx=10, pady=10)

# Data table
data_frame = Frame(rightbox, bd=0)
data_frame.pack(side=TOP, fill=BOTH, expand=True)
scrollbarx = Scrollbar(data_frame, orient=HORIZONTAL)
scrollbary = Scrollbar(data_frame, orient=VERTICAL)
data_table = ttk.Treeview(data_frame, columns=("ID", "Name", "Designation", "Department"), xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
scrollbarx.pack(side=BOTTOM, fill=X)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=data_table.xview)
scrollbary.config(command=data_table.yview)
data_table.heading("ID", text="ID")
data_table.heading("Name", text="Name")
data_table.heading("Designation", text="Designation")
data_table.heading("Department", text="Department")
data_table['show'] = 'headings'
data_table.column("ID", width=50)
data_table.column("Name", width=150)
data_table.column("Designation", width=150)
data_table.column("Department", width=100)
data_table.pack(side=TOP, fill=BOTH, expand=True)
data_table.bind('<ButtonRelease-1>', getdata)

root.mainloop()
