import cv2
from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
tk = Tk()
#camera properties
resolution = (800,600)
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,resolution[0])
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,resolution[1])

#video
videowrite = None

#control variables
cameraStatus = True
recordStatus = False

def startRecordVideo():
    global recordStatus,videowrite
    resolution = (int(cam.get(3)),int(cam.get(4)))
    videowrite = cv2.VideoWriter(f'./Record/{datetime.now().strftime("%d-%m-%Y %I_%M_%p")}.avi',cv2.VideoWriter.fourcc(*'XVID'),24,resolution)
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

def openCamera(cameraStat,recordStat):
    global cam,videowrite,cameraStatus
    if(cameraStat): 
        closeCamButton.configure(state="active")
        startRecordButton.configure(state="active")
        
        ret,frame = cam.read()
        if(recordStat):
            videowrite.write(frame)

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
openCamButton = Button(text="Open Camera", command=lambda:openCamera(cameraStatus,recordStatus),state="active",width=15,height=2)
closeCamButton = Button(text="Close Camera", command=closeCamera,state="disabled",width=15,height=2)
startRecordButton = Button(text="Start Record", command=startRecordVideo,state="disabled",width=15,height=2)
stopRecordButton = Button(text="Stop Record", command=stopRecordVideo,state="disabled",width=15,height=2)
closeButton = Button(text="Close", command=quitApplication,state="active",width=12,height=2)

#layout
imgLabel.grid(row=0,column=0,columnspan=5)
openCamButton.grid(row=1,column=0)
closeCamButton.grid(row=1,column=1)
startRecordButton.grid(row=1,column=2)
stopRecordButton.grid(row=1,column=3)
closeButton.grid(row=1,column=4)

tk.mainloop()
