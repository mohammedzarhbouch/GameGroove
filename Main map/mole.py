# test.py

from tkinter import Label, ttk, PhotoImage
import random
import tkinter
from PIL import Image, ImageTk

def onSelectionButtonClick4(selectionWindow):
    selectionWindow.destroy()
    startMole()

def startMole():
    try:
        
        global score
        score = 0

        def Close(): 
            window.destroy()

        def updateScore():
            global score 
            score += 1
            scorePosition.config(text=("point(s):",score))

        def onClick(event):
            pointImageLabel.place(relx=random.uniform(0.1 , 0.9), rely=random.uniform(0.15 , 0.85), anchor=tkinter.CENTER)
            
            print()
            updateScore()
            
            
            

        def onImageClick(event):
            Close()
        window = tkinter.Tk()
        




        window.attributes('-fullscreen', True)
        window.geometry("800x800")
        window.configure(bg="black")


        scorePosition = Label(window, text=("point(s):", score), font=("Black italic", 50), bg="black", fg="white")
        scorePosition.pack(pady=(30, 0))


        # exit button
        exitImg_path = "img/exitred.png"
        exitImg = Image.open(exitImg_path)
        exitImg = exitImg.resize((150, 100))    
        exitImg = ImageTk.PhotoImage(exitImg)

        exitImageLabel = Label(window, image=exitImg, bg="black", width=200)
        exitImageLabel.pack(side=tkinter.TOP, anchor=tkinter.NE, padx=20, pady=20)

        exitImageLabel.bind("<Button-1>", onImageClick)

        grassImgPath = "img/green-grass.jpg"
        grassImg = Image.open(grassImgPath)
        grassImg = grassImg.resize((1250, 1000))
        grassImg = ImageTk.PhotoImage(grassImg)

        # Set the grass image as the background of gameWindow
        gameWindow = tkinter.Canvas(window, width=1500, height=1000, bg='green', highlightthickness=0)
        gameWindow.pack(pady=(0, 100))

        # gameWindow.create_image(0, 0, anchor=tkinter.NW, image=grassImg)

        # point button
        pointImg_path = "img/nobg.png"
        pointImg = Image.open(pointImg_path)
        pointImg = pointImg.resize(size=(150,150))
        pointImg = ImageTk.PhotoImage(pointImg)

        pointImageLabel = Label(gameWindow, image=pointImg, width=150, height=150, highlightthickness=0)
        pointImageLabel.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        pointImageLabel.config(bg="green") 
        pointImageLabel.bind("<Button-1>", onClick)



        window.mainloop()
    except Exception as e:
        print(f"Error during test: {e}")
