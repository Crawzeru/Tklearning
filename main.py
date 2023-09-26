import tkinter

#window
window=tkinter.Tk()
window.title("Learning")
window.minsize(500,300)

def button_clicked():
    user_input=my_entry.get()#ne yazıldıysa onu string olarak verir
    print(user_input)
#label-metin gösterme
my_label=tkinter.Label(text="This is a label",font=("Arial",20,"normal"))
#my_label.config(bg="black",fg="white")
#my_label.pack()
my_label.grid(row=0,column=0)
#button

my_button=tkinter.Button(text="This is a button",command=button_clicked)
#my_button.pack()
my_button.grid(row=2,column=0)
#entry

my_entry=tkinter.Entry(width=28)
#my_entry.pack()
my_entry.grid(row=1,column=0)

window.mainloop()