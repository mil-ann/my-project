import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import StringVar, IntVar

class FootballManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("local playground")
        self.root.geometry("800x600")

        # Initialize data storage
        self.players = []

        # UI setup
        self.setup_ui()

    def setup_ui(self):
        # Create frames
        top_frame = tk.Frame(self.root, pady=10)
        top_frame.pack(side=tk.TOP, fill=tk.X)
        
        middle_frame = tk.Frame(self.root)
        middle_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        bottom_frame = tk.Frame(self.root, pady=10)
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)



        
        
        # Top frame - title
        title = tk.Label(top_frame, text="local playground", font=("Arial", 24))
        title.pack()

        # Middle frame - form and list
        form_frame = tk.Frame(middle_frame, padx=10, pady=10, borderwidth=2, relief="groove")
        form_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.list_frame = tk.Frame(middle_frame, padx=10, pady=10, borderwidth=2, relief="groove")
        self.list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.setup_form(form_frame)
        self.setup_list(self.list_frame)

        # Bottom frame - actions
        add_button = tk.Button(bottom_frame, text="Add Player", command=self.add_player)
        add_button.pack(side=tk.LEFT, padx=10)
        
        delete_button = tk.Button(bottom_frame, text="Delete Player", command=self.delete_player)
        delete_button.pack(side=tk.LEFT, padx=10)
        
    def setup_form(self, frame):
        # Labels and entry fields
        self.name_var = StringVar()
        self.country_var = StringVar()
        self.location_var = StringVar()
        self.age_var = IntVar()
        #self.contact_var = IntVar()
        
        tk.Label(frame, text="Player Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        tk.Entry(frame, textvariable=self.name_var).grid(row=0, column=1, pady=5)
        
        tk.Label(frame, text="Country:").grid(row=1, column=0, sticky=tk.W, pady=5)
        tk.Entry(frame, textvariable=self.country_var).grid(row=1, column=1, pady=5)
        
        tk.Label(frame, text="Location:").grid(row=2, column=0, sticky=tk.W, pady=5)
        tk.Entry(frame, textvariable=self.location_var).grid(row=2, column=1, pady=5)
        
        tk.Label(frame, text="Age:").grid(row=3, column=0, sticky=tk.W, pady=5)
        tk.Entry(frame, textvariable=self.age_var).grid(row=3, column=1, pady=5)

        #tk.Label(frame, text="conact number:").grid(row=4, column=0, sticky=tk.W, pady=5)
        #tk.Entry(frame, textvariable=self.age_var).grid(row=4, column=1, pady=5)

    def setup_list(self, frame):
        # Listbox and scrollbar
        self.listbox = tk.Listbox(frame)
        self.scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def add_player(self):
        name = self.name_var.get()
        country = self.country_var.get()
        location = self.location_var.get()
        age = self.age_var.get()
        #contact = self.contact_var.get()
        
        if not name or not country or not location or not age:
            messagebox.showwarning("Input Error", "All fields are required.")
            return
        
        player_info = f"{name}, {country}, {location}, Age: {age} "
        self.players.append(player_info)
        self.listbox.insert(tk.END, player_info)
        
        self.name_var.set("")
        self.country_var.set("")
        self.location_var.set("")
        self.age_var.set(0)
        #self.contact_var.set(0)

    def delete_player(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "No player selected.")
            return
        
        index = selected[0]
        self.listbox.delete(index)
        del self.players[index]

if __name__ == "__main__":
    root = tk.Tk()
    app = FootballManagementSystem(root)
    root.mainloop()