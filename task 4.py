import tkinter as tk

def key_pressed(event):
    key = event.keysym

    with open("key_log.txt", "a") as file:
        file.write(key + "\n")

    status.config(text=f"Last key: {key}")

root = tk.Tk()
root.title("Keyboard Event Logger")
root.geometry("400x200")

label = tk.Label(
    root,
    text="Click this window and press keys.\nOnly keys pressed here are logged.",
    font=("Arial", 12)
)
label.pack(pady=20)

status = tk.Label(root, text="Press any key", font=("Arial", 10))
status.pack()

root.bind("<Key>", key_pressed)

root.mainloop()