# Importing Modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from tkinter.ttk import Sizegrip

# Creating Window
window = Tk()
title = "Untitled-Notepad"
window.title(title)
window.geometry('500x500')
menu = Menu(window, tearoff=0, selectcolor='white')
file_menu = Menu(menu, tearoff=0)

# Creating Text area
text_changed = False
text_area = Text(window, wrap='none', relief=FLAT, font="arial 12", undo=True)
text_area.pack(expand=True, fill=BOTH)
fil = None
text_area.focus_force()

# Status Bar Work
status_bar = Label(window, text='Status Bar')
status_bar.pack(side=BOTTOM)
show_statusbar = BooleanVar()
show_statusbar.set(True)
window_title = ''
change_title = True

# Functions

def undo_func(event=""):
    try:
        text_area.edit_undo()
    except:
        pass


def redo_func(event=""):
    try:
        text_area.edit_redo()
    except:
        pass



def help_pad(event=""):
    messagebox.showinfo("Info", "Thanks for using our Notepad. This Notepad is Published by FaizansCommunit.\n (NO-COPYRIGHT) ")


def changed(event=""):
    global text_changed, change_title
    if text_area.edit_modified():

        if change_title:
            if window.title() == 'Untitled-Notepad':
                pass
            else:
                window.title(f'{window_title}*')
        if change_title:
            text_changed = True
        words = len(text_area.get(1.0, 'end-1c').split())
        characters = len(text_area.get(1.0, 'end-1c'))
        status_bar.config(
            text=f'Words  :  {words}   Characters   :  {characters}')
        change_title = True

    text_area.edit_modified(False)

def open_file(event=""):
    try:
        global fil, window_title, change_title, text_changed
        fil = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text Documents', '.txt'), (
            'HTML Documents', '.html'), ('Python Documents', '.py'), ('Word Documents', '.docx'), ('All Types', '*.*')])
        if fil == "":
            fil = None
        else:
            window.title(os.path.basename(fil)+"-Notepad")
            window_title = os.path.basename(fil)+"-Notepad"
            change_title = False
            text_area.delete(1.0, END)
            f = open(fil, 'r')
            text_area.insert(1.0, f.read())
            text_changed = False
    except:
        messagebox.showerror('Error', "Can't open the file!")
        window.title('Untitled-Notepad')

def quit_func(event=""):
    global fil, text_changed
    if text_changed:
        window.wm_protocol("WM_DELETE_WINDOW", quit_func)
        au = messagebox.askyesnocancel(
            "Warning", "Do you want to save the changes to Untitled?")
        if au == TRUE:
            ask_user_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Documents', '.txt'), (
                'HTML Documents', '.html'), ('Python Documents', '.py'), ('Word Documents', '.docx'), ('All Types', '*.*')])
            if ask_user_path == "":
                window.quit()
            else:
                window.title(os.path.basename(ask_user_path))
                as_us = open(ask_user_path, 'w')
                data = text_area.get(1.0, END)
                as_us.write(data)
                as_us.close()
                window.quit()
        elif au == False:
            window.quit()
        else:
            pass
    else:
        window.quit()


def clear_all(event=""):
    text_area.delete(1.0, END)


def new_file(event=""):
    global text_changed
    if text_changed == False:
        txt = text_area.get(1.0, END)
        text_area.delete(1.0, END)
        window.title('Untitled-Notepad')
    else:
        save_file = messagebox.askyesnocancel(
            "Notepad", "Do you want to save the changes to Untitled")
        if save_file == True:
            file_path = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text Documents', '.txt'), (
                'HTML Documents', '.html'), ('Python Documents', '.py'), ('Word Documents', '.docx'), ('All Types', '*.*')])
            opened_file = open(file_path, "w")
            opened_file.write(text_area.get(1.0, END))
            opened_file.close()
            text_area.delete(1.0, END)
            text_changed = False
            status_bar.config(text="Status Bar")
            text_area.edit_modified(False)

        elif save_file == False:
            txt = text_area.get(1.0, END)
            text_area.delete(1.0, END)
            window.title('Untitled-Notepad')
            text_changed = False
            text_area.edit_modified(False)
            status_bar.config(text="Status Bar")
        else:
            pass

def save_as(event=""):
    try:
        ask = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[(
            'Text Documents', '.txt'), ('HTML Documents', '.html'), ('Python Documents', '.py'), ('Word Documents', '.docx'), ('All Types', '*.*')])
        fc = open(ask, 'w')
        fc.write(text_area.get(1.0, END))
        fc.close()
    except:
        pass


def save_file(event=""):
    global fil, window_title, change_title
    if fil == None:
        fil = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[(
            'Text Documents', '.txt'), ('HTML Documents', '.html'), ('Python Documents', '.py'), ('Word Documents', '.docx'), ('All Types', '*.*')])
        if fil == "":
            fil = None
        else:
            f = open(fil, 'w')
            f.write(text_area.get(1.0, END))
            f.close()
            window.title(os.path.basename(fil+'-Notepad'))
            window_title = os.path.basename(fil+'-Notepad')
            change_title = False

    else:
        f = open(fil, 'w')
        f.write(text_area.get(1.0, END))
        f.close()
        window.title(os.path.basename(fil+'-Notepad'))
        file_saved = True


