import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Home Page")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('bg1.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


#
label_l2 = tk.Label(root, text="___Crowd + Suspicious Activity Detection System___",font=("times", 30, 'bold'),
                    background="black", fg="white", width=68, height=2)
label_l2.place(x=0, y=0)






frame_alpr = tk.LabelFrame(root, text=" --Login & Register-- ", width=800, height=300, bd=5, font=('times', 14, ' bold '),bg="grey")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=400, y=400)


def log():
#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    from subprocess import call
    call(["python","login.py"])
    #root.destroy()
    
def reg():
    from subprocess import call
    call(["python","registration.py"])
    #root.destroy()
    
def window():
  root.destroy()
  


#####################################################################################################################

button1 = tk.Button(frame_alpr, text="Login", command=log, width=15, height=1,font=('times', 15, ' bold '), bg="green", fg="white")
button1.place(x=100, y=20)

button2 = tk.Button(frame_alpr, text="Registration",command=reg,width=15, height=1,font=('times', 15, ' bold '), bg="green", fg="white")
button2.place(x=300, y=100)

button3 = tk.Button(frame_alpr, text="Exit",command=window,width=14, height=1,font=('times',15, ' bold '), bg="red", fg="white")
button3.place(x=500, y=200)





root.mainloop()