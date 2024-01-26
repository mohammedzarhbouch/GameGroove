import tkinter as tk
import random
import time


def onSelectionButtonClick2(selectionWindow):
    selectionWindow.destroy()
    startAimTrainer()

def startAimTrainer():

    MAX_CLICKS = 30
    start_time = None
    elapsed_time = 0  # Define elapsed_time as a global variable

    def move_button_to_center():
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        center_x = canvas_width // 2
        center_y = canvas_height // 2

        canvas.coords(button_circle, center_x - button_radius, center_y - button_radius,
                    center_x + button_radius, center_y + button_radius)

    def move_button():
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        # Limit the random coordinates to keep the button within the canvas
        new_x = random.randint(button_radius, canvas_width - button_radius * 2)
        new_y = random.randint(button_radius, canvas_height - button_radius * 2)

        canvas.coords(button_circle, new_x, new_y, new_x + button_radius * 2, new_y + button_radius * 2)

    def on_circle_click(event):
        if countdown.get() > 0 or click_count.get() >= MAX_CLICKS:
            return
        move_button()
        update_click_count()
        update_timer()

    def update_click_count():
        click_count.set(click_count.get() + 1)
        label_count.config(text=f"Click Count: {click_count.get()}")
        if click_count.get() >= MAX_CLICKS:
            update_scoreboard()

    def update_timer():
        global start_time, elapsed_time
        if start_time is None:
            start_time = time.time()
        elapsed_time = time.time() - start_time
        label_timer.config(text=f"Time: {elapsed_time:.2f} seconds")

    def update_scoreboard():
        scoreboard.insert(tk.END, f"Reached {MAX_CLICKS} clicks - Time: {elapsed_time:.2f} seconds")

    def reset_game():
        global start_time, elapsed_time
        start_time = None
        elapsed_time = 0
        click_count.set(0)
        label_count.config(text="Click Count: 0")
        label_timer.config(text="Time: 0.00 seconds")
        move_button_to_center()
        start_countdown()

    def start_countdown():
        countdown.set(3)
        countdown_label()

    def countdown_label():
        if countdown.get() > 0:
            label_timer.config(text=f"Countdown: {countdown.get()}")
            window.after(1000, countdown_label)
            countdown.set(countdown.get() - 1)
        else:
            label_timer.config(text="Time: 0.00 seconds") 

    button_radius = 20

    window = tk.Tk()
    window.title("Aim Trainer")
    window.geometry("730x550")
    window.configure(bg='darkviolet')

    canvas = tk.Canvas(window, width=500, height=400, bg='white', highlightthickness=0)
    canvas.pack(side=tk.LEFT, padx=10, pady=10)

    button_circle = canvas.create_oval(0, 0, button_radius * 2, button_radius * 2, fill='black')
    canvas.tag_bind(button_circle, '<Button-1>', on_circle_click)

    click_count = tk.IntVar()
    click_count.set(0)

    countdown = tk.IntVar()
    countdown.set(0)

    label_count = tk.Label(window, text="Click Count: 0", font=('Helvetica', 14), bg='slateblue')
    label_count.pack()

    label_timer = tk.Label(window, text="Time: 0.00 seconds", font=('Helvetica', 14), bg='slateblue')
    label_timer.pack()

    button_reset = tk.Button(window, text="Reset", command=reset_game, font=('Helvetica', 12))
    button_reset.pack(pady=10)

    scoreboard = tk.Listbox(window, font=('Helvetica', 12), bg='slateblue', selectbackground='darkviolet', selectmode=tk.BROWSE)
    scoreboard.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    start_time = None

    window.mainloop()

