from tkinter import *
from tkinter.ttk import *
from driver import *
# def selection(): 
#     if(radio.get()==1):
#         selection = "Iterative DNS Querying: "
#         selectLabel.config(text = selection) 
#     elif (radio.get() ==2):
#         selection = "Recursive DNS Querying:  "  
#         selectLabel.config(text = selection)  

#main window object named root
connect()

def submit():
    url = urlINP.get()
    loc = locINP.get()
    result=checkCache(url)
    if(result=="empty"):
        if(radio.get()==1):
            ip = iterativeDNSResolver(url,loc)
        else:
            ip = recursiveDNSResolution(url,loc)
    else:
        ip=getCache(url)
    selectLabel.config(text = "IP ADDRESS: "+ip)


root = Tk()
root.geometry('800x600')
root.title('DNS Visualiser')

lbl = Label(root,text = "DNS VISUALISATION").place(x = 360, y = 30)
url =  Label(root,text = "URL").place(x = 200,y = 60)
location =  Label(root,text = "Location").place(x = 200,y = 100)

urlINP= StringVar()
locINP= StringVar()
radio = IntVar()
url_input_area = Entry(root,width = 40,textvariable = urlINP).place(x=270,y=60)
location_input_area = Entry(root,width = 40,textvariable = locINP).place(x=270,y=100)

lbl = Label(root,text = "Select mode of querying:").place(x = 200, y = 130)
    
R1 = Radiobutton(root,text = "Iterative",variable = radio,value = 1).place(x = 210,y  = 160 )
R2 = Radiobutton(root,text = "Recursive",variable = radio,value = 2).place(x = 210,y  = 180 )

button = Button(root, text="Visualise",command =submit ).place(x = 350 , y = 210)

selectLabel = Label(root)
selectLabel.place(x = 100, y = 240)

root.mainloop()
close()
