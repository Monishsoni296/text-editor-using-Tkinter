import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os

# main window ban rhe hai isse
main_application = tk.Tk()  
main_application.geometry('1200x800')
main_application.title('Deepanshu Text Editor')

# ****************************** Main Menu**********************************

main_menu=tk.Menu()
# file
files = tk.Menu(main_menu,tearoff=True)

# edit
edit = tk.Menu(main_menu,tearoff=True)

# View

view = tk.Menu(main_menu,tearoff=False)

# colourtheme

colour_theme = tk.Menu(main_menu,tearoff=False)

# colourtheme radio
theme_choice = tk.StringVar()


color_dict = {          # text, backgrd
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('#cafc03','#f2666d'),
    'Monokai' : ('#d3b774','#f29e66') ,
    'Night Blue' : ('#ededed','#6b9dc4')
}

# cascade
main_menu.add_cascade(label='File',menu=files)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Colour_Theme',menu=colour_theme)
# ----------------------------End Main Menu---------------------------------

# ****************************** Toolbar **********************************

toolbar = ttk.Label(main_application)
toolbar.pack(side=tk.TOP,fill=tk.X)

# font box
font_touple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(toolbar,width=30,textvariable=font_family,state='readonly')
font_box['values'] = font_touple 
font_box.current(font_touple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

# size box
size_var=tk.IntVar()
font_size = ttk.Combobox(toolbar,width=14,textvariable=size_var)
font_size['values']=tuple(range(8,80,2))
font_size.grid(row=0,column=1,padx=5)
font_size.current(2)

# bold button
bold_btn = ttk.Button(toolbar,text='BOLD')
bold_btn.grid(row=0,column=2,padx=5)
# italics button
italic_btn = ttk.Button(toolbar,text='ITALIC')
italic_btn.grid(row=0,column=3,padx=5)
# underline button
underline_btn = ttk.Button(toolbar,text='UNDERLINE')
underline_btn.grid(row=0,column=4,padx=5)
# colour picker
colour_picker_btn = ttk.Button(toolbar,text='COLOUR')
colour_picker_btn.grid(row=0,column=5,padx=5)
# left allign

left_btn = ttk.Button(toolbar,text='LEFT')
left_btn.grid(row=0,column=6,padx=5)
# center allign

center_btn = ttk.Button(toolbar,text='CENTER')
center_btn.grid(row=0,column=7,padx=5)
# right allign
right_btn = ttk.Button(toolbar,text='RIGHT')
right_btn.grid(row=0,column=8,padx=5)
# ----------------------------End Toolbar ---------------------------------

# ****************************** Text Editor **********************************
text_editor = tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality
current_font_ = 'Arial'
current_size_ = 12
def change_font(main_application): #its not imp to use main_application we can use anything eg: event=None its beacause of bind function beacuse it takes one positional argument
    global current_font_
    current_font_ = font_family.get()
    text_editor.configure(font=(current_font_,current_size_))
def change_size(main_application):
    global current_size_
    current_size_=size_var.get()
    text_editor.configure(font=(current_font_,current_size_))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)
text_editor.configure(font=('Arial',12))

# Buttons functionality
# bold button
def change_bold():
    bold_prop = tk.font.Font(font=text_editor['font'])
    if bold_prop.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_,current_size_,'bold'))
    if bold_prop.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_,current_size_,'normal'))
bold_btn.configure(command=change_bold)
# italic button
def change_italic():
    italic_prop = tk.font.Font(font=text_editor['font'])
    if italic_prop.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_,current_size_,'italic'))
    if italic_prop.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_,current_size_,'roman'))
italic_btn.configure(command=change_italic)
# underline button
def change_underline():
    underline_prop = tk.font.Font(font=text_editor['font'])
    if underline_prop.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_,current_size_,'underline'))
    if underline_prop.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_,current_size_,'normal'))
underline_btn.configure(command=change_underline)
# font color
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
colour_picker_btn.configure(command=change_font_color)

