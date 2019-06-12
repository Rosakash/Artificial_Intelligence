from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter import messagebox as mBox
import time
import cv2
import numpy as np
from PIL import Image
import pickle
from os import path, makedirs
import tkinter as tk
import speech_recognition as sr
from playsound import playsound as ps
import re
import requests
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write



class listen():
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
        self.b=Button(f,padx=10,pady=10,bd=8,fg="green",font=('arial',20,'bold'),text="Say", bg="powder blue",command=self.mic)
        self.b.grid(row=0,column=0)
    def mic(self):
        with sr.Microphone() as source:
            print("Say Something Akash")
            text= self.r.listen (source)
            print(type(text))
            sampling_freq, signal = wavfile.read(text)
            write(file_tone_sequence, sampling_freq, signal)
            print('\nSignal shape:', signal.shape)
            print('Datatype:', signal.dtype)
            print('Signal duration:', round(signal.shape[0] / float(sampling_freq), 2),'seconds')
            signal = signal / np.power(2, 15)
            signal = signal[:50]
            time_axis = 1000 * np.arange(0, len(signal), 1) / float(sampling_freq)
            plt.plot(time_axis, signal, color='black')
            plt.xlabel('Time (milliseconds)')
            plt.ylabel ( 'Amplitude ' )
            plt.title('Input audio signal')
            plt.show()
            #self.mic()
            #sleep(5)
p = listen()
p.root.mainloop()