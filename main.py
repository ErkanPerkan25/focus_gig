import time as tm
import tkinter as tk
from tkinter import messagebox

alarm_file = "jarvis_alarm.mp3"


def startTimer():
    try:
        time = int(time_min.get())*60 + int(time_sec.get())
    except time:
        print("Enter a correct number!")
    while time > -1:
        minutes, seconds = divmod(time, 60)
        time_min.set("{0:2d}".format(minutes))
        time_sec.set("{0:2d}".format(seconds))
        root.update()
        tm.sleep(1)

        if (time == 0):
            messagebox.showinfo("Timer Notification", "Times up!")

        time -= 1


root = tk.Tk()
root.title("Timer App")
root.geometry("400x300")

setTime_label = tk.Label(root, text="Set timer:")
setTime_label.pack(pady=5, anchor=tk.N)

frame = tk.Frame(root)
frame.pack(expand=True)

time_min = tk.StringVar()
time_sec = tk.StringVar()

time_min.set("0")
time_sec.set("0")

entry_min = tk.Entry(frame, width=2, textvariable=time_min)
entry_sec = tk.Entry(frame, width=2, textvariable=time_sec)
entry_min.pack(side=tk.LEFT, padx=3)
entry_sec.pack(side=tk.LEFT, padx=3)

submit_btn = tk.Button(
    root,
    text="Start timer",
    pady=5,
    command=startTimer
)

button = tk.Button(root, text="Exit", width=10, command=root.destroy)
submit_btn.pack(pady=5)
button.pack(pady=5)

root.mainloop()
