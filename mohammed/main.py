import tkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk

window = tkinter.Tk()


window.attributes("-fullscreen", True)
window.geometry("400x400")

imagePath = "img/plz.png"

try:
    # Open the image using Pillow
    originalImage = Image.open(imagePath)

    # Resize the image using Pillow
    resizedImage = originalImage.resize((1920, 1080))  # Specify the desired size

    # Convert the Pillow image to a Tkinter-compatible format
    tkImage = ImageTk.PhotoImage(resizedImage)

    # Create a label with the resized image
    backgroundLabel = tkinter.Label(window, image=tkImage)
    backgroundLabel.place(relwidth="1", relheight="1")

except Exception as e:
    # Print the exception to understand the issue
    print(f"Error loading/resizing image: {e}")




window.mainloop()