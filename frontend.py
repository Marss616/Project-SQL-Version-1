from tkinter import * 
 
# creating main tkinter window/toplevel
master = Tk()
master.title("GUI SQL display Version 0.3")
master.geometry('500x500') # Set window size

def putsomething():
    print("hello world")

# START wigets
sql_cmd_label = Label(master, text="Enter your SQL command:")
sql_cmd_entry = Entry(master)

sql_cmd_button = Button(master, text="enter", command=putsomething, padx=20)

header_output = Label(master, text = "Output: ", font=("Comic Sans MS", 20))
sql_cmd_output = Entry(master)
# END wigets

# START Place Wigets

sql_cmd_label.grid(row = 1, column = 1, padx=20, pady=10)
sql_cmd_entry.grid(row = 1, column = 2, padx=10)
sql_cmd_button.grid(row = 1, column = 3, padx=20, pady=10)
header_output.grid(row = 2, column = 1)
sql_cmd_output.grid(row = 3, column = 2, padx=10)

# START Place Wigets

mainloop()