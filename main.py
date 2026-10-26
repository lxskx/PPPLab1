import tkinter as tk


root = tk.Tk()
root.title("Двоичные числа")
root.geometry("800x350")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=800,
    height=350,
    bg="white",
    highlightthickness=0
)
canvas.pack()

root.mainloop()