# align left 
def align_lefty():
    text_str = text_editor.get(1.0,'end')
    text_editor.tag_configure('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_str,'left')

left_btn.configure(command=align_lefty)
#align center
def align_centre():
    text_str = text_editor.get(1.0,'end')
    text_editor.tag_configure('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_str,'center')

center_btn.configure(command=align_centre)
# align right
def align_righty():
    text_str = text_editor.get(1.0,'end')
    text_editor.tag_configure('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_str,'right')

right_btn.configure(command=align_righty)


# ----------------------------End Text Editor---------------------------------


# ****************************** Statusbar **********************************
status_bar = ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)
txt_changed = False
def tell_status(event=None):
    global txt_changed
    if text_editor.edit_modified():
        txt_changed=True
        words = len(text_editor.get(1.0,'end-1c').split())
        chrs = len(text_editor.get(1.0,'end-1c').replace(" ","")) 
        status_bar.config(text=f"Characters : {chrs} Words : {words}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>",tell_status)
# ----------------------------End Statusbar---------------------------------


# ****************************** Main Menu Functions **********************************

# file commands
url = ""
def new_file(event = None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

def save_file(event=None):
    global url
    try:
        if url:
            with open(url,'w',encoding='utf-8') as fw:
                cont = str(text_editor.get(1.0,tk.END))
                fw.write(cont)
        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
            cont2=text_editor.get(1.0,tk.END)
            url.write(cont2)
            url.close()
    except:
        return
    
def save_as_file(event=None):
    global url
    try:
        content=text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
        url.write(content)
        url.close()
    except:
        return

def exit_file(event=None):
    global url,txt_changed
    try:
        if txt_changed:
            m_box = messagebox.askyesnocancel('Warning','Do you want to save the file')
            if m_box is True:
                if url:
                    conte = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding=utf-8) as gw:
                        gw.write(conte)
                        main_application.destroy()    
                else:
                    conte2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
                    url.write(conte2)
                    url.close()
                    main_application.destroy()
            elif m_box is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return


files.add_command(label='New',compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)
files.add_command(label='Open',compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
files.add_command(label='Save',compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
files.add_command(label='Save As',compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as_file)
files.add_command(label='Exit',compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_file)

# edit commands
def find_func(event=None):
    def find():
        word = find_entry.get()
        text_editor.tag_remove('match',1.0,tk.END)
        match=0
        if word:
            start_pos=1.0
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                match+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word=find_entry.get()
        replace_text = replace_entry.get()
        content=text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dia = tk.Toplevel()
    find_dia.geometry('450x250+500+200')
    find_dia.title('Find')
    find_dia.resizable(0,0)
    # frame
    find_frame = ttk.LabelFrame(find_dia,text='Find/Replace')
    find_frame.pack(pady=20)
    # labels
    find_label = ttk.Label(find_frame,text='Find')
    find_label.grid(row=0,column=0,padx=4,pady=4)
    replace_label = ttk.Label(find_frame,text='replace')
    replace_label.grid(row=1,column=0,padx=4,pady=4)
    # entrybox
    find_entry = ttk.Entry(find_frame,width=30)
    find_entry.grid(row=0,column=1,padx=4,pady=4)
    replace_entry = ttk.Entry(find_frame,width=30)
    replace_entry.grid(row=1,column=1,padx=4,pady=4)
    # buttons
    find_btn = ttk.Button(find_frame,text='Find',command=find)
    find_btn.grid(row=2,column=0,padx=4,pady=4)
    replace_btn = ttk.Button(find_frame,text='Replace',command=replace)
    replace_btn.grid(row=2,column=1,padx=4,pady=4)
    find_dia.mainloop()


edit.add_command(label='Copy',compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate('<Control c>'))
edit.add_command(label='Paste',compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
edit.add_command(label='Cut',compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
edit.add_command(label='Clear All',compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=lambda: text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)

# view check buttons
tool_var=tk.BooleanVar()
tool_var.set(True)
status_var=tk.BooleanVar()
status_var.set(True)

def hide_toolbar():
    global tool_var
    if tool_var:
        toolbar.pack_forget()
        tool_var = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        toolbar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        tool_var=True

def hide_statusbar():
    global status_var
    if status_var:
        status_bar.pack_forget()
        status_var = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        status_var=True

view.add_checkbutton(label='Tool bar',offvalue=0,onvalue=1,variable=tool_var,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status bar',offvalue=0,onvalue=1,variable=status_var,compound=tk.LEFT,command=hide_statusbar)

# colortheme
def change_theme():
    choosen_theme = theme_choice.get()
    color_tuple = color_dict[choosen_theme]
    fgg,bgg=color_tuple[0],color_tuple[1]
    text_editor.config(background=bgg,fg=fgg)

for i in color_dict:
    colour_theme.add_radiobutton(label=i,variable=theme_choice,compound=tk.LEFT,command=change_theme)
    
# ----------------------------End Main Menu Functions---------------------------------

# bind shortcut keys
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_as_file)
main_application.bind("<Control-q>",exit_file)
main_application.bind("<Control-f>",find_func)

main_application.configure(menu=main_menu)
main_application.mainloop()