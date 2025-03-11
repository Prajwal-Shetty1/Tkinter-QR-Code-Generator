from tkinter import *
import qrcode

root=Tk()
root.title("QR Generator")
root.geometry("1000x500")
root.config(bg="Dark Blue")
root.resizable(True,True)



#To define a function named generate
def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("QRcode/" + str(name) + ".png")
    
#to extract a QR image from file
    global Image
    Image = PhotoImage(file="QRcode/" + str(name) + ".png")
    Image_view.config(image=Image)
    
#to place a QR image
Image_view=Label(root,bg="Dark Blue")
Image_view.pack(padx=50,pady=10,side=RIGHT)


#To create a label as scan&share QR
Label(root,text="Scan&Share QR",bg="Dark Blue",fg="White",font="arial 20").place(x=50,y=150)

#To create a Entrybox1
title=Entry(root,width=17,font="arial 20")
title.place(x=50,y=200)

#To create a Entrybox2
entry=Entry(root,width=27,font="arial 20")
entry.place(x=50,y=260)

#to create a button as a generate
Button(root,text="GENERATE",bg="white",fg="Black",width=20,height=2,command=generate).place(x=50,y=320)




root.mainloop()
