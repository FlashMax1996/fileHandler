from tkinter import *
from tkinter import ttk
import csv
from tkinter import filedialog

def openFile():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                 filetypes=(("CSV", "*.csv"), ("All files", "*.*")))
    print(filename)

    try:
        with open(filename, 'r') as UseFile:
            reader = csv.DictReader(UseFile, delimiter=',')
            for row in reader:
                firstname = row['firstname']
                lastname = row['lastname']
                address = row['address']
                tree.insert("", 0, values=(firstname, lastname, address))
    except:
        print("No file exists")

def tabs(TableMargin, tree):


    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Firstname', text="Firstname", anchor=W)
    tree.heading('Lastname', text="Lastname", anchor=W)
    tree.heading('Address', text="Address", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

window = Tk()
window.title("Programm")
window.geometry('800x500')
menu = Menu(window)
file = Menu(menu)
file.add_command(label='Загрузить', command=openFile)
file.add_command(label='Сохранить')
file.add_command(label='Выход', command=window.destroy)
menu.add_cascade(label='Файл', menu=file)

handle = Menu(menu)
handle.add_command(label='1')
handle.add_command(label='2')
handle.add_command(label='3')
handle.add_command(label='4')
handle.add_command(label='5')
menu.add_cascade(label='Обработка', menu=handle)


other = Menu(menu)
other.add_command(label='1')
other.add_command(label='2')
other.add_command(label='3')
menu.add_cascade(label='Прочее', menu=other)
window.config(menu=menu)

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Отображение исходного файла')
tab_control.add(tab2, text='Отображение обработанного файла')
tab_control.add(tab3, text='Какая-то статистика с графиками')

TableMargin = Frame(tab1, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Firstname", "Lastname", "Address"), height=400, selectmode="extended",
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
tabs(TableMargin, tree)

TableMargin2 = Frame(tab2, width=500)
TableMargin2.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin2, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin2, orient=VERTICAL)
tree2 = ttk.Treeview(TableMargin2, columns=("Firstname", "Lastname", "Address"), height=400, selectmode="extended",
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
tabs(TableMargin2, tree2)

lbl3 = Label(tab3, text='Вкладка 3')
lbl3.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')



#============================INITIALIZATION==============================
if __name__ == '__main__':
    window.mainloop()