import tkinter
root = tkinter.Tk()

button1 = tkinter.Button(root)
button1.config(text="MOOD",
               bg= "pink",
               fg="light blue",
               font=("Wide Latin", "50"))

button1.grid()

root.mainloop()