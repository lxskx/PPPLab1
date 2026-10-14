import tkinter as tk

root = tk.Tk()
root.title("Двоичные числа")
root.geometry("800x350")

canvas = tk.Canvas(
    root,
    width=800,
    height=350,
    bg="white"
)

canvas.pack()

root.mainloop()
