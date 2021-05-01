import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text = "Hello, User!")
greeting.pack()

label = tk.Label(text = "Welcome to Netflix Titles!", foreground = "light green", background = "black", width = 20, height = 20)
label.pack()

button = tk.Button (text = "Log In Here!", width = 20, height = 5, bg = "black", fg = "light green")
button.pack()

#entry = tk.Entry(fg="light green", bg="black", width=50)
#entry.pack()


window.mainloop()
