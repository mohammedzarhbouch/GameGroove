from tkinter import *
from tkinter import messagebox
from tkinter import Tk, Frame, Button

window = Tk()
window.title('Tic Tac Toe')
window.attributes("-fullscreen", True)
window.geometry("1200x710")
window.config(background="#12BDAC")

clicked = True
count = 0

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="#1BAC12")
        b2.config(bg="#1BAC12")
        b3.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X heeft gewonnen")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="#1BAC12")
        b5.config(bg="#1BAC12")
        b6.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X heeft gewonnen")
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="#1BAC12")
        b8.config(bg="#1BAC12")
        b9.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X heeft gewonnen")
        disable_all_buttons()



    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="#1BAC12")
        b4.config(bg="#1BAC12")
        b7.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X heeft gewonnen")
        disable_all_buttons()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="#1BAC12")
        b5.config(bg="#1BAC12")
        b8.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X heeft gewonnen")
        disable_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="#1BAC12")
        b6.config(bg="#1BAC12")
        b9.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X heeft gewonnen")
        disable_all_buttons()


    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="#1BAC12")
        b5.config(bg="#1BAC12")
        b9.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X heeft gewonnen")
        disable_all_buttons()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="#1BAC12")
        b5.config(bg="#1BAC12")
        b7.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X heeft gewonnen")
        disable_all_buttons()

    #### CHECK FOR O WIN ####
        
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="#1BAC12")
        b2.config(bg="#1BAC12")
        b3.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O heeft gewonnen")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="#1BAC12")
        b5.config(bg="#1BAC12")
        b6.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O heeft gewonnen")
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="#1BAC12")
        b8.config(bg="#1BAC12")
        b9.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O heeft gewonnen")
        disable_all_buttons()



    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="#1BAC12")
        b4.config(bg="#1BAC12")
        b7.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O heeft gewonnen")
        disable_all_buttons()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="#1BAC12")
        b5.config(bg="#1BAC12")
        b8.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O heeft gewonnen")
        disable_all_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="#1BAC12")
        b6.config(bg="#1BAC12")
        b9.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O heeft gewonnen")
        disable_all_buttons()


    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="#1BAC12")
        b5.config(bg="#1BAC12")
        b9.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O heeft gewonnen")
        disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="#1BAC12")
        b5.config(bg="#1BAC12")
        b7.config(bg="#1BAC12")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O heeft gewonnen")
        disable_all_buttons()


    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "Losers niemand won")
        disable_all_buttons()

def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Is al gepakt... \n Pak andere vak a sahbi")

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8 ,b9
    global clicked, count
    clicked = True
    count = 0



    frame = Frame(window)
    frame.grid(row=0, column=0, padx=10, pady=10)

    b1= Button(window, text=" ", font=("Comic Sans MS", 30), height=2, width=6, bg="#12BDAC", command=lambda: b_click(b1))
    b2= Button(window, text=" ", font=("Comic Sans MS", 30), height=2, width=6, bg="#12BDAC", command=lambda: b_click(b2))
    b3= Button(window, text=" ", font=("Comic Sans MS", 30), height=2, width=6, bg="#12BDAC", command=lambda: b_click(b3))

    b4= Button(window, text=" ", font=("Comic Sans MS", 30), height=2, width=6, bg="#12BDAC", command=lambda: b_click(b4))
    b5= Button(window, text=" ", font=("Comic Sans MS", 30), height=2, width=6, bg="#12BDAC", command=lambda: b_click(b5))
    b6= Button(window, text=" ", font=("Comic Sans MS", 30), height=2, width=6, bg="#12BDAC", command=lambda: b_click(b6))

    b7= Button(window, text=" ", font=("Comic Sans MS", 30), height=2, width=6, bg="#12BDAC", command=lambda: b_click(b7))
    b8= Button(window, text=" ", font=("Comic Sans MS", 30), height=2, width=6, bg="#12BDAC", command=lambda: b_click(b8))
    b9= Button(window, text=" ", font=("Comic Sans MS", 30), height=2, width=6, bg="#12BDAC", command=lambda: b_click(b9))


    b1.place(relx=0.4, rely=0.33, anchor="center")
    b2.place(relx=0.5, rely=0.33, anchor="center")
    b3.place(relx=0.6, rely=0.33, anchor="center")

    b4.place(relx=0.4, rely=0.5, anchor="center")
    b5.place(relx=0.5, rely=0.5, anchor="center")
    b6.place(relx=0.6, rely=0.5, anchor="center")

    b7.place(relx=0.4, rely=0.67, anchor="center")
    b8.place(relx=0.5, rely=0.67, anchor="center")
    b9.place(relx=0.6, rely=0.67, anchor="center")

    buttonQuit = Button(
        window,
        text="Quit",
        bg="red",
        font=("Helvetica", 18),
        command=exit,
        width=12 )
    
    buttonQuit.place(relx= 0.44, rely= 0.8)



my_menu = Menu(window)
window.config(menu=my_menu)


options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset", command=reset)

reset()

window.mainloop()