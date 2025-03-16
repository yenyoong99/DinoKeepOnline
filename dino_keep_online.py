import tkinter as tk
import pyautogui
import threading
import random
import time

def run_dino_animation():
    def move_dino():
        nonlocal dino_x
        if not keep_running:
            return
        canvas.delete("dino")
        canvas.create_rectangle(dino_x, 60, dino_x + 40, 100, fill="#4caf50", tags="dino")
        canvas.create_oval(dino_x + 10, 100, dino_x + 30, 120, fill="#8bc34a", tags="dino")

        dino_x = (dino_x + 5) % 200
        root.after(100, move_dino)

    dino_x = 10
    move_dino()

def keep_online():
    while keep_running:
        action = random.choice(["mouse", "keyboard"])
        if action == "mouse":
            x, y = pyautogui.position()
            pyautogui.moveTo(x + random.randint(-10, 10), y + random.randint(-10, 10), duration=0.2)
        elif action == "keyboard":
            pyautogui.press("shift")
        time.sleep(random.randint(5, 15))

def start_mofish():
    global keep_running
    keep_running = True
    threading.Thread(target=keep_online, daemon=True).start()
    status_label.config(text="Mo Fish... Keep Online...", font=("Arial", 10, "bold"))
    start_button.pack_forget()
    stop_button.pack(pady=20)
    run_dino_animation()

def stop_mofish():
    global keep_running
    keep_running = False
    status_label.config(text="Mo Fish Stopped.", font=("Arial", 10, "bold"))
    stop_button.pack_forget()
    start_button.pack(pady=20)

root = tk.Tk()
root.title("Dino Keep Online v1.0")
root.geometry("500x500+{}+{}".format(root.winfo_screenwidth() // 2 - 250, root.winfo_screenheight() // 2 - 250))
root.configure(bg="#2c2f33")
root.attributes("-alpha", 0.9)
root.attributes("-topmost", True)
root.overrideredirect(True)

title_bar = tk.Frame(root, bg="#23272a", relief="raised", bd=0)
title_bar.pack(fill=tk.X, side=tk.TOP)

title_label = tk.Label(title_bar, text="Dino Keep Online v1.0", bg="#23272a", fg="#ffffff", font=("Arial", 12, "bold"))
title_label.pack(side=tk.LEFT, padx=10)

close_button = tk.Button(title_bar, text="X", bg="#f44336", fg="#ffffff", font=("Arial", 10, "bold"), bd=0, command=root.destroy)
close_button.pack(side=tk.RIGHT, padx=5)

def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def on_move(event):
    x = root.winfo_x() + (event.x - root.x)
    y = root.winfo_y() + (event.y - root.y)
    root.geometry(f"500x500+{x}+{y}")

title_bar.bind("<Button-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", on_move)

status_label = tk.Label(root, text="Click START to keep online", font=("Arial", 12, "bold"), fg="#ffffff", bg="#2c2f33")
status_label.pack(pady=20)

canvas = tk.Canvas(root, width=300, height=200, bg="#23272a", highlightthickness=0)
canvas.pack(pady=10)

start_button = tk.Button(root, text="START", font=("Arial", 12, "bold"), bg="#4caf50", fg="#ffffff", command=start_mofish, width=12, height=2, bd=0, activebackground="#45a049")
start_button.pack(pady=20)

stop_button = tk.Button(root, text="STOP", font=("Arial", 12, "bold"), bg="#f44336", fg="#ffffff", command=stop_mofish, width=12, height=2, bd=0, activebackground="#e53935")

author_label = tk.Label(root, text="Program by YY - 2025", font=("Arial", 10), fg="#b0bec5", bg="#2c2f33")
author_label.pack(side="bottom", pady=10)

keep_running = False

root.mainloop()
