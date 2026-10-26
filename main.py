import tkinter as tk


root = tk.Tk()
root.title("Двоичные числа")
root.geometry("800x350")
root.resizable(False, False)
root.configure(bg="white")

canvas = tk.Canvas(
    root,
    width=800,
    height=180,
    bg="white",
    highlightthickness=0
)
canvas.pack()

bits = [0] * 8
circles = []
texts = []

result_label = tk.Label(
    root,
    text="0",
    font=("Arial", 64, "bold"),
    fg="black",
    bg="white"
)
result_label.pack(pady=20)


def update_number():
    """Calculate and display the decimal value."""
    value = 0

    for bit in bits:
        value = value * 2 + bit

    result_label.config(text=str(value))


def toggle_bit(index):
    """Switch the selected binary register."""
    bits[index] = 1 - bits[index]

    if bits[index] == 1:
        canvas.itemconfig(circles[index], fill="black")
        canvas.itemconfig(texts[index], text="1", fill="white")
    else:
        canvas.itemconfig(circles[index], fill="white")
        canvas.itemconfig(texts[index], text="0", fill="black")

    update_number()


for i in range(8):
    x = 85 + i * 90
    y = 90
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
        fill="black",
        font=("Arial", 22, "bold")
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
