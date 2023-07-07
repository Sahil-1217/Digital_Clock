import tkinter as tk
import time


def update_clock():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_clock)


# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Create a label for displaying the time
label = tk.Label(window, font=('Arial', 80), bg='black', fg='white')
label.pack(padx=50, pady=50)

# Update the clock initially and start the update loop
update_clock()

# Start the GUI event loop
window.mainloop()