def find_func(event=None):
    def find():
        word = find_input.get()
        text_area.tag_remove('match', '1.0', END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_area.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_area.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_area.tag_config(
                    'match', foreground='white', background='grey')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_area.get(1.0, END)
        new_content = content.replace(word, replace_text)
        text_area.delete(1.0, END)
        text_area.insert(1.0, new_content)
    find_dialogue = Toplevel()
    find_dialogue.geometry("400x160+200+100")
    find_dialogue.title("Find and Replace")
    find_dialogue.config(bg="white")
    find_dialogue.resizable(0, 0)
    find_frame = LabelFrame(find_dialogue, bg="white",
                            text="Find/Replace", padx=0)
    find_frame.pack(pady=20)
    text_find = Label(find_frame, text="Find :", bg="white")
    text_replace = Label(find_frame, text="Replace :", bg="white")
    find_input = Entry(find_frame, width=30, bg="white")
    replace_input = Entry(find_frame, width=30, bg="white")
    find_button = Button(find_frame, text="Find",
                         command=find, width=20, bg="white", bd=2)
    replace_button = Button(find_frame, text="Replace",
                            command=replace, width=20, bd=2, bg="white")
    text_find.grid(row=0, column=0, pady=4, padx=4)
    text_replace.grid(row=1, column=0, pady=4, padx=4)
    find_input.grid(row=0, column=1, pady=4, padx=4)
    replace_input.grid(row=1, column=1, pady=4, padx=4)
    find_button.grid(row=2, column=1, pady=4, padx=8)
    replace_button.grid(row=2, column=0, pady=4, padx=8)
    text_find.focus_force()
    find_dialogue.mainloop()


def hide_statusbar(event=None):
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=BOTTOM)
        show_statusbar = True


def selection():
    lines = len(text_area.get("1.0", "end").split('\n'))
    for idx in range(1, lines):
        text_area.tag_add('sel', '{}.0'.format(idx), '{}.end'.format(idx))


# Binding Keys and Text Area
text_area.bind('<<Modified>>', selection)
text_area.bind('<<Modified>>', changed)
window.bind('<Control-f>', find_func)
window.bind('<Control-z>', undo_func)
window.bind('<Control-y>', redo_func)
window.bind('<Control-n>', new_file)
window.bind('<Control-i>', help_pad)
window.bind('<Control-o>', open_file)
window.bind('<Control-Shift-s>', save_as)
window.bind('<Control-s>', save_file)
window.bind('<Control-Delete>', clear_all)
window.wm_protocol("WM_DELETE_WINDOW", quit_func)

# Menu Working
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="New File", font=(
    'arial', '10'), command=new_file, compound=LEFT, accelerator='Ctrl+N')
file_menu.add_command(label="Open File", command=open_file,
                      compound=LEFT, accelerator='Ctrl+O')
file_menu.add_command(label="Save File", command=save_file,
                      compound=LEFT, accelerator='Ctrl+S')
file_menu.add_command(label="Save As", command=save_as,
                      compound=LEFT, accelerator='Ctrl+Shift+S')
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit_func,
                      compound=LEFT, accelerator='Alt+F4')
edit_menu = Menu(menu, tearoff=0)

# Edit Menu
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', compound=LEFT, accelerator='Ctrl+C',
                      command=lambda: text_area.event_generate("<Control c>"))
edit_menu.add_command(label='Cut', compound=LEFT, accelerator='Ctrl+X',
                      command=lambda: text_area.event_generate("<Control x>"))
edit_menu.add_command(label='Paste', compound=LEFT, accelerator='Ctrl+V',
                      command=lambda: text_area.event_generate("<Control v>"))
edit_menu.add_command(label='Undo', compound=LEFT,
                      accelerator='Ctrl+Z', command=undo_func)
edit_menu.add_command(label='Redo', compound=LEFT,
                      accelerator='Ctrl+Y', command=redo_func)
edit_menu.add_separator()
edit_menu.add_command(label='Clear All', command=clear_all,
                      compound=LEFT, accelerator='Ctrl+Delete')
edit_menu.add_command(label='Find and Replace',
                      command=find_func, compound=LEFT, accelerator='Ctrl+F')
edit_menu.add_separator()

# View and Help Menu
view_menu = Menu(window, tearoff=0)
help_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='View', menu=view_menu)
menu.add_cascade(label='Help', menu=help_menu)
view_menu.add_checkbutton(label='Status Bar', onvalue=1, offvalue=False,
                          variable=show_statusbar, compound=LEFT, command=hide_statusbar)
help_menu.add_command(label='About Notepad ', command=help_pad,
                      compound=LEFT, accelerator='Ctrl+I')

# Creating Scroll Bar
hscrollbar = Scrollbar(text_area, orient=HORIZONTAL)
vscrollbar = Scrollbar(text_area, orient=VERTICAL)
sizegrip = Sizegrip(text_area)

# Packing them
hscrollbar.pack(side=BOTTOM, fill=X)
vscrollbar.pack(side=RIGHT, fill=Y)
sizegrip.pack(in_=hscrollbar, side=BOTTOM, anchor="se")

# Configuring them
vscrollbar.config(command=text_area.yview)
hscrollbar.config(command=text_area.xview)
text_area.config(yscrollcommand=vscrollbar.set)
text_area.config(xscrollcommand=hscrollbar.set)


# Windows Configuration
window.config(menu=menu)
window.lift()
window.mainloop()
