from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter import messagebox as mBox
import time
from os import path, makedirs
import tkinter as tk
import speech_recognition as sr
from playsound import playsound as ps
import re
import requests
#ps('myy favo.mp3')
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
        print("I am in.")
        # Make sure data is in array.
        #Check status.
        if 'scan' == self.c[0].lower():
            self.host = self.c[1].lower()
            h= ('http://www.'+self.host+".com")
            r=requests.get(h)
            print(h)
            print('\nStatus Code: ',str(r.status_code))
            self.scr.insert(INSERT,'\nHost is alive.\n')
            self.scr.insert(INSERT,h)
            self.scr.insert(INSERT,"\n")
            self.scr.insert(INSERT,str(r.status_code))
            p = (str(r.status_code)+".wav")
            print(p)
            ps(p)
            
        if 'source' == self.c[1].lower():
            self.host = self.c[0].lower()
            h= ('http://www.'+self.host+".com")
            r=requests.get(h)
            print(r.text)
            print(str(r.status_code))
            self.scr.insert(INSERT,'\n Page Source: \n',str(r.text))
            ps('igotit.wav')
            self.Information()
            #self.Fuction()
            #if 'email' in self.c[1]:
               # print("I am in Email.")
        if 'extract' == self.c[0].lower():
            if 'email' or 'emails' == self.c[1].lower():
                if 'from' == self.c[2].lower():
                    print(self.c[3].lower())
                    self.host = self.c[3].lower()
                    h= ('http://www.'+self.host+".com")
                    r=requests.get(h)                    
                    r=re.findall(r'@\w+.\w+',str(r.text))
                    for line in r:
                        print(line)
                        self.scr.insert(INSERT,line)
                    print("These are emails.")       
        else:
            print("No sufficient data available")
    def Fuction(self):
    
    
        with sr.Microphone() as source:
              print("Say Something Akash")
              text= self.r.listen (source)
        
        try:
            print("You Said :"+ self.r.recognize_google(text))
            self.scr.insert(INSERT,self.r.recognize_google(text))
            self.cmd = self.r.recognize_google(text)
            #c = (cmd+"()")
            print(type(self.cmd))
            self.c = self.cmd.split(" ")
            #self.c = (self.c.lower())
            print(self.c)
            self.play()
        except:
            pass
    def Information(self):
    
    
        with sr.Microphone() as source:
            print("Say Something Akash")
            text= self.r.listen (source)
        
        try:
            print("Akash Said :"+ self.r.recognize_google(text))
            self.scr.insert(INSERT,self.r.recognize_google(text))
            self.msg = self.r.recognize_google(text)
        except:
            pass
            self.play()

p = pa()
p.root.mainloop()
