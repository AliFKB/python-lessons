import time
from tkinter import *

# date_time = str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec)

# while True:
#     time.sleep(1)
#     print(date_time)

root = Tk()
root.title("Часы")
root.resizable(width = False, height = False)

def tick():
    watch.after(1000, tick)
    watch["text"] = time.strftime("%d %B %Y, %A - %H:%M:%S")

watch = Label(root, font = "Arial 40", bg = "#000", fg = "#008000")
watch.pack()
tick()

root.mainloop()
