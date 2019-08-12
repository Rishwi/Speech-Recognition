# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:08:22 2019

@author: Rishwi Binnu
"""

import speech_recognition as sr
import pyaudio

j=sr.Recognizer()

with sr.Microphone() as source:
  print("Tell me Mr. Rishwi...")
  audio = j.listen(source)

try:
  text = j.recognize_google(audio)
  print("You just said : {}".format(text))
  
except:
  print("apologize me, i couldn't recognize it")