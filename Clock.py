import datetime

seconds=datetime.datetime.now().second
minutes=datetime.datetime.now().minute
hours=datetime.datetime.now().hour

import time
from turtle import *
t1=Turtle()
while True:
  t1.color('red')
  t1.begin_fill()
  t1.clear()
  t1.write(str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2), font=('oxygen', 25, 'normal'))
  seconds=seconds+1
  time.sleep(1)
  if (seconds == 60):
    seconds=0
    minutes+=1
  if (minutes == 60):
    minutes=0
    hours+=1
  if (hours >= 12):
    hours-=12
  t1.end_fill()
