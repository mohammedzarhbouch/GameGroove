# test.py

import tkinter

def onStartButtonClick(mainWindow):
    print("Start button clicked in test.py!")
    mainWindow.destroy()  # Close the main window created by main.py
    startTest()  # Start the new window with buttons

def startTest():
    try:
        # Set up the window
        testWindow = tkinter.Tk()
        testWindow.title("Button Grid")
        testWindow.configure(bg="black")
        testWindow.attributes("-fullscreen", True)

        # Create a 2 by 2 grid of buttons
        for row in range(2):
            for col in range(2):
                button_number = row * 2 + col + 1  # Button number from 1 to 4
                button_text = f"Button {button_number}"

                button = tkinter.Button(
                    testWindow,
                    text=button_text,
                    font=("Arial", 12),
                    bg="white",
                    fg="black",
                    padx=10,
                    pady=5
                )
                button.grid(row=row, column=col, padx=10, pady=10)

        testWindow.mainloop()

    except Exception as e:
        print(f"Error during test: {e}")
