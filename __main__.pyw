import tkinter as tk
from tkinter import ttk
import tkinterDnD
from PIL import Image,ImageTk

parameter = {}

timea = []
framenbr = 0
root = tkinterDnD.Tk()  
root.title("Entity Animation exporter")

stringvar = tk.StringVar()
stringvar.set('Drop your animation texture here !')
img = Image.open('0.png')

def drop(event):
    global img
    stringvar.set(event.data)
    if event.data[0] == '{':
        img = Image.open(event.data[1:-1])
    else:
        img = Image.open(event.data)
    
def drag_command(event):
    return (tkinterDnD.COPY, "DND_Text", "Some nice dropped text!")



    return None



def saveImage():
    
    img2 = img.convert('RGBA')
    
    pixelcolor = img2.getpixel((0,0))
    img2.putpixel((0,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],245))
    pixelcolor = img2.getpixel((1,0))
    img2.putpixel((1,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],int(parameter['sizex'])))
    pixelcolor = img2.getpixel((2,0))
    img2.putpixel((2,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],int(parameter['timeMultiply'])))
    pixelcolor = img2.getpixel((3,0))
    img2.putpixel((3,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],int(parameter['desync'])))
    if parameter['isManully'] == 1:
        pixelcolor = img2.getpixel((4,0))
        img2.putpixel((4,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],int(parameter['frameNumber'])))
    else:
        sommeTime = 0
        for i in timea:
            sommeTime += int(i)
        
        img2.putpixel((4,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],(sommeTime)))
    pixelcolor = img2.getpixel((5,0))
    img2.putpixel((5,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],int(parameter['sizey'])))
    if parameter['asDamage'] == 1:
        pixelcolor = img2.getpixel((6,0))
        img2.putpixel((6,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],int(parameter['asDamageColumn'])))
    else:
        img2.putpixel((6,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],0))
    if parameter['asDistanceVar'] == 1:
        pixelcolor = img2.getpixel((7,0))
        img2.putpixel((7,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],int(parameter['asDistanceColumn'])))
        pixelcolor = img2.getpixel((8,0))
        img2.putpixel((8,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],int(parameter['asDistanceBlock'])))
    else:
        pixelcolor = img2.getpixel((7,0))
        img2.putpixel((7,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],0))
        pixelcolor = img2.getpixel((8,0))
        img2.putpixel((8,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],0))
    if parameter['asSleepingVar'] == 1:
        pixelcolor = img2.getpixel((9,0))
        img2.putpixel((9,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],int(parameter['asSleepingColumn'])))
    else:
        pixelcolor = img2.getpixel((9,0))
        img2.putpixel((9,0),(pixelcolor[0],pixelcolor[1],pixelcolor[2],0))
        
    for i,j in enumerate(timea):
        coord = (int(i)%int(parameter['sizey']),1+(int(int(i)/int(parameter['sizey']))))
        pixelcolor = img2.getpixel(coord)
        img2.putpixel((coord),(pixelcolor[0],pixelcolor[1],pixelcolor[2],int(j)))
        print(i,j)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    img2.save('2.png')
    return img2.getpixel((0,0))
    
