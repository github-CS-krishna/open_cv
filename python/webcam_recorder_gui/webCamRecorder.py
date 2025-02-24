import cv2
from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
from time import time
from random import randint
tk = Tk()

#camera properties
resolution = (800,600)
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,resolution[0])
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,resolution[1])

#video
videowrite = frame = None
#fps variables
previousTime = currentTime = fps = 0
#control variables
drawNewRectangle = False
cameraStatus = True
recordStatus = False
#x and y
x,y = randint(0,680),randint(0,480)

def startRecordVideo():
    global recordStatus,videowrite
    resolution = (int(cam.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    videowrite = cv2.VideoWriter(f'./Record/{datetime.now().strftime("%d-%m-%Y %I_%M_%p")}.avi',cv2.VideoWriter.fourcc(*'XVID'),30,resolution)
    recordStatus = True
    stopRecordButton.configure(state="active")
    

def stopRecordVideo():
    global recordStatus,videowrite
    recordStatus = False
    videowrite.release()
    stopRecordButton.configure(state="disabled")

def closeCamera():
    global cameraStatus
    cameraStatus = False

def drawRectangle():
    global drawNewRectangle
    drawNewRectangle = True
    drawRectangleButton.configure(state="disabled")

def openCamera(cameraStat,recordStat):
    global cam,videowrite,cameraStatus,previousTime
    if(cameraStat): 
        closeCamButton.configure(state="active")
        startRecordButton.configure(state="active")
        
        ret,frame = cam.read()
        #record video
        if(recordStat):
            videowrite.write(frame)
        #calculate FPS
        currentTime = time()
        fps = 1/(currentTime-previousTime)
        previousTime = currentTime
        fps = "FPS " + str(int(fps))
        cv2.putText(frame,fps,(35,40),cv2.FONT_HERSHEY_SIMPLEX,1,(25,116,207),2,cv2.LINE_AA)

        if(drawNewRectangle):
            cv2.rectangle(frame,(x,y), (x+120,y+120), (255,0,0), 3)

        captured = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        photoImage = Image.fromarray(captured)
        img = ImageTk.PhotoImage(photoImage)
        imgLabel.img = img
        imgLabel.configure(image=img)
        tk.after(10,openCamera,cameraStatus,recordStatus)
    else:
        cameraStatus = True
        cam.release()
        setCamOffImage()
        closeCamButton.configure(state="disabled")
        startRecordButton.configure(state="disabled")
        drawRectangleButton.configure(state="disabled")
        cam = cv2.VideoCapture(0)
        cam.set(cv2.CAP_PROP_FRAME_WIDTH,resolution[0])
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT,resolution[1])

def quitApplication():
    tk.quit()

def setCamOffImage():
    camoff = ImageTk.PhotoImage(Image.open("./cameraOff.jpg"))
    imgLabel.image = camoff
    imgLabel.configure(image=camoff)

#label and buttons
imgLabel = Label()

setCamOffImage()
openCamButton = Button(text="Open Camera", command=lambda:openCamera(cameraStatus,recordStatus),state="active",width=12,height=2)
closeCamButton = Button(text="Close Camera", command=closeCamera,state="disabled",width=12,height=2)
drawRectangleButton = Button(text="Draw Rectangle", command=drawRectangle,state="active",width=15,height=2)
startRecordButton = Button(text="Start Record", command=startRecordVideo,state="disabled",width=12,height=2)
stopRecordButton = Button(text="Stop Record", command=stopRecordVideo,state="disabled",width=12,height=2)
closeButton = Button(text="Close", command=quitApplication,state="active",width=10,height=2)

#layout
imgLabel.grid(row=0,column=0,columnspan=6)
openCamButton.grid(row=1,column=0)
closeCamButton.grid(row=1,column=1)
drawRectangleButton.grid(row=1,column=2)
startRecordButton.grid(row=1,column=3)
stopRecordButton.grid(row=1,column=4)
closeButton.grid(row=1,column=5)

tk.mainloop()