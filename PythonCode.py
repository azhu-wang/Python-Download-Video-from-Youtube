from tkinter import *
from pytube import YouTube
import os
import threading

def loadVideo(): 
    x.set("狀態:檔案下載中(無反應可多按幾次)...")
    vlinks = links.get()
    yt = YouTube(vlinks)

    threading.Thread(target=yt.register_on_progress_callback(progress)).start()
    threading.Thread(target=lambda:downoad(yt,path)).start()

    videoViews = yt.views
    videoSeconds = yt.length
    videoRating = yt.rating
    videoTitle = yt.title
    a.set(str(videoViews ))
    b.set(str(videoSeconds))
    c.set(str(videoRating)+" / 5")
    d.set(str(videoTitle))
    x.set("狀態:影音檔案下載中") 
    y.set("[Download]:")

def downoad(yt,path):
    yt.streams.first().download(path)
    
def progress(streams, chunk, bytes_remaining):
    if int(bytes_remaining) == 0:
        x.set("狀態:影音檔案下載完成") 
        y.set("[Download]:██████████ 100%"+" in "+ path)
    size = streams.filesize
    progress = (float(abs(bytes_remaining-size)/size))*float(100)
    y.set('[Download]:[%s%s]%.2f%%' % ('█' * int(progress//5), ' '*(20-int(progress//5)), float(progress)))
 
def reMove():
    links.set(" ")

def width():
    window.title("YouTube影片下載小工具  by王璽鑄")
    window.geometry("250x240")
def back():
    window.title("YouTube影片下載小工具  by王璽鑄")
    window.geometry("500x240")
 
path="d:\\myYoutube"     #位置
if not os.path.isdir(path):
    os.mkdir(path)

window = Tk()
window.title("YouTube影片下載小工具  by王璽鑄")
window.geometry("500x240")

x = StringVar()
y = StringVar()
a = StringVar()
b = StringVar()
c = StringVar()
d = StringVar()
links = StringVar()
x.set("狀態:等待輸入影片網址")
y.set("[Download]:")
a.set("...")
b.set("...")
c.set("...")
d.set("...")

lab0 = Label(window,text="請輸入輸入影片網址 : ",bg="lightyellow",width=20).grid(row=0)
lab1 = Label(window,text="影片標題     : ",bg="lightyellow",width=15)
lab2 = Label(window,text="影片評價     : ",bg="lightyellow",width=15)
lab3 = Label(window,text="影片長度(秒) : ",bg="lightyellow",width=15)
lab4 = Label(window,text="影片觀賞次數 : ",bg="lightyellow",width=15)
lab5 = Label(window,textvariable=x,width=45)
lab6 = Label(window,textvariable=y,width=45)
lab11 = Label(window,textvariable=d,width=50)
lab22 = Label(window,textvariable=c,width=50)
lab33 = Label(window,textvariable=b,width=50)
lab44 = Label(window,textvariable=a,width=50)

lab1.place(x=0,y=30)
lab2.place(x=0,y=60)
lab3.place(x=0,y=90)
lab4.place(x=0,y=120)
lab5.place(x=65,y=150)
lab6.place(x=80,y=180)
lab11.place(x=120,y=30)
lab22.place(x=120,y=60)
lab33.place(x=120,y=90)
lab44.place(x=120,y=120)

e1 = Entry(window,textvariable=links,width=40)
e1.grid(row=0,column=1)
btn1 = Button(window,text="下載",command=loadVideo)
btn1.place(x=100,y=210)
btn2 = Button(window,text="重置",command=reMove)
btn2.place(x=200,y=210)
btn3 = Button(window,text="結束",command=window.destroy)
btn3.place(x=300,y=210)

menu = Menu(window)        #視窗變化
window["menu"] = menu
filemenu = Menu(menu, tearoff=0) 
menu.add_cascade(label="視窗調整", menu=filemenu)
filemenu.add_command(label="視窗變窄", command=width)
filemenu.add_separator() 
filemenu.add_command(label="回復", command=back)

window.mainloop()
