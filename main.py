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

circles = []

for i in range(8):
    x = 85 + i * 90
    y = 100
    radius = 32

    circle = canvas.create_oval(
        x - radius,
        y - radius,
        x + radius,
        y + radius,
        fill="white",
        outline="black",
        width=3
    )

    circles.append(circle)

root.mainloop()
