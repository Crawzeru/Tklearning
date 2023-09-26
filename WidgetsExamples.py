from tkinter import *
#window
window=Tk()
window.title("Example")
window.minsize(600,600)
window.config(padx=20,pady=20)

#label
my_label=Label(text="This is example")
my_label.config(bg="black")
my_label.config(fg="white")
my_label.config(padx=10,pady=10)
my_label.pack()

def button_clicked():
    print(my_text.get("1.0",END)) #MULTİLİNE DAKİ TEXT İ ALIRKEN BÖYLE YAPILIR.
#button
my_button=Button(text="button",command=button_clicked)
my_button.config(padx=10,pady=10)
my_button.pack()

#entry
my_entry=Entry(width=20)
my_entry.focus()
my_entry.pack()
#multiline
my_text=Text(width=20,height=20)
my_text.pack()
#scale
def scale_selected(value):#yazdırır
    print(value)
my_scale=Scale(from_=0,to=50,command=scale_selected)
my_scale.pack()

#spinbox
def spinbox_selected():
    print(my_spinbox.get())
my_spinbox=Spinbox(from_=0,to=50,command=spinbox_selected)
my_spinbox.pack()

#checkbutton
def check_button_selected():
    print(check_state.get())#bu tıklandı mı tıklanmadı mı onu kontrol eder

check_state=IntVar()
my_checkbutton=Checkbutton(text="Check",variable=check_state,command=check_button_selected)
my_checkbutton.pack()

#radio button
def radio_selected():
    print(radio_check.get())
radio_check=IntVar()
my_radiobutton=Radiobutton(text="1.option",value=10,variable=radio_check,command=radio_selected)
my_radiobutton2=Radiobutton(text="1.option",value=20,variable=radio_check,command=radio_selected)
my_radiobutton.pack()
my_radiobutton2.pack()

#listbox

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox=Listbox()
name_list=["baho","atil","KGM","TTK","KKT"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])
my_listbox.bind('<<ListboxSelect>>',listbox_selected)#tıklandığında bişi yapmasını istiyorsan bunu yapman lazım
my_listbox.pack()

window.mainloop()