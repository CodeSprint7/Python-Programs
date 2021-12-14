from tkinter import *
from PyDictionary import PyDictionary

#creating object for tkinter
root=Tk()
pd=PyDictionary()
root.geometry("400x300")#providing the size for window
root.title("my project") #title of the window
root.config(bg="orange") #for background color
#widgets are like labels,buttons,entries e.t.c

def printoutput():
  meaningans.config(text=pd.meaning(entry1.get())['Noun'][0]) #taking input from button and storing in text and printing after meaningans
  synonymans.config(text=pd.synonym(entry1.get()))
  antonymans.config(text=pd.antonym(entry1.get()))

#antonym(entry1.get())[0] means the first anotonym in the dict
#entry.get() means taking the input and antonym(input) checks the antonym in the dict and store in text and will be displayed after the respective lable

#creating frame object for root
frame1=Frame(root,bg="orange")
label1=Label(frame1,text="word dictionary project",font= ('Helvetica 20 italic'),bg= "orange", fg= "black") #label parent is frame1
label2=Label(frame1,text="enter word",font= ('Helvetica 10 italic'),bg= "orange", fg= "black")
entry1=Entry(frame1)
button1=Button(frame1,text="click me",command=printoutput)
#pack order wise
frame1.grid()
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
entry1.grid(row=2, column=0)
button1.grid(row=3, column=0)

frame2=Frame(root,bg="orange")
meaning=Label(frame2,text="Meaning: ",font= ('Helvetica 10 italic'),bg= "orange", fg= "black")
meaningans=Label(frame2,text="",font= ('Helvetica 10 italic'),bg= "orange", fg= "blue")
frame2.grid() #packs to the main window
meaning.grid(row=0, column=0)
meaningans.grid(row=0, column=1)

frame3=Frame(root,bg="orange")
synonym=Label(frame3,text="Synonym: ",font= ('Helvetica 10 italic'),bg= "orange", fg= "black")
synonymans=Label(frame3,text="",font= ('Helvetica 10 italic'),bg= "orange", fg= "blue")
frame3.grid() #packs to the main window
synonym.grid(row=0, column=0)
synonymans.grid(row=0, column=1)

frame4=Frame(root,bg="orange")
antonym=Label(frame4,text="Antonym: ",font= ('Helvetica 10 italic'),bg= "orange", fg= "black")
antonymans=Label(frame4,text="",font= ('Helvetica 10 italic'),bg= "orange", fg= "blue")
frame4.grid() #packs to the main window
antonym.grid(row=0, column=0)
antonymans.grid(row=0, column=1)

root.mainloop() # enteing the main event loop