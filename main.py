from tkinter import *
import pathlib
from pytube import YouTube
from tkinter import messagebox, filedialog


root = Tk()
root.geometry("500*110")
root.resizable(0, 0)
root.title("Youtube Video Downloader")
root.config(background="#000000")

video_Link = StringVar()
download_Path = StringVar()

Widget()
root.mainloop()



def Widgets():
    link_label = Label(root, text="YouTube link :")