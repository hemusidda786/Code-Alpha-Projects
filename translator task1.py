from  tkinter import *
from  translate (import) Translator 

#create a window 
window =Tk()
window.title("language translator")

# Add a grid to window 
mainframe = Frame(window)
mainframe.grid(column=0,row=0)
#mainframe.columnconfigure(0,weight=1)
#mainframe.rowconfigure(0,weight=1)
mainframe.pack(pady =100,padx = 100)

#variables to set languages
Lan1 = StringVar(window)
Lan2=StringVar(window)

#funtion which translates the given text
def trans():
    translator = Translator(from_lan = Lan1.get(), to_lang=Lan2.get())
    translation = translator.translate(Var.get())
    Var1.set(translation)

#select language
Choice = {"ENGLISH","HINDI"}
lan1menu = OptionMenu( mainframe, Lan1, *Choice )
Label(mainframe,text="select language").grid(row =0, column=1)
lan1menu.grid(row =1, column=1)


lan2menu = OptionMenu( mainframe ,Lan2,*Choice)
Label(mainframe, text="select language").grid(row= 0, column =1)
lan2menu.grid(row=1, column=1)

#input text field 
Label(mainframe, text = "enter text").grid(row=2,column=0)
Var =StringVar()
Textbox = Entry(mainframe ,textvariable = Var).grid(row=2,column=1)

#output text field 
Label(mainframe, text ="output").grid(row=2,column=2)
Var1 =StringVar()
Textbox = Entry(mainframe, textvariable = Var1).grid(row=2,column=3)

Button =Button(mainframe,text= 'translate', command = trans).grid(row=3,column=1, columnspan=3)


window.mainloop()