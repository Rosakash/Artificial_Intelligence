from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter import messagebox as mBox
import time
from os import path, makedirs
import tkinter as tk
import speech_recognition  as sr
from playsound import playsound as ps
import re
from threading import Thread
from time import sleep

class pa():
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Spirit Communication")
        self.root.geometry("400x350+0+0")
        self.root.resizable(0, 0)
        
        
        f = Frame(self.root,width=300,height=50,bg="white",relief=SUNKEN)
        f.pack(side=TOP)
        
        scrolW  = 130; scrolH = 50
        self.scr = scrolledtext.ScrolledText(f, width=scrolW, height=scrolH, wrap=WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)
        self.scr.insert(INSERT,"You Said :")
          
        self.r = sr.Recognizer()
        self.b=Button(f,padx=10,pady=10,bd=8,fg="green",font=('arial',20,'bold'),text="Start", bg="powder blue",command=self.create_thread)
        self.b.grid(row=0,column=0)
        
        self.b1=Button(f,padx=10,pady=10,bd=8,fg="green",font=('arial',20,'bold'),text="Stop", bg="powder blue",command=self.create_thread)
        self.b1.grid(row=1,column=0)
        
    def create_thread(self):
        runt = Thread(target=self.play)
        runt.start()
    def play(self):
        ps("Ghost_Track_4.mp3")
        #self.play()


p = pa()
p.root.mainloop()
