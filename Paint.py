from pygame import * 
from tkinter import *
from math import*
from random import*

root=Tk()#Tkinter
root.withdraw() #hiding the extra window
####Assigning names to colours 
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(1,120,210,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
AQUA=(0,255,255)
size=(1200,750)#size of window
screen = display.set_mode(size)
init()#initializing 
#font.init()#initializing fonts
mixer.pre_init(44100,16,2,4096)#initializing music
mx,my=mouse.get_pos()#mouse position
mb=mouse.get_pressed()#mouse gets pressed
####different tools
tool="no tool"
ftool="stamp"
stool="S"
gtool="G"
omx,omy=300,300#a variable for position
####lists for redo and undo tool
undo=[]
redo=[]
####variables
rad=5
mm=0
f=1
m=0
n=0
e=1
col=BLACK

#####Loading and Playing background music
mixer.music.load("song.mp3")
mixer.music.set_volume(1)
######load ALL pictures
wheelPic=image.load("images/rwheel.png")
groundPic=image.load("images/cricketground.png")                    
pencilPic=image.load("images/pencil.png")
shapePic1=image.load("images/r.png")
eraserPic=image.load("images/eraser.png")
savePic=image.load("images/save.gif")
clearPic=image.load("images/clear.png")
openPic=image.load("images/open.png")
undoPic=image.load("images/undo.png")
redoPic=image.load("images/redo.png")
fellipsePic=image.load("images/fellipse.png")
sprayPic=image.load("images/spray.png")
rectPic=image.load("images/rectangle.png")
urectPic=image.load("images/urectangle.png")
uellipsePic=image.load("images/uellipse.png")
markerPic=image.load("images/marker.png")
bucketPic=image.load("images/bucket.png")
linePic=image.load("images/line.png")
lPic=image.load("images/larrow.png")
rPic=image.load("images/rarrow.png")
playPic=image.load("images/play.png")
pausePic=image.load("images/pause.png")
pickerPic=image.load("images/picker.png")
tbrushPic=image.load("images/tbrush.png")
purplePic=image.load("images/purple.png")
whitePic=image.load("images/whitePic.png")
brushPic=image.load("images/brush.png")
musicPic=image.load("images/music.png")
####Resizing pictures
musicPic=transform.scale(musicPic,(160,50))
lPic=transform.scale(lPic,(20,170))
rPic=transform.scale(rPic,(20,170))
blPic=transform.scale(lPic,(50,100))
brPic=transform.scale(rPic,(50,100))
whitePic=transform.scale(whitePic,(160,20))
purplePic1=transform.scale(purplePic,(220,80))
#####Loading stamps
stamp1Pic=image.load("images/stamp1.png")
stamp2Pic=image.load("images/stamp2.png")
stamp3Pic=image.load("images/stamp3.png")
stamp4Pic=image.load("images/stamp4.png")
stamp5Pic=image.load("images/stamp5.png")
stamp6Pic=image.load("images/stamp6.png")
stamp7Pic=image.load("images/stamp7.png")
stamp8Pic=image.load("images/stamp8.png")
#####Resizing the stamps
stamp1Pic=transform.scale(stamp1Pic,(80,80))
stamp2Pic=transform.scale(stamp2Pic,(80,80))
stamp3Pic=transform.scale(stamp3Pic,(80,80))
stamp4Pic=transform.scale(stamp4Pic,(80,80))
stamp5Pic=transform.scale(stamp5Pic,(80,80))
stamp6Pic=transform.scale(stamp6Pic,(80,80))
stamp7Pic=transform.scale(stamp7Pic,(80,80))
stamp8Pic=transform.scale(stamp8Pic,(80,80))
#making a list of stamps
slist=[stamp1Pic,stamp2Pic,stamp3Pic,stamp4Pic,stamp5Pic,stamp6Pic,stamp7Pic,stamp8Pic]
x=0#a variable for position in list

####Loading Backgrounds
back1Pic=image.load("images/b1.png")
back2Pic=image.load("images/b2.png")
back3Pic=image.load("images/b3.png")
back4Pic=image.load("images/b4.png")
back5Pic=image.load("images/b5.png")
back6Pic=image.load("images/b6.png")
#####Resizing
back1=transform.scale(back1Pic,(200,100))
back2=transform.scale(back2Pic,(200,100))
back3=transform.scale(back3Pic,(200,100))
back4=transform.scale(back4Pic,(200,100))
back5=transform.scale(back5Pic,(200,100))
back6=transform.scale(back6Pic,(200,100))
blist=[back1,back2,back3,back4,back5,back6]
Blist=[back1Pic,back2Pic,back3Pic,back4Pic,back5Pic,back6Pic]
a=0#variable for list positions
##############################defining all RECTS
sizeRect=Rect(0,0,1200,750)
groundRect=Rect(0,0,1200,750)
canvasRect=Rect(170,80,800,550)
wheelRect=Rect(980,100,200,200)
openRect=Rect(20,50,60,60)
saveRect=Rect(90,50,60,60)
undoRect=Rect(20,10,60,30)
redoRect=Rect(90,10,60,30)
pencilRect=Rect(20,120,60,60)
eraserRect=Rect(90,120,60,60)
clearRect=Rect(20,185,60,60)
lineRect=Rect(90,185,60,60)
shapeRect1=Rect(20,250,60,60)
shapeRect2=Rect(90,250,60,60)
shapeRect3=Rect(20,315,60,60)
shapeRect4=Rect(90,315,60,60)
shapeRect5=Rect(20,380,60,60)
shapeRect6=Rect(90,380,60,60)
shapeRect7=Rect(20,445,60,60)
shapeRect8=Rect(90,445,60,60)
shapeRect9=Rect(20,510,60,60)
shapeRect10=Rect(90,510,60,60)
stampRect=Rect(1020,350,135,40)
stampRect1=Rect(1000,400,80,80)
stampRect2=Rect(1090,400,80,80)
stampRect3=Rect(1000,490,80,80)
stampRect4=Rect(1090,490,80,80)
leftRect=Rect(975,400,20,170)
rightRect=Rect(1175,400,20,170)
TextRect1=Rect(300,20,100,100)
TextRect3=Rect(20,530,120,120)
TextRect4=Rect(975,20,120,120)
TextRect5=Rect(975,50,120,120)
TextRect6=Rect(975,35,120,120)
TextRect7=Rect(975,65,120,120)
TextRect8=Rect(975,80,120,120)
purplePicRect=Rect(975,20,80,60)
whitePicRect=Rect(1000,300,100,20)
backRect1=Rect(250,640,200,100)
backRect2=Rect(470,640,200,100)
backRect3=Rect(690,640,200,100)
blRect=Rect(190,640,50,100)
brRect=Rect(900,640,50,100)
musicRect=Rect(1010,590,150,60)
playRect=Rect(1005,640,80,80)
pauseRect=Rect(1090,640,80,80)
b1Rect=Rect(170,80,800,550)
##############Text before loop
arialFont=font.SysFont("Arial",40)
arialblack=font.SysFont("ArialBlack",15)
comicFont=font.SysFont("Comic Sans MS",30)
TextPic1=arialFont.render("STAMPS",True,(BLUE))
algerianFont=font.SysFont("Algerian",60)
TextPic2=algerianFont.render("THE CRICKET PAINT",True,(124,255,0))
###############
#######Blitting pictures 
screen.blit(groundPic,groundRect)
draw.rect(screen,WHITE,canvasRect)#drawing the canvas BEFORE the loop
screen.blit(wheelPic,wheelRect)
screen.blit(pencilPic,pencilRect)
screen.blit(shapePic1,shapeRect1)
screen.blit(eraserPic,eraserRect)
screen.blit(savePic,saveRect)
screen.blit(clearPic,clearRect)
screen.blit(openPic,openRect)
screen.blit(undoPic,undoRect)
screen.blit(redoPic,redoRect)
screen.blit(fellipsePic,shapeRect1)
screen.blit(sprayPic,shapeRect5)
screen.blit(rectPic,shapeRect4)
screen.blit(urectPic,shapeRect3)
screen.blit(uellipsePic,shapeRect2)
screen.blit(linePic,lineRect)
screen.blit(lPic,leftRect)
screen.blit(rPic,rightRect)
screen.blit(blPic,blRect)
screen.blit(brPic,brRect)
screen.blit(playPic,playRect)
screen.blit(pausePic,pauseRect)
screen.blit(tbrushPic,shapeRect9)
screen.blit(pickerPic,shapeRect10)
screen.blit(whitePic,whitePicRect)
screen.blit(brushPic,shapeRect6)
screen.blit(musicPic,musicRect)
screen.blit(markerPic,shapeRect7)
screen.blit(bucketPic,shapeRect8)
screen.blit(purplePic1,purplePicRect)
#########Blitting the text before loop
screen.blit(TextPic1,(stampRect))
screen.blit(TextPic2,(TextRect1))
##########
undo.append(screen.subsurface(canvasRect).copy())#apending picture on canvasRect in undo list
running=True##loop starts
while running:
    click=False
    for evt in event.get(): 
        if evt.type == QUIT: 
            running = False
        if evt.type==MOUSEBUTTONDOWN:
            sx,sy=mouse.get_pos()
            backPic=screen.copy()#copying the screen
            click=True
        if evt.type==KEYDOWN:#adjusting radius
            if evt.key==K_UP:
                if rad<=70:
                    rad+=1
            if evt.key==K_DOWN:
                if rad>1:
                    rad-=1
        ######undo/redo
         #saves the canvas after the mouse button is unpressed 
        if evt.type == MOUSEBUTTONUP and canvasRect.collidepoint(mx , my): 
             undo.append(screen.subsurface(canvasRect).copy())#appending the picture in undo list after something is drawn
             ###########
    mx,my=mouse.get_pos()#mouse position inside loop
    mb=mouse.get_pressed()#mouse gets pressed inside loop
    ########drawing the tools
    draw.rect(screen,GREEN,openRect,2)
    draw.rect(screen,GREEN,saveRect,2)
    draw.rect(screen,GREEN,undoRect,2)
    draw.rect(screen,GREEN,redoRect,2)
    draw.rect(screen,GREEN,pencilRect,2)
    draw.rect(screen,GREEN,eraserRect,2)
    draw.rect(screen,GREEN,clearRect,2)
    draw.rect(screen,GREEN,shapeRect1,2)
    draw.rect(screen,GREEN,shapeRect2,2)
    draw.rect(screen,GREEN,shapeRect3,2)
    draw.rect(screen,GREEN,shapeRect4,2)
    draw.rect(screen,GREEN,lineRect,2)
    draw.rect(screen,GREEN,shapeRect5,2)
    draw.rect(screen,GREEN,shapeRect6,2)
    draw.rect(screen,GREEN,shapeRect7,2)
    draw.rect(screen,GREEN,shapeRect8,2)
    draw.rect(screen,GREEN,shapeRect9,2)
    draw.rect(screen,GREEN,shapeRect10,2)
    draw.rect(screen,GREEN,stampRect1,2)
    draw.rect(screen,GREEN,stampRect2,2)
    draw.rect(screen,GREEN,stampRect3,2)
    draw.rect(screen,GREEN,stampRect4,2)
    draw.rect(screen,GREEN,leftRect,2)
    draw.rect(screen,GREEN,rightRect,2)
    draw.rect(screen,WHITE,(stampRect1))
    draw.rect(screen,WHITE,(stampRect2))
    draw.rect(screen,WHITE,(stampRect3))
    draw.rect(screen,WHITE,(stampRect4))
    draw.rect(screen,GREEN,(backRect1),2)
    draw.rect(screen,GREEN,(backRect2),2)
    draw.rect(screen,GREEN,(backRect3),2)
    draw.rect(screen,GREEN,(blRect),2)
    draw.rect(screen,GREEN,(brRect),2)
    draw.rect(screen,GREEN,playRect,2)
    draw.rect(screen,GREEN,pauseRect,2)
    draw.rect(screen,col,sizeRect,3)
    #####selecting the tools
    if mb[0]==1:#Left click
        if pencilRect.collidepoint(mx,my):
            m=1
            tool="Pencil"
            draw.rect(screen,RED,pencilRect,2)
        elif eraserRect.collidepoint(mx,my):
            tool="Eraser"
            m=2
            draw.rect(screen,RED,eraserRect,2)
        elif shapeRect3.collidepoint(mx,my):
            tool="Rectangle"
            m=3
            draw.rect(screen,RED,shapeRect3,2)
        elif shapeRect4.collidepoint(mx,my):
            tool="Filled Rectangle"
            m=4
            draw.rect(screen,RED,shapeRect4,2)
        elif shapeRect2.collidepoint(mx,my):
            tool="Ellipse"
            m=5
        elif shapeRect1.collidepoint(mx,my):
            tool="Filled Ellipse"
            m=6
            draw.rect(screen,RED,shapeRect1,2)
        elif saveRect.collidepoint(mx,my):
            tool="Save"
            m=7
        elif openRect.collidepoint(mx,my):
            tool="Open"
            m=8
        elif lineRect.collidepoint(mx,my):
            tool="Line"
            m=9
        elif shapeRect5.collidepoint(mx,my):
            tool="Spray"
            m=10
        elif shapeRect6.collidepoint(mx,my):
            tool="Brush"
            m=11
        elif shapeRect7.collidepoint(mx,my):
            tool="Marker"
            m=23
        elif shapeRect8.collidepoint(mx,my):
            tool="Colour Fill"
            m=24
        elif shapeRect9.collidepoint(mx,my):
            tool="Transparent Brush"
            m=25
        elif shapeRect10.collidepoint(mx,my):
            tool="Colour Picker"
            m=26
        elif stampRect1.collidepoint(mx,my):
            tool="Stamp1"
            m=12
        elif stampRect2.collidepoint(mx,my):
            tool="Stamp2"
            m=21
        elif stampRect3.collidepoint(mx,my):
            tool="Stamp3"
            m=14
        elif stampRect4.collidepoint(mx,my):
            tool="Stamp4"
            m=15
        elif backRect1.collidepoint(mx,my):
            gtool="background1"#when backRect1 is clicked 
            tool="Background"
            e=5
            mm=1
            m=16
        elif backRect2.collidepoint(mx,my):#when backRect2 is clicked 
            gtool="background2"
            tool="Background"
            e=5
            mm=2
            m=17
        elif backRect3.collidepoint(mx,my):#when backRect3 is clicked 
            gtool="background3"
            tool="Background"
            e=5
            mm=3
            m=18
        elif playRect.collidepoint(mx,my) and n==0:
            tool="Play/Resume"
            mixer.music.play(-1)#Playing the music 
            n=1
            m=19
        elif playRect.collidepoint(mx,my) and n==1:
            tool="Play/Resume"
            mixer.music.unpause()#resuming the music
            m=22
        elif pauseRect.collidepoint(mx,my):
            tool="Pause"
            mixer.music.pause()#pauses the music
            m=20
    if rightRect.collidepoint(mx,my) and click==True:#going right in stamps tool
        if x==0:
            x+=4
            ####drawing rects behind the stamps
            draw.rect(screen,WHITE,(stampRect1))
            draw.rect(screen,WHITE,(stampRect2))
            draw.rect(screen,WHITE,(stampRect3))
            draw.rect(screen,WHITE,(stampRect4))
    elif leftRect.collidepoint(mx,my) and click==True:#going left in stamps tool
        if x==4:
            x-=4
            #drawing rects behind stamps
            draw.rect(screen,WHITE,(stampRect1))
            draw.rect(screen,WHITE,(stampRect2))
            draw.rect(screen,WHITE,(stampRect3))
            draw.rect(screen,WHITE,(stampRect4))
    elif ftool=="stamp":
        ###blitting the pictures of stamp icons
        screen.blit(slist[x],stampRect1)
        screen.blit(slist[x+1],stampRect2)
        screen.blit(slist[x+2],stampRect3)
        screen.blit(slist[x+3],stampRect4)
    if brRect.collidepoint(mx,my) and click==True:#going right in backgrounds
        gtool="s"
        if a==0:
            a+=3
    elif blRect.collidepoint(mx,my) and click==True:#going left in backgrounds 
        gtool="s"
        if a==3:
            a-=3
    ####bliting background icons
    screen.blit(blist[a],backRect1)       
    screen.blit(blist[a+1],backRect2)
    screen.blit(blist[a+2],backRect3)    
    ######using the selected tool
    if mb[0]==1:        
        if canvasRect.collidepoint(mx,my):#clicked on canvas
            screen.set_clip(canvasRect)#only allows the CANVAS to be modified
            if tool=="Pencil":
                draw.line(screen,col,(omx,omy),(mx,my))
            elif tool=="Eraser"  and f==1 and e==1:
                dx=mx-omx #horizontal distance
                dy=my-omy #vertical distance
                dist=int(sqrt(dx**2+dy**2))#getting the distance
                for i in range(1,dist+1):#in range of 1 to distance+1
                    xc=int(omx+i*dx//dist)#a variable for location
                    yc=int(omy+i*dy/dist)#a variable for location
                    draw.circle(screen,WHITE,(xc,yc),rad)
            elif tool=="Eraser" and e!=1 and mm==1: #when there is background1 on canvasRect
                try:
                    samplePic=Blist[a].subsurface((mx-170,my-80,rad,rad))#making subsurface of the background behind  
                    screen.blit(samplePic,(mx,my))#bliting the background again insted of erasing 
                except:
                    pass
            elif tool=="Eraser" and e!=1 and mm==2: #when there is background2
                try:
                    samplePic=Blist[a+1].subsurface((mx-170,my-80,rad,rad)) #making subsurface of the background behind
                    screen.blit(samplePic,(mx,my))#bliting the background again insted of erasing
                except:
                    pass
            elif tool=="Eraser" and e!=1 and mm==3:#for background3
                try:
                    samplePic=Blist[a+2].subsurface((mx-170,my-80,rad,rad))#making subsurface of the background behind 
                    screen.blit(samplePic,(mx,my))#bliting the background again insted of erasing 
                except:
                    pass
            elif tool=="Rectangle":
                w=mx-sx#variable for width
                l=my-sy#variable for length
                screen.blit(backPic,(0,0))#bliting screen with packPic 
                for i in range(rad):#drawing multiple rectangles around each other in the range of radius 
                    if w>0 and l>0 or l<0 and w<0 : #if length or width combined is greater than or less than zero
                        draw.rect(screen,col,(sx-i,sy-i,w+2*i,l+2*i),1)
                    if w>0 and l<0 or w<0 and l>0 : #if length is positive and width is negative or vice versa
                        draw.rect(screen,col,(sx-i,sy+i,(w+2*i),(l-2*i)),1)
            elif tool=="Filled Rectangle":
                screen.blit(backPic,(0,0))
                draw.rect(screen,(col),(sx,sy,mx-sx,my-sy))#drawing filled rectangle 
            elif tool=="Ellipse":#drawing unfilled ellipse
                screen.blit(backPic,(0,0))
                ###making different rects for different ellipses
                eRect=Rect(sx,sy,mx-sx,my-sy)
                elRect=Rect(sx+1,sy,mx-sx,my-sy)
                ellRect=Rect(sx-1,sy,mx-sx,my-sy)
                elliRect=Rect(sx,sy+1,mx-sx,my-sy)
                ellipRect=Rect(sx,sy-1,mx-sx,my-sy)
                #normalizing the rects for ellipse for negative lengths and widths 
                eRect.normalize()
                elRect.normalize()
                ellRect.normalize()
                elliRect.normalize()
                ellipRect.normalize()
                try:
                    ###trying to draw the ellipses in the rectangles together for different thckness
                    draw.ellipse(screen,col,eRect,rad)
                    draw.ellipse(screen,col,elRect,rad)
                    draw.ellipse(screen,col,ellRect,rad)
                    draw.ellipse(screen,col,elliRect,rad)
                    draw.ellipse(screen,col,ellipRect,rad)
                except:
                    pass
            elif tool=="Filled Ellipse":
                screen.blit(backPic,(0,0))
                eRect=Rect(sx,sy,mx-sx,my-sy)#making rect for ellipse to draw in
                eRect.normalize()#normalizing the rect for ellipse for negative lengths and widths 
                try:
                    draw.ellipse(screen,col,eRect)#drawing the filled ellipse 
                except:
                    pass
            elif tool=="Spray":
                for s in range(20):#setting a range
                    ##randmizing dx and dy for random spots on both sides
                    dx=randint(-rad,rad)
                    dy=randint(-rad,rad)
                    d=int(sqrt(dx**2+dy**2))#calculating the distance 
                    if d<rad:#if the distance is less than the radius
                        draw.circle(screen,col,(mx+dx,my+dy),0)#drawing small circles for spray
            elif tool=="Line":
                screen.blit(backPic,(0,0))
                draw.line(screen,(col),(sx,sy),(mx,my),rad) #drawing line tool     
            elif tool=="Brush":
                #getting points 
                ax=mx-omx
                ay=my-omy
                dist=int(sqrt(ax**2+ay**2))#calculating distance
                for i in range(1,dist+1):#same as eraser
                    cx=int(omx+i*ax/dist)#getting new precised points
                    cy=int(omy+i*ay/dist)
                    draw.circle(screen,col,(cx,cy),(rad))
            elif tool=="Marker":
                #same as eraser
                ax=mx-omx
                ay=my-omy
                dist=int(sqrt(ax**2+ay**2))
                for i in range(1,dist+1):
                    cx=int(omx+i*ax/dist)
                    cy=int(omy+i*ay/dist)
                    draw.rect(screen,col,(cx,cy,rad,rad))#drawing rect with new points 
            elif tool=="Colour Fill":
                screen.fill(col,canvasRect)#filling the canvas 
            elif tool=="Transparent Brush":
                dx=mx-omx #horizontal distance
                dy=my-omy #vertical distance
                dist=int(sqrt(dx**2+dy**2))
                #same as eraser (most of it)
                for i in range(1,dist+1):
                    xc=int(omx+i*dx//dist)
                    yc=int(omy+i*dy/dist)
                    transparent = Surface((rad,rad),SRCALPHA)#as sticky note
                    draw.circle(transparent,(col[0],col[1],col[2],20),(rad,rad),rad)#using rgba feature to make it transpaent
                    screen.blit(transparent,(xc-rad,yc-rad))#bliting the surface
            elif ftool=="stamp":###bliting stamps on canvas
                screen.blit(backPic,(0,0))
                if tool=="Stamp1":
                    screen.blit(slist[x],(mx,my))
                if tool=="Stamp2":
                    screen.blit(slist[x+1],(mx,my))
                if tool=="Stamp3":
                    screen.blit(slist[x+2],(mx,my))
                if tool=="Stamp4":
                    screen.blit(slist[x+3],(mx,my))
            screen.set_clip(None)#EVERYTHING can be modified
    if tool=="Background":#bliting the background on canvas
        if gtool=="background1":
            screen.blit(Blist[a],(170,80))
        elif gtool=="background2":
            screen.blit(Blist[a+1],(170,80))
        elif gtool=="background3":
            screen.blit(Blist[a+2],(170,80))
        
            
    #1 step tools
    if click: #left mouse click (button down)
        if clearRect.collidepoint(mx,my):#clearing the canvas
            draw.rect(screen,WHITE,canvasRect)
            print("clearing the screen")
            tool="clear"
            m=13
            f=1
            e=1
        elif saveRect.collidepoint(mx,my):#saving the canvas
            try:
                fname=filedialog.asksaveasfilename(defaultextension=".png")#ask the user to create a name for a file
                image.save(screen.subsurface(canvasRect),fname)#saving the image
            except:
                print("Saving Error")
            tool="Save"
        elif openRect.collidepoint(mx,my):#loading a picture
            try:
                fname=filedialog.askopenfilename()#asking to open a certain file
                mname=image.load(fname)#loading the image
                mname=transform.scale(mname,(800,550))#Resizing it to canvas
                screen.blit(mname,canvasRect)#bliting it on canvas
            except:
                print("Loading Error")#print loading error if it fails to load
            tool="Load"
        elif redoRect.collidepoint(mx , my): #redo tool  
             if len(redo) > 0:#if the length of redo list is greater than zero
                redo1 = redo.pop()#removes the element from the list 
                undo.append(redo1)#appending the element into undo list after removing from redo list
                screen.blit(undo[-1],(170,80))#blitting last pic in undo list on canvas
                tool="redo"
                m=27
        elif undoRect.collidepoint(mx,my): #undo tool
             if len(undo) >1:#if the length of redo list is greater than one
                undo1 = undo.pop() #removes the element from the list
                redo.append(undo1) #appending the element into redo list after removing from undo list
                screen.blit(undo[-1],(170,80))#bliting lat picture on canvas 
                tool="undo"
                m=28
        elif tool=="Colour Picker": #picking colors from anywhere in the window
                c=screen.get_at((mx,my))#getting the colors
                col=c
                draw.circle(screen,col,(1080,200),10)#drawing circle in the wheel
                col=screen.get_at((mx,my))#getting colour at mouse position when clicked
                ###making rects for ellipse
                colRect=Rect(990,110,180,180)
                coloRect=Rect(991,109,180,180)
                colouRect=Rect(990,111,180,180)
                colourRect=Rect(989,110,180,180)
                colourrRect=Rect(990,109,180,180)
#######Drawing the circle around wheel 
                draw.ellipse(screen,col,colRect,3)
                draw.ellipse(screen,col,coloRect,3)
                draw.ellipse(screen,col,colouRect,3)
                draw.ellipse(screen,col,colourRect,3)
                draw.ellipse(screen,col,colourrRect,3)
                draw.circle(screen,col,(1080,200),10)
#####Drawing col Rect around canvas
    for c in range (5):
        draw.rect(screen,col,(170-c,80-c,800+2*c,550+2*c),1)        
    ##### hovering
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,pencilRect,2)
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,eraserRect,2)
    if openRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,openRect,2)
    if saveRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,saveRect,2)
    if redoRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,redoRect,2)
    if undoRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,undoRect,2)
    if lineRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,lineRect,2)
    if clearRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,clearRect,2)
    if shapeRect1.collidepoint(mx,my):
        draw.rect(screen,BLUE,shapeRect1,2)
    if shapeRect2.collidepoint(mx,my):
        draw.rect(screen,BLUE,shapeRect2,2)
    if shapeRect3.collidepoint(mx,my):
        draw.rect(screen,BLUE,shapeRect3,2)
    if shapeRect4.collidepoint(mx,my):
        draw.rect(screen,BLUE,shapeRect4,2)
    if shapeRect5.collidepoint(mx,my):
        draw.rect(screen,BLUE,shapeRect5,2)
    if shapeRect6.collidepoint(mx,my):
        draw.rect(screen,BLUE,shapeRect6,2)
    if stampRect1.collidepoint(mx,my):
        draw.rect(screen,BLUE,stampRect1,2)
    if stampRect2.collidepoint(mx,my):
        draw.rect(screen,BLUE,stampRect2,2)
    if stampRect3.collidepoint(mx,my):
        draw.rect(screen,BLUE,stampRect3,2)
    if stampRect4.collidepoint(mx,my):
        draw.rect(screen,BLUE,stampRect4,2)
    if shapeRect7.collidepoint(mx,my):
        draw.rect(screen,BLUE,shapeRect7,2)
    if shapeRect8.collidepoint(mx,my):
        draw.rect(screen,BLUE,shapeRect8,2)
    if shapeRect9.collidepoint(mx,my):
        draw.rect(screen,BLUE,shapeRect9,2)
    if shapeRect10.collidepoint(mx,my):
        draw.rect(screen,BLUE,shapeRect10,2)
    if backRect1.collidepoint(mx,my):
        draw.rect(screen,BLUE,backRect1,2)
    if backRect2.collidepoint(mx,my):
        draw.rect(screen,BLUE,backRect2,2)
    if backRect3.collidepoint(mx,my):
        draw.rect(screen,BLUE,backRect3,2)
    if rightRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,rightRect,2)
    if leftRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,leftRect,2)
    if blRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,blRect,2)
    if brRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,brRect,2)
    if playRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,playRect,2)
    if pauseRect.collidepoint(mx,my):
        draw.rect(screen,BLUE,pauseRect,2)
       ##### showing selected tool
    if m==1:
        draw.rect(screen,RED,pencilRect,2)
    elif m==2:
        draw.rect(screen,RED,eraserRect,2)
    elif m==3:
        draw.rect(screen,RED,shapeRect3,2)
    elif m==4:
        draw.rect(screen,RED,shapeRect4,2)
    elif m==5:
        draw.rect(screen,RED,shapeRect2,2)
    elif m==6:
        draw.rect(screen,RED,shapeRect1,2)
    elif m==7:
        draw.rect(screen,RED,saveRect,2)
    elif m==8:
        draw.rect(screen,RED,openRect,2)
    elif m==9:
        draw.rect(screen,RED,lineRect,2)
    elif m==10:
        draw.rect(screen,RED,shapeRect5,2)
    elif m==11:
        draw.rect(screen,RED,shapeRect6,2)
    elif m==12:
        draw.rect(screen,RED,stampRect1,2)
    elif m==13:
        draw.rect(screen,RED,clearRect,2)
    elif m==21:
        draw.rect(screen,RED,stampRect2,2)
    elif m==14:
        draw.rect(screen,RED,stampRect3,2)
    elif m==15:
        draw.rect(screen,RED,stampRect4,2)
    elif m==16:
        draw.rect(screen,RED,backRect1,2)
    elif m==17:
        draw.rect(screen,RED,backRect2,2)
    elif m==18:
        draw.rect(screen,RED,backRect3,2)
    elif m==19:
        draw.rect(screen,RED,playRect,2)
    elif m==20:
        draw.rect(screen,RED,pauseRect,2)
    elif m==22:
        draw.rect(screen,RED,playRect,2)
    elif m==23:
        draw.rect(screen,RED,shapeRect7,2)
    elif m==24:
        draw.rect(screen,RED,shapeRect8,2)
    elif m==25:
        draw.rect(screen,RED,shapeRect9,2)
    elif m==26:
        draw.rect(screen,RED,shapeRect10,2)
    elif m==27:
        draw.rect(screen,RED,redoRect,2)
    elif m==28:
        draw.rect(screen,RED,undoRect,2)
    #####Creating text for tools     
    TextPic3=arialblack.render("tool:"+tool,True,(BLUE))
    TextPic5=arialblack.render("Thickness/Radius:"+str(rad),True,(BLUE))
    TextPic6=arialblack.render("Use key UP and DOWN",True,(BLUE))
    TextPic7=arialblack.render("to adjust Radius",True,(BLUE))
    TextPic8=arialblack.render(str(col),True,(BLUE))
    ####Bliting the text and pictures at the back of text
    screen.blit(whitePic,whitePicRect)
    screen.blit(purplePic1,purplePicRect)
    screen.blit(TextPic3,(TextRect4))
    screen.blit(TextPic5,(TextRect6))
    screen.blit(TextPic6,(TextRect7))
    screen.blit(TextPic7,(TextRect8))
    screen.blit(TextPic8,(whitePicRect))
    if canvasRect.collidepoint(mx,my):#bliting the mouse position of canvas
        px,py=mouse.get_pos()#getting mouse position
        TextPic4=arialblack.render("Mouse Position:"+str(px-170)+","+str(py-80),True,(BLUE))
        screen.blit(TextPic4,(TextRect5))#bliting the mouse position on purple picture
    ####changing the colour
    dist=((1080-mx)**2+(200-my)**2)**0.5#getting radius of wheel
    if wheelRect.collidepoint(mx,my):#when mouse is in wheel rect
        if mb[0]==1:#when clicked 
            if dist<90:
                col=screen.get_at((mx,my))#getting colour at mouse clicked
                ##defining rects around wheel
                colRect=Rect(990,110,180,180)
                coloRect=Rect(991,109,180,180)
                colouRect=Rect(990,111,180,180)
                colourRect=Rect(989,110,180,180)
                colourrRect=Rect(990,109,180,180)
#######Drawing the circle around wheel 
                draw.ellipse(screen,col,colRect,3)
                draw.ellipse(screen,col,coloRect,3)
                draw.ellipse(screen,col,colouRect,3)
                draw.ellipse(screen,col,colourRect,3)
                draw.ellipse(screen,col,colourrRect,3)
                ###drawing circle inside the wheel
                draw.circle(screen,col,(1080,200),10)                    
    omx=mx
    omy=my
    display.flip() 
quit() #
