# #from tkinter import *
from tkinter import *
from tkinter import ttk
import time
# from tkinter import messagebox
# from PIL import ImageTk
# from PIL import Image


#make tkinter-compatible image
#img = ImageTk.PhotoImage(Image.open("Documents/GitHub/Chinese-Memory-Game/Chinese_bg.jpg"))


window = Tk()
#titles the window
window.title('Chinese Memory Game')

#outside box color (window)
window.configure(bg='gold')
#creates size of the canvas
canvas = Canvas(window, width=370,height=450)
# filename = PhotoImage(file = "C:\\GitHub\\Chinese-Memory-Game\\Chinese_bg.png")
# background_label = Label(window, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
canvas.pack()

#inside box color (canvas)
canvas.configure(bg= 'red')

# panel = tk.Label(window, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")



#b1 = ttk.Button(window,text= "hello")


#if button is clicked, then start timer (call timer function). have timer function
#wait 5 seconds and then turn plain background back to red/yellow

#covers for buttons after click
def cover1():
    canvas.create_rectangle(40,50,120,120, fill = 'maroon')

def cover2():
    canvas.create_rectangle(40,180,120,250, fill = 'maroon')

def cover3():
    canvas.create_rectangle(40,310,120,380, fill = 'maroon')

def cover4():
    canvas.create_rectangle(240,50,320,120, fill = 'maroon')

def cover5():
    canvas.create_rectangle(240,180,320,250, fill = 'maroon')

def cover6():
    canvas.create_rectangle(240,310,320,380, fill = 'maroon')

#def timer(button):
    #timer = button.after(1000, cover6)

#def cardBack(self):
    #self.button = Button(self, command = self.color_change, bg = "red")
    #self.button.grid(row = 2, column = 2, sticky = W)


#button functions for when clicked

def button1text():
    print("编码")
    #we want this function to create a new rectangle that has text or image displayed on it
    #add background color change for all buttons
    canvas.create_rectangle(40,50,120,120, fill = 'yellow')
    canvas.create_text(80,80,  fill = "maroon", text='编码')
    canvas.create_text(80,100, fill = "maroon", text='bian1 ma3')
    canvas.after(4000, cover1)



def button2text():
    #add background color change for all buttons

    print("软件")
    canvas.create_rectangle(40,180,120,250, fill = 'yellow')
    #canvas.create_text(80,210, fill = "red", text='游戏')
    canvas.create_text(80,210, fill = "maroon", text='软件')
    canvas.create_text(80,230, fill = "maroon", text='ruan3 jian4')
    canvas.after(4000, cover2)
    #button["bg"] = "red"

def button3text():
    #add background color change for all buttons
    print("算法")
    canvas.create_rectangle(40,310,120,380, fill = 'yellow')
    canvas.create_text(80,340, fill = "maroon", text='算法')
    canvas.create_text(80,360, fill = "maroon", text='suan4 fa3')
    canvas.after(4000, cover3)

def button4text():
    print("硬件")
    canvas.create_rectangle(240,50,320,120, fill = 'yellow')
    canvas.create_text(280,80,  fill = "maroon",  text='硬件')
    canvas.create_text(280,100,  fill = "maroon",  text='ying4 jian4')
    canvas.after(4000, cover4)

def button5text():
    print("键盘")
    canvas.create_rectangle(240,180,320,250, fill = 'yellow')
    canvas.create_text(280,210,  fill = "maroon", text='键盘')
    canvas.create_text(280,230,  fill = "maroon", text='jian4 pan2')
    canvas.after(4000, cover5)

def button6text():
    print("便宜")
    canvas.create_rectangle(240,310,320,380, fill = 'yellow')
    canvas.create_text(280,340, fill = "maroon", text='电脑')
    canvas.create_text(280,360, fill = "maroon", text='dian4 nao3')
    canvas.after(4000, cover6)



def home_screen():
#create six cards that will flip when
#clicked on/when click on the adjacent "click" button

    #create card position 50,50, of size 60 by 70

    #create variables with each card location

    #button variables: location, command, style
    cover1()
    b1 = ttk.Button(canvas, text = "Coding", command=button1text)
    b1.place(x = 40, y = 140)

    cover2()
    b2 = ttk.Button(canvas, text = "Software", command=button2text)
    b2.place(x = 40, y = 270)

    cover3()
    b3 = ttk.Button(canvas, text = "Algorithm", command=button3text)
    b3.place(x = 40, y = 390)

    cover4()
    b4 = ttk.Button(canvas, text = "Hardware", command=button4text)
    b4.place(x = 240, y = 140)

    cover5()
    b5 = ttk.Button(canvas, text = "Keyboard", command=button5text)
    b5.place(x = 240, y = 270)

    cover6()
    #card6 = canvas.create_rectangle(250,310,310,380, fill = 'maroon')
    b6 = ttk.Button(canvas, text = "Computer", command=button6text)
    b6.place(x = 240, y = 390)



    # button1 = button1text()
    # button2 = button2text()



    #def button_check():
        #if button1 = button2


# var = IntVar()
#
# c = Checkbutton(canvas, text="Expand", variable=var)
# c.pack()
#
# mainloop()

# v = IntVar()
#
# Radiobutton(canvas, text="One", variable=v, value=1).pack(anchor=W)
# Radiobutton(canvas, text="Two", variable=v, value=2).pack(anchor=W)
#
# mainloop()







home_screen()

#if card1 is clicked, show "this is card one"
def callback():
    print( "click!")

b = Button(window, text="OK", command=callback)
window.mainloop()
