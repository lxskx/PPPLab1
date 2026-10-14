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

bits = [0, 0, 0, 0, 0, 0, 0, 0]

circles = []
texts = []


def toggle_bit(index):
    bits[index] = 1 - bits[index]

    if bits[index] == 1:
        canvas.itemconfig(
            circles[index],
            fill="black"
        )

        canvas.itemconfig(
            texts[index],
            text="1",
            fill="white"
        )

    else:
        canvas.itemconfig(
            circles[index],
            fill="white"
        )

        canvas.itemconfig(
            texts[index],
            text="0",
            fill="black"
        )


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

    text = canvas.create_text(
        x,
        y,
        text="0",
        font=("Arial", 22)
    )

    circles.append(circle)
    texts.append(text)

    canvas.tag_bind(
        circle,
        "<Button-1>",
        lambda event, i=i: toggle_bit(i)
    )

    canvas.tag_bind(
        text,
        "<Button-1>",
        lambda event, i=i: toggle_bit(i)
    )

root.mainloop()
