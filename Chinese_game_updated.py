# #from tkinter import *
from tkinter import *
from tkinter import ttk
import time


#titles the window
window = Tk()
window.title('Chinese Memory Game')
#creates size of the canvas
canvas = Canvas(window, width=400,height=450)
canvas.pack()

b1 = ttk.Button(window,text= "hello")


#if button is clicked, then start timer (call timer function). have timer function
#wait 5 seconds and then turn plain background back to red/yellow

#covers for buttons after click
def cover1():
    canvas.create_rectangle(50,50,110,120, fill = 'maroon')

def cover2():
    canvas.create_rectangle(50,180,110,250, fill = 'maroon')

def cover3():
    canvas.create_rectangle(50,310,110,380, fill = 'maroon')

def cover4():
    canvas.create_rectangle(250,50,310,120, fill = 'maroon')

def cover5():
    canvas.create_rectangle(250,180,310,250, fill = 'maroon')

def cover6():
    canvas.create_rectangle(250,310,310,380, fill = 'maroon')

#def timer(button):
    #timer = button.after(1000, cover6)

#def cardBack(self):
    #self.button = Button(self, command = self.color_change, bg = "red")
    #self.button.grid(row = 2, column = 2, sticky = W)


#button functions for when clicked

def button1text():
    print("你好")
    #we want this function to create a new rectangle that has text or image displayed on it
    #add background color change for all buttons
    canvas.create_rectangle(50,50,110,120, fill = 'yellow')
    canvas.create_text(80,80,  fill = "maroon", text='你好')
    canvas.after(2000, cover1)



def button2text():
    #add background color change for all buttons

    print("游戏")
    canvas.create_rectangle(50,180,110,250, fill = 'yellow')
    #canvas.create_text(80,210, fill = "red", text='游戏')
    canvas.create_text(80,210, fill = "red", text='hello')
    canvas.after(2000, cover2)
    #button["bg"] = "red"

def button3text():
    #add background color change for all buttons
    print("写字")
    canvas.create_rectangle(50,310,110,380, fill = 'yellow')
    canvas.create_text(80,340, fill = "red", text='写字')
    canvas.after(2000, cover3)

def button4text():
    print("唱歌")
    canvas.create_rectangle(250,50,310,120, fill = 'yellow')
    canvas.create_text(280,80,  fill = "red",  text='唱歌')
    canvas.after(2000, cover4)

def button5text():
    print("画画")
    canvas.create_rectangle(250,180,310,250, fill = 'yellow')
    canvas.create_text(280,210,  fill = "red", text='画画')
    canvas.after(2000, cover5)

def button6text():
    print("便宜")
    canvas.create_rectangle(250,310,310,380, fill = 'yellow')
    canvas.create_text(280,340, fill = "red", text='便宜')
    canvas.after(2000, cover6)



def home_screen():
#create six cards that will flip when
#clicked on/when click on the adjacent "click" button

    #create card position 50,50, of size 60 by 70

    #create variables with each card location

    #button variables: location, command, style
    cover1()
    b1 = ttk.Button(canvas, text = "Click me", command=button1text)
    b1.place(x = 40, y = 140)

    cover2()
    b2 = ttk.Button(canvas, text = "Click me", command=button2text)
    b2.place(x = 40, y = 270)

    cover3()
    b3 = ttk.Button(canvas, text = "Write Characters", command=button3text)
    b.place(x = 40, y = 390)

    cover4()
    b4 = ttk.Button(canvas, text = "Sing", command=button4text)
    b.place(x = 240, y = 140)

    cover5()
    b5 = ttk.Button(canvas, text = "Draw", command=button5text)
    b.place(x = 240, y = 270)

    cover6()
    #card6 = canvas.create_rectangle(250,310,310,380, fill = 'maroon')
    b6 = ttk.Button(canvas, text = "Cheap", command=button6text)
    b.place(x = 240, y = 390)



    button1 = button1text()
    button2 = button2text()



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
