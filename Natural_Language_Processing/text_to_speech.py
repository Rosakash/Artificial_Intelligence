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

class pa():
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Speech")
        self.root.geometry("400x350+0+0")
        self.root.resizable(0, 0)
        
        
        f = Frame(self.root,width=800,height=50,bg="white",relief=SUNKEN)
        f.pack(side=TOP)
        
        scrolW  = 130; scrolH = 50
        self.scr = scrolledtext.ScrolledText(f, width=scrolW, height=scrolH, wrap=WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)
        self.scr.insert(INSERT,"You Said :")
          
        self.r = sr.Recognizer()
        self.b=Button(f,padx=10,pady=10,bd=8,fg="green",font=('arial',20,'bold'),text="Say", bg="powder blue",command=self.Fuction)
        self.b.grid(row=0,column=0)
        
    def play(self):
        if 'name' in self.c[3]:
            print("\n My name is Annie")
            self.scr.insert(INSERT,"\n My name is Annie")
        if 'you'  in self.c[2]:
            print("I am Annie")
    def Fuction(self):
    
    
        with sr.Microphone() as source:
              print("Say Something Akash")
              text= self.r.listen (source)
        
        try:
            print("You Said :"+ self.r.recognize_google(text))
            self.scr.insert(INSERT,self.r.recognize_google(text))
            cmd = self.r.recognize_google(text)
            #c = (cmd+"()")
            #print(c)
            self.c = cmd.split(" ")
            for x in self.c:
                i = (x+".wav")
                ps(i)
            
        except:
            pass

p = pa()
p.root.mainloop()
