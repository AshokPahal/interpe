import tkinter as tk
from time import strftime

def time():
    # Get the current time in the desired format
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    # Update the clock every 1 second
    label.after(1000, time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label for displaying the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

# Call the time function to start the clock
time()

# Run the application's main event loop
root.mainloop()