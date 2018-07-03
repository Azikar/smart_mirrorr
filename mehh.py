
# naudoja PILLOW , requests, ir beautifulsoup4



from tkinter import *
#import tkinter as tk
from PIL import Image, ImageTk
import time
import sys
import requests
from bs4 import BeautifulSoup

#import ImageTk
#root = Tk()
#root.configure(background='black')
#ima = Image.open(r"C:\Users\merp\Desktop\New folder (10)\meh.png")
#img=ImageTk.PhotoImage(file="C:\Users\merp\Desktop\New folder (10)\meh.png")
#ima=ima.convert('RGB')
#maxsize = (100, 100)
#root.configure(bg='black')
#ima.thumbnail(maxsize, Image.ANTIALIAS)
#x=root.winfo_screenmmheight()
#photo = ImageTk.PhotoImage(ima)



#label=Label(frame,image=ima)
#label.pack(side='top')
#curtime=' '
#clock=Label()
maxsize = (100, 100)
list ={"assets/Sun.png":'Clear',
       "assets/Cloud.png":'Overcast',
       "assets/PartlySunny.png":'Partly Cloudy',
       "assets/PartlySunny.png":'Scattered Clouds',
       "assets/Rain.png":'Rain',
       "assets/Haze.png":'Fog',
       "assets/Storm.png":'Thunderstorms with Hail',
       "assets/PartlySunny.png":'Mostly Cloudy',
       "assets/Snow.png":'Snow'    
       }

def framas(root):   
    frame=Frame(root,bg='black',width=50,height=50)
    frame2=Frame(root,bg='black',width=50,height=50)
    #virsus 
    frame.pack(side='top',fill='both',expand='yes')
    #apacia
    frame2.pack(side='bottom',fill='both',expand='yes')
    c=Clock(frame)
    w=Wether(frame)
    
    
class Clock:
    def __init__(self,frame):
        clocfr=Frame(frame,bg='white')
        clocfr.pack(side='right',anchor='n')
        self.curtime=' '
        self.clockk=Label(clocfr,compound='right',font=('Symbol',60 ),width=5,height=2 )
        self.clockk.pack(side='top',anchor='e')
        self.time()
        
        
    def time(self):
    
        newtime=time.strftime('%H:%M')
        if newtime != self.curtime:
            self.curtime=newtime
            self.clockk.config(text=self.curtime,foreground='white',background='black')
        self.clockk.after(200, self.time)
 
class Wether:
    def __init__(self,frame):
        
        self.temp=70
        self.degreeFr = Frame(frame, bg="black",width=60,height=100)
        self.degreeFr.pack(side='top', anchor='w')
        
    
        
        self.wetherr=Label(self.degreeFr,compound='top',font=('Symbol',70),pady=20)
        self.wetherr.pack(side='left',anchor='n')
        self.wetherr.config(text=self.temp,foreground='white',background='black',padx=20)

        self.deg = Label(self.degreeFr, bg="black",font=('Helvetica', 50))
        self.deg.pack(side='left', anchor='n',pady=50)
        self.deg.config(text="°C",foreground='white')

        self.pav = Label(self.degreeFr)
        self.pav.pack(side='left', anchor='n',pady=50,padx=20)

        
        
        
        

        
        self.currentlyLbl = Label(frame, font=('Helvetica', 20), foreground='white',background='black')
        self.currentlyLbl.pack(side='top', anchor='w',padx=20)
       # self.currentlyLbl.config(text="Clear")
       # self.pic=Label(wetfr,bg='white',font=('Symbol',30),width=10)
       # self.pic.pack(side='right',anchor='n')
      
       # self.pic.config(text=self.temp,foreground='white',background='black')
        self.wether()
       
    def wether(self):
        print ("ivyko")
        laipsniai=" "
        debesuotumas=" "

        r=requests.get("http://www.infosniper.net/")
        soup=BeautifulSoup(r.content)
        a=soup.find_all("td",{"class": "content-td2"})
        web="https://www.wunderground.com/cgi-bin/findweather/getForecast?query="
        miestas=" "
        sk=1
        for item in a:
    
            if sk==2:
               miestas=item.contents[0]
            sk=sk+1
            miestas="kaunas"
        print ("a",miestas)

        linkas=web+miestas
        r=requests.get(linkas)
        soup=BeautifulSoup(r.content)
        a=soup.find_all("span",{"class":"wx-value"})
        sk=1
        for item in a:
            if sk==5:
                self.currentlyLbl.config(text=item.contents[0])
                print("",item.contents[0])
                oras=item.contents[0]
            if sk==6:
                self.wetherr.config(text=item.contents[0],foreground='white',background='black',padx=20)
                print("",item.contents[0])
                break
            sk=sk+1
            
        for name, key in list.items():
            if key==oras:
                print("",name)
                img=name
        load=Image.open(img)
        load.thumbnail(maxsize, Image.ANTIALIAS)
        render= ImageTk.PhotoImage(load)
        self.pav.config(image=render)
        self.pav.image=render
        self.wetherr.after(600000, self.wether)

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        master.attributes('-fullscreen',True)
        self.state=False
       
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        self.master.attributes('-fullscreen',self.state)
        if self.state:
            self.state=False
        else:
            self.state=True
        
if __name__ == '__main__':
    root = Tk()
    FullScreenApp(root)
    
    

    
    root.configure(background='black')
    root.configure(bg='black')
    root.geometry("1000x1000")
    framas(root)
    
    
    root.mainloop()
    