def newWindow():
    def newWindowReturn():
        global parameter
        parameter['sizex'] = sizex.get()
        parameter['sizey'] = sizey.get()
        parameter['timeMultiply'] = timeMultiply.get()
        if timeMultiply.get() != '':
            parameter['timeMultiply'] = parameter['timeMultiply']
        else:
            parameter['timeMultiply'] = '1.0';
        
        parameter['desync'] = desyncVar.get()
        parameter['isManully'] = isManullyVar.get()
        parameter['frameNumber'] = frameNumber.get()
        parameter['asDamage'] = asDamageVar.get()
        parameter['asDamageColumn'] = asDamageColumn.get()
        parameter['asDistanceVar'] = asDistanceVar.get()
        parameter['asDistanceColumn'] = asDistanceColumn.get()
        parameter['asDistanceBlock'] = asDistanceBlock.get()
        parameter['asSleepingVar'] = asSleepingVar.get()
        parameter['asSleepingColumn'] = asSleepingColumn.get()
        newwindow.destroy()
        
        
        
        print(parameter)

    newwindow = tk.Toplevel(root)
    newwindow.title("Parameter")
    label_1 = tk.Label(newwindow, text='Y size of a single frame (beetween 0 and 255)')
    label_1.pack()
    sizex = ttk.Entry(newwindow)
    sizex.pack()
    label_2 = tk.Label(newwindow, text='X size of a single frame (beetween 0 and 255)')
    label_2.pack()
    sizey = tk.Entry(newwindow)
    sizey.pack()
    label_3 = tk.Label(newwindow, text='time multiplicator, the animation lenght for 1 frame is 1 seconde / this value (1 by default)')
    label_3.pack()
    timeMultiply = tk.Entry(newwindow)
    timeMultiply.pack()
    label_4 = tk.Label(newwindow, text='disable syncronisation of the animatio beetween enntity base on position, but this isn\'t working great')
    label_4.pack()
    desyncVar = tk.IntVar()
    desync = tk.Checkbutton(newwindow,variable = desyncVar)
    desync.pack()
    label_5 = tk.Label(newwindow, text='if you check you have to register manually the number of frame the animation as (frame isn\'t the frame number but it is the addition of every frametime)')
    label_5.pack()
    isManullyVar = tk.IntVar()
    isManully = tk.Checkbutton(newwindow,variable = isManullyVar)
    isManully.pack()
    frameNumber = tk.Entry(newwindow)
    frameNumber.pack()
    label_5 = tk.Label(newwindow, text='as a damage animation, if check register the column number of the animation for this')
    label_5.pack()
    asDamageVar = tk.IntVar()
    asDamage = tk.Checkbutton(newwindow,variable = asDamageVar)
    asDamage.pack()
    asDamageColumn = tk.Entry(newwindow)
    asDamageColumn.pack()
    label_5 = tk.Label(newwindow, text='as a distance animation, if check register the column number of the animation for this and the amount of block distance when the animation is play')
    label_5.pack()
    asDistanceVar = tk.IntVar()
    asDistance = tk.Checkbutton(newwindow, variable=asDistanceVar)
    asDistance.pack()
    asDistanceColumn = tk.Entry(newwindow)
    asDistanceColumn.pack()
    asDistanceBlock = tk.Entry(newwindow)
    asDistanceBlock.pack()
    label_5 = tk.Label(newwindow, text='as a sleeping animation, if check register the column number of the animation for this (sleeping animation just change the upper face with the texture register)')
    label_5.pack()
    asSleepingVar = tk.IntVar()
    asSleeping = tk.Checkbutton(newwindow, variable = asSleepingVar)
    asSleeping.pack()
    asSleepingColumn = tk.Entry(newwindow)
    asSleepingColumn.pack()
    done = tk.Button(newwindow,text='done',command=newWindowReturn)
    done.pack()
    

def animTime():
    global timea,framenbr
    
    
    
    def nextf():
        ''''''
        global framenbr, timea
        if framenbr <=  int(img.size[1]/int(parameter['sizex']))-1:
            timea =timea + [timeEntry.get()]
            framenbr = framenbr+1
            label_1 = tk.Label(animTime, text='enter time in second (this time will be divide by timemultiply in parameter) frame'+str(framenbr)+'/'+str(int(img.size[1]/int(parameter['sizex']))))
            label_1.pack()
            print(timea,framenbr)
        else:
            animTime.destroy()
        
    animTime = tk.Toplevel(root)
    animTime.title("Parameter")
    if not 'sizex' in parameter.keys():
        
        label_1 = tk.Label(animTime, text='please enter anim parameter before')
        label_1.pack()
        
    
    else:
        if parameter['sizex'] != '':
            label_1 = tk.Label(animTime, text='enter time in second (this time will be divide by timemultiply in parameter) frame'+str(framenbr)+'/'+str(int(img.size[1]/int(parameter['sizex']))))
            label_1.pack()
            timeEntry = tk.Entry(animTime)
            timeEntry.pack()
            AnimBt = tk.Button(animTime,text='next',command=nextf)
            AnimBt.pack()
        else:
            label_1 = tk.Label(animTime, text='please enter anim parameter before')
            label_1.pack()
    
    
    
    
    
    
label_1 = tk.Label(root, textvar=stringvar, relief="solid")
label_1.pack(fill="both", expand=True, padx=10, pady=10)

label_1.register_drop_target("*")
label_1.bind("<<Drop>>", drop)

label_1.register_drag_source("*")
label_1.bind("<<DragInitCmd>>", drag_command)


label_2 = ttk.Label(root, ondrop=drop, ondragstart=drag_command,
                    textvar=stringvar, padding=50, relief="solid")
label_2.pack(fill="both", expand=True, padx=10, pady=10)

parametreBt = tk.Button(root,text='Animation Parametre',command=newWindow)
parametreBt.pack()
AnimBt = tk.Button(root,text='Animation Time',command=animTime)
AnimBt.pack()
AnimBt = tk.Button(root,text='Save',command=saveImage)
AnimBt.pack()
root.mainloop()
