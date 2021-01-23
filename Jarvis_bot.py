import random
from tkinter import *
import pyttsx3
import wikipedia
import webbrowser

root=Tk()
title=Label(root,text="Welcome",font=("times new roman",12,"bold"),bg="lime",fg="darkorange",relief=GROOVE,border=2)
title.place(x=0,y=0,relwidth=1)
#---------------------------------------------------------------Command--------------------------------------------------------------------------------------------------------
hellow =["hi","is anyone there?","hello"]
bye = ["goodbye","bye","by","see you letter","i am leaving","exit","close","abort"]
make = ["who make you","who develope you","who created you"]
about = ["Who are you","about you","your details"]
name = ["what is your name","your name"]
youtube = ["open youtube","youtube"]
google = ["open google","google"]
music = ["play music","music","play song","open music","open song"]
who = ["who are you"]
what =["What are you","what are you doing","what about you"]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wi():
    def wiki():

    #print(entry_1)
        s1 = entry_1.get()
    #print(entry_1)
        s2 = wikipedia.summary(s1)
        txt.insert(END,"Answer:"+s2)
    

    Second=Toplevel()
    #Second = Tk()
    Second.title("Jarvis Bot")
    Second.geometry("500x400+50+50")
    Second.resizable(False,False)
    Second.iconbitmap("D:\my_peronal\Iconshock-Real-Vista-Mail-Robot.ico")
    Second.configure(bg="magenta")

    k=Label(Second,text="Enter")
    k.grid(row=0,column=0)
    entry_1 = Entry(Second,fg="red")
    entry_1.grid(row=1,column=0)
    txt = Text(Second,height=20,width=70)
    txt.grid(row=2,column=0)
    b = Button(Second,text="submit",command=wiki)
    b.place(x=190,y=363) 
    b2 = Button(Second,text="Exit",command=Second.destroy)
    b2.place(x=250,y=363)


    Second.mainloop()

def send():
    send="You -> "+e.get("0.0","end")
    txt.insert(END,"\n"+send)

    if(e.get("0.0","end-1c").lower() in hellow):
        botans = ["Hello !","hi"]
        s = random.choice(botans)
        txt.insert(END,"Jarvis ->"+s)
        speak(s)

    elif (e.get("0.0","end-1c").lower() in bye):
        botans = ["bye","miss you"]
        s = random.choice(botans)
        #print('Bot said - '+ s +'\n')
        txt.insert(END,"Jarvis ->"+s)
        speak(s)
        exit()
    
    elif (e.get("0.0","end-1c").lower() in make):
        botans = ["For your information Karamveer Rajput Created me ! I give Lot of thanks to him"]
        s = random.choice(botans)
        #print('Bot said - '+ s +'\n')
        txt.insert(END,"Jarvis ->"+s)
        speak(s)

    elif (e.get("0.0","end-1c").lower() in about):
        botans = ["I am Jarvis bot.I based computer program i can help you lot like a your close friend !  Simple try me to give simple command ! like i play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "]
        s = random.choice(botans)
        #print('Bot said - '+ s +'\n')
        txt.insert(END,"Jarvis ->"+s)
        speak(s)

    elif (e.get("0.0","end-1c").lower() in who):
        botans = ["I am Jarvis"]
        s = random.choice(botans)
        #print('Bot said - '+ s +'\n')
        txt.insert(END,"Jarvis ->"+s)
        speak(s)

    elif (e.get("0.0","end-1c").lower() in what):
        botans = ["I am based on computer program i can help you lot like a your close friend !  Simple try me to give simple command ! like i play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "]
        s = random.choice(botans)
        #print('Bot said - '+ s +'\n')
        txt.insert(END,"Jarvis ->"+s)
        speak(s)

    elif (e.get("0.0","end-1c").lower() in name):
        botans = ["My name is Jarvis"]
        s = random.choice(botans)
        #print('Bot said - '+ s +'\n')
        txt.insert(END,"Jarvis ->"+s)
        speak(s)

    elif (e.get("0.0","end-1c").lower() in youtube):
        botans = ["opening youtube"]
        s = random.choice(botans)
        #print('Bot said - '+ s +'\n')
        txt.insert(END,"Jarvis ->"+s)
        speak(s)
        webbrowser.open("www.youtube.com")

    elif (e.get("0.0","end-1c").lower() in google):
        botans = ["Opening Google"]
        s = random.choice(botans)
        #print('Bot said - '+ s +'\n')
        txt.insert(END,"Jarvis ->"+s)
        speak(s)
        webbrowser.open("www.google.com")

    elif (e.get("0.0","end-1c").lower() in music):
        botans = ["opening new song page from youtube"]
        s = random.choice(botans)
        #print('Bot said - '+ s +'\n')
        txt.insert(END,"Jarvis ->"+s)
        speak(s)
        webbrowser.open("https://www.youtube.com/results?search_query=new+song")

    elif "wikipedia" in (e.get("0.0","end-1c").lower()):
        wi()
    
    else:
        txt.insert(END,"Jarvis ->"+"Error")

    #e.delete(0.0,"end")

txt=Text(root,font=("times new roman",18,"bold"),height=10.4,width=42,bg="black",fg="red")
txt.place(x=0,y=25)
e=Text(root,font=("times new roman",16,"bold"),bg="yellow",fg="red",width=32)
e.place(x=144,y=290)
send=Button(text="Send",command=send,font=("times new roman",24,"bold"),bg="blue",fg="red",activebackground="lightblue",width=7,height=3)
send.place(x=0,y=290)


root.title("Jarvis Bot")
root.geometry("500x400+50+50")
root.resizable(False,False)
root.iconbitmap("D:\my_peronal\Iconshock-Real-Vista-Mail-Robot.ico")
root.configure(bg="magenta")
root.mainloop()