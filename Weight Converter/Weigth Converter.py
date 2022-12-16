from tkinter import *
 
window = Tk()
window.iconbitmap(r"C:\Users\abhis\OneDrive\Desktop\Abhishek D Jaiswar\Project\Own Projects\Python\Weight Converter\icoimg.ico")
window.title("Weigth Converter")

def convert_from_kg_to():
     
    gram = float(value.get())*1000
    
    dekagram = float(value.get())*100
     
    hectogram = float(value.get())*10

    merticton = float(value.get())/1000
    
    pound = float(value.get())*2.20462
     
    ounce = float(value.get())*35.274

    stone = float(value.get())/6.35
     
    t1.delete("1.0", END)
    t1.insert(END,gram)
     
    t2.delete("1.0", END)
    t2.insert(END,dekagram)
     
    t3.delete("1.0", END)
    t3.insert(END,hectogram)

    t4.delete("1.0", END)
    t4.insert(END,merticton)
     
    t5.delete("1.0", END)
    t5.insert(END,pound)
     
    t6.delete("1.0", END)
    t6.insert(END,ounce)

    t7.delete("1.0", END)
    t7.insert(END, stone)
 
e1 = Label(window, text = "Enter the weight in Kg")
value = StringVar()
e2 = Entry(window, textvariable = value)
e3 = Label(window, text = 'Gram')
e4 = Label(window, text = 'Decakgram')
e5 = Label(window, text = 'Hectogram')
e6 = Label(window, text = 'Metric Ton')
e7 = Label(window, text = 'Pounds')
e8 = Label(window, text = 'Ounce')
e9 = Label(window, text = 'Stone')
 
t1 = Text(window, height = 1, width = 20)
t2 = Text(window, height = 1, width = 20)
t3 = Text(window, height = 1, width = 20)
t4 = Text(window, height = 1, width = 20)
t5 = Text(window, height = 1, width = 20)
t6 = Text(window, height = 1, width = 20)
t7 = Text(window, height = 1, width = 20)
 
b1 = Button(window, text = "Convert", fg = "black", bg = "gray95", command = convert_from_kg_to)
 
e1.grid(row = 0, column = 0)
e2.grid(row = 0, column = 1)
b1.grid(row = 0, column = 2)
e3.grid(row = 1, column = 0)
e4.grid(row = 1, column = 1)
e5.grid(row = 1, column = 2)
e6.grid(row = 3, column = 0)
e7.grid(row = 3, column = 1)
e8.grid(row = 3, column = 2)
e9.grid(row = 5, column = 1)
t1.grid(row = 2, column = 0)
t2.grid(row = 2, column = 1)
t3.grid(row = 2, column = 2)
t4.grid(row = 4, column = 0)
t5.grid(row = 4, column = 1)
t6.grid(row = 4, column = 2)
t7.grid(row = 6, column = 1)


window.mainloop()
