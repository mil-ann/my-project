import tkinter as tk 
root = tk.Tk()
root.title("tkinter window")
root.geometry("400x300")

#adding label
label = tk.Label(root, text="FORM")
label.pack()

#button click functio
def on_submit():
    print("button clicked!")

#adding button
button = tk.Button(root,text="submit", command=on_submit)
button.pack() 

#adding input entry
entry = tk.Entry(root)
entry.pack()

#adding text area
text = tk.Text(root, height=5, width=40)
text.pack()

#adding checkbox
frame = tk.Frame(root, bg="blue")


check = tk.IntVar()
check2 = tk.IntVar()
checkbutton = tk.Checkbutton(frame,text="check me", variable=check)
checkbutton2 = tk.Checkbutton(frame,text="check me too", variable=check2)
checkbutton.pack()
checkbutton2.pack()

#adding radio box

label = tk.Label(frame, text="Gender")
label.pack()

radio_var = tk.StringVar()
radiobutton1 = tk.Radiobutton(frame,text="male",\
                              variable=radio_var,value="M")
radiobutton2 = tk.Radiobutton(frame,text="female",\
                              variable=radio_var,value="F")

radiobutton1.pack()
radiobutton2.pack()

frame.pack()
##menu add
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="file", menu=file_menu)
file_menu.add_command(label="new")
file_menu.add_command(label="open")
file_menu.add_command(label="save")
file_menu.add_separator()
file_menu.add_command(label="exit", command=root.quit)

#treeview widget
tree = ttk.Treeview(root)
tree["columns"]=("name","age")



root.mainloop()



