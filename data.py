#Create folder named drunk and sober . Store the vidoes in their folders respectively
#Create output folder named dataset
#Import the libraries imported below 
#

from moviepy.editor import VideoFileClip
import os
import math
import numpy as np
from random import randint

drunk=os.listdir('./5sec/Drunk')
sober=os.listdir('./5sec/Sober')
'''
num=[]
for i in range(1,41):
    num.append(i)
rand=[]
for i in range(1,41):
    n=randint(0,len(num)-1)
    rand.append(num[n])
    del num[n]

#For videos of 10 seconds
#name of videos 
name='./dataset/video10_'
file = open("./dataset/drunk.txt","w")

for i in range(20):
    filename=name+str(rand[i])+'.mp4'
    filepath='./drunk/'+drunk[i]
    clip=VideoFileClip(filepath).subclip(0,10)
    clip.write_videofile(filename)
    clip.close()
    file.write(str(filename))
for i in range(20):
    filename=name+str(rand[i+20])+'.mp4'
    filepath='./sober/'+sober[i]
    clip=VideoFileClip(filepath).subclip(0,10)
    clip.write_videofile(filename)
    clip.close()
'''

#For videos of 15 seconds
#name of videos	
for i in range(len(drunk)):
	filename=drunk[i]
	filepath='./5sec/Drunk/'+drunk[i]
	filesavepath='./5seg/Drunk/'+drunk[i]
	clip=VideoFileClip(filepath)
	dur=clip.duration
	clip.close()
	cn=1
	for j in range(0,int(dur-5),5):
		clip=VideoFileClip(filepath).subclip(j,j+5)
		filename1=filesavepath+"_"+str(cn)+".mp4"
		clip.write_videofile(filename1)
		clip.close()
		cn=cn+1
#    file.write(str(filename))

for i in range(len(sober)):
	filename=sober[i]
	filepath='./5sec/Sober/'+sober[i]
	filesavepath='./5seg/Sober/'+sober[i]
	clip=VideoFileClip(filepath)
	dur=clip.duration
	clip.close()
	cn=1
	for j in range(0,int(dur-5),5):
		clip=VideoFileClip(filepath).subclip(j,j+5)
		filename1=filesavepath+"_"+str(cn)+".mp4"
		clip.write_videofile(filename1)
		clip.close()
		cn=cn+1

'''
#For videos of 20 seconds
#name of videos
name='./dataset/video20_'
for i in range(20):
    filename=name+str(rand[i])+'.mp4'
    filepath='./drunk/'+drunk[i]
    clip=VideoFileClip(filepath).subclip(0,20)
    clip.write_videofile(filename)
    clip.close()
    file.write(str(filename))

for i in range(20):
    filename=name+str(rand[i+20])+'.mp4'
    filepath='./sober/'+sober[i]
    clip=VideoFileClip(filepath).subclip(0,20)
    clip.write_videofile(filename)
    clip.close()
file.close()
'''
