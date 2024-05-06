import tkinter as tk
from tkinter import filedialog

class SimpleNotePad(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Notepad")
        self.geometry("800x600")

        self.textArea = tk.Text(self)
        self.textArea.pack(fill=tk.BOTH, expand=True)

        menuBar = tk.Menu(self)
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New", command=self.new_file)
        fileMenu.add_command(label="Open", command=self.open_file)
        fileMenu.add_command(label="Save", command=self.save_file)
        menuBar.add_cascade(label="File", menu=fileMenu)
        self.config(menu=menuBar)

        self.filepath = None

    def new_file(self):
        self.textArea.delete(1.0, tk.END)
        self.filepath = None

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.textArea.delete(1.0, tk.END)
                self.textArea.insert(1.0, file.read())
                self.filepath = file_path

    def save_file(self):
        if self.filepath:
            with open(self.filepath, "w") as file:
                file.write(self.textArea.get(1.0, tk.END))
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_path:
                with open(file_path, "w") as file:
                    file.write(self.textArea.get(1.0, tk.END))
                self.filepath = file_path

if __name__ == "__main__":
    app = SimpleNotePad()
    app.mainloop()
