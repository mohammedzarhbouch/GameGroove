# test.py

import tkinter
from PIL import Image, ImageTk
from sys import exit

def startTest(main_window):
    try:
         originalImage = Image.open(imagePath)

         # Get the screen width and height
         screen_width = main_window.winfo_screenwidth()
         screen_height = main_window.winfo_screenheight()

         # Resize the image to the screen size
         resizedImage = originalImage.resize((screen_width, screen_height))

         # Convert the Pillow image to a Tkinter-compatible format
         tkImage = ImageTk.PhotoImage(resizedImage)

         # Create a label with the resized image
         backgroundLabel = tkinter.Label(main_window, image=tkImage)
         backgroundLabel.place(relwidth="1", relheight="1")
    except Exception as e:
        print(f"Error during test: {e}")
