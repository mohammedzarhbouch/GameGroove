
import tkinter 
from PIL import Image, ImageTk
from selection import onStartButtonClick

def startMain():
    window = tkinter.Tk()
    window.attributes("-fullscreen", True)

    imagePath = "img/plz.png"

    try:
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

        startButton = tkinter.Button(
            window,
            text="Start!",
            bg="lightblue",
            fg="white",
            font=("Arial", 20),
            padx=30,
            pady=2,
            command=lambda: onStartButtonClick(window)  # Pass the main window to the function
        )
        startButton.place(relx=0.5, rely=0.58, anchor="center") 

        quitButton = tkinter.Button(
            window,
            text="Quit",
            command=exit,
            bg="indian red",
            fg="white",
            font=("Arial", 16),
            padx=15,
            pady=2
        )
        quitButton.place(relx=0.5, rely=0.65, anchor="center")

        window.mainloop()

    except Exception as e:
        # Print the exception to understand the issue
        print(f"Error loading/resizing image: {e}")

if __name__ == "__main__":
    startMain()
