from tkinter import *


root=Tk()
root.title("Dictionary")
root.geometry("600x400")

click_me = Label(root)


def clickMe():
    click_me["text"] = dictionary['Click Me']
    
    
btn0= Button(root , text = "Click Me",command = click_me)
btn0.place(relx = 0.5, rely= 0.2, anchor = CENTER)





root.mainloop()
 