import tkinter

root = tkinter.Tk()

root.title("Hello World!!!")  # sets the title of the window
root.geometry("600x200")  # sets the window's width and height

# create a label
my_label = tkinter.Label(root)  # creates a label and attaches it to the window
my_label.config(text="Hello!", fg="green")  # options to configure the label
my_label.grid()  # a special method for placing the widget on the window


#create a label
my_label2 = tkinter.Label(root)
my_label2.config(text="Hey there!", fg="blue")
my_label2.grid()

#create a label
my_label3 = tkinter.Label(root)
my_label3.config(text="Hey you!", fg="pink")  
my_label3.grid()
root.mainloop()
