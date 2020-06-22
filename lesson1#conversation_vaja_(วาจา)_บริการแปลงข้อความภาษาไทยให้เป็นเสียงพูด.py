# -*- coding: utf-8 -*-
"""Lesson1# CONVERSATION  Vaja (วาจา) บริการแปลงข้อความภาษาไทยให้เป็นเสียงพูด.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qS9pqmHFyvygqFY7j-1JP0rXExtfG-Bq
"""

import requests

Apikey='t5xX0LLizRkhF63izmJ7YUc6AiQHhs17'
url = 'https://api.aiforthai.in.th/vaja'
headers = {'Apikey':Apikey,'Content-Type' : 'application/x-www-form-urlencoded'}
text = 'ทดสอบพูด'
 
data = {'text':text,'mode':'st'}
 
# sending post request and saving response as response object
response = requests.get(url, params=data, headers=headers)
 
print(response.json())

result = response.json()['output']['audio']['result']
numChannels =response.json()['output']['audio']['numChannels']
validBits = response.json()['output']['audio']['validBits']
sizeSample=response.json()['output']['audio']['sizeSample']
sampleRate=response.json()['output']['audio']['sampleRate']
len(result), numChannels, validBits, sizeSample,sampleRate

# นำค่า result มาไลทเป็นไฟล์ wav
import wave, struct
 
obj = wave.open('sound.wav','wb') #ตั้งชื่อ
obj.setparams((1, int(validBits/8), sampleRate, 0, 'NONE', 'not compressed')) #1 คือ โมโน channel
for i in range(sizeSample):
  value = int(result[i])
  data = struct.pack('<h', value)  
  obj.writeframesraw(data)
obj.close() #ไลทเป็นไฟล์ wav

from IPython.display import Audio #เปิดไฟล์เสียง
Audio('/content/sound.wav')

