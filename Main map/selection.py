import tkinter
from PIL import Image, ImageTk
from ttt import onSelectionButtonClick
from aimtrainer import onSelectionButtonClick2
from Snake import onSelectionButtonClick3
from mole import onSelectionButtonClick4

def onStartButtonClick(mainWindow):
    
    mainWindow.destroy()  # Close the main window created by main.py
    startSelection()  # Start the new window with buttons


def startSelection():
    window = tkinter.Tk()
    window.attributes("-fullscreen", True)

    imagePath = "img/plz.png"

    # Open the image using Pillow
    originalImage = Image.open(imagePath)

    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Resize the image to the screen size
    resizedImage = originalImage.resize((screen_width, screen_height))

    # Convert the Pillow image to a Tkinter-compatible format
    tkImage = ImageTk.PhotoImage(resizedImage)

    # Create a label with the resized image
    backgroundLabel = tkinter.Label(window, image=tkImage)
    backgroundLabel.place(relwidth="1", relheight="1")



    miniGame1 = tkinter.Button(window, text="Wack a Mole", width=40, height=10, bg="red", command=lambda: onSelectionButtonClick4(window))
    miniGame2 = tkinter.Button(window, text="Tic Tac Toe", width=40, height=10, bg="red", command=lambda: onSelectionButtonClick(window))
    miniGame3 = tkinter.Button(window, text="Aim Trainer", width=40, height=10, bg="red", command=lambda: onSelectionButtonClick2(window))
    miniGame4 = tkinter.Button(window, text="Snake", width=40, height=10, bg="red", command=lambda: onSelectionButtonClick3(window))

    miniGame1.place(rely= 0.3, relx=0.3)
    miniGame2.place(rely= 0.3, relx=0.5)
    miniGame3.place(rely= 0.5, relx=0.3)
    miniGame4.place(rely= 0.5, relx=0.5)

    window.mainloop()