from tkinter import * 
from tkinter import messagebox
root = Tk()
root.title('raphs game bitch')
clicked=True
count=0
def winner():
    # check for x
    if b1['text']=='x' and b2['text']=='x' and b3['text']=='x':
        messagebox.showinfo('X and O', 'we have a winner')
        b1.configure(bg='blue')
        b2.configure(bg='blue')
        b3.configure(bg='blue')
    elif b1['text']=='x' and b4['text']=='x' and b7['text']=='x':
        messagebox.showinfo('X and O', 'we have a winner')
        b1.configure(bg='blue')
        b4.configure(bg='blue')
        b7.configure(bg='blue')
    elif b1['text']=='x' and b5['text']=='x' and b9['text']=='x':
        messagebox.showinfo('X and O', 'we have a winner')
        b1.configure(bg='blue')
        b5.configure(bg='blue')
        b9.configure(bg='blue')
    elif b2['text']=='x' and b5['text']=='x' and b8['text']=='x':
        messagebox.showinfo('X and O', 'we have a winner')
        b2.configure(bg='blue')
        b5.configure(bg='blue')
        b8.configure(bg='blue')
    elif b3['text']=='x' and b6['text']=='x' and b9['text']=='x':
        messagebox.showinfo('X and O', 'we have a winner')
        b3.configure(bg='blue')
        b6.configure(bg='blue')
        b9.configure(bg='blue')
    elif b4['text']=='x' and b5['text']=='x' and b6['text']=='x':
        messagebox.showinfo('X and O', 'we have a winner')
        b4.configure(bg='blue')
        b5.configure(bg='blue')
        b6.configure(bg='blue')
    elif b7['text']=='x' and 8['text']=='x' and b9['text']=='x':
        messagebox.showinfo('X and O', 'we have a winner')
        b7.configure(bg='blue')
        b8.configure(bg='blue')
        b9.configure(bg='blue')
    
    #check for o
    if b1['text']=='o' and b2['text']=='o' and b3['text']=='o':
        messagebox.showinfo('X and O', 'we have a winner')
        b1.configure(bg='blue')
        b2.configure(bg='blue')
        b3.configure(bg='blue')
    elif b1['text']=='o' and b4['text']=='o' and b7['text']=='o':
        messagebox.showinfo('X and O', 'we have a winner')
        b1.configure(bg='blue')
        b4.configure(bg='blue')
        b7.configure(bg='blue')
    elif b1['text']=='o' and b5['text']=='o' and b9['text']=='o':
        messagebox.showinfo('X and O', 'we have a winner')
        b1.configure(bg='blue')
        b5.configure(bg='blue')
        b9.configure(bg='blue')
    elif b2['text']=='o' and b5['text']=='o' and b8['text']=='o':
        messagebox.showinfo('X and O', 'we have a winner')
        b2.configure(bg='blue')
        b5.configure(bg='blue')
        b8.configure(bg='blue')
    elif b3['text']=='o' and b6['text']=='o' and b9['text']=='o':
        messagebox.showinfo('X and O', 'we have a winner')
        b3.configure(bg='blue')
        b6.configure(bg='blue')
        b9.configure(bg='blue')
    elif b4['text']=='o' and b5['text']=='o' and b6['text']=='o':
        messagebox.showinfo('X and O', 'we have a winner')
        b4.configure(bg='blue')
        b5.configure(bg='blue')
        b6.configure(bg='blue')
    elif b7['text']=='o' and 8['text']=='o' and b9['text']=='o':
        messagebox.showinfo('X and O', 'we have a winner')
        b7.configure(bg='blue')
        b8.configure(bg='blue')
        b9.configure(bg='blue')
def click(b):
    global clicked,count
    if b['text']== ' ' and clicked== True:
        b['text']= 'x'
        clicked= False
        count= count+1
        winner()
    elif b['text']==' ' and clicked == False:
        b['text']='o'
        clicked = True
        count= count+1
        winner()
    else:
        messagebox.showerror('X and O','What are you doing')


b1= Button(root, text=' ',font=(20),height= 3,width=6, bg= 'systembuttonface',command=lambda:click(b1))
b2= Button(root, text=' ',font=(20),height= 3,width=6, bg= 'systembuttonface',command=lambda:click(b2))
b3= Button(root, text=' ',font=(20),height= 3,width=6, bg= 'systembuttonface',command=lambda:click(b3))
b4= Button(root, text=' ',font=(20),height= 3,width=6, bg= 'systembuttonface',command=lambda:click(b4))
b5= Button(root, text=' ',font=(20),height= 3,width=6, bg= 'systembuttonface',command=lambda:click(b5))
b6= Button(root, text=' ',font=(20),height= 3,width=6, bg= 'systembuttonface',command=lambda:click(b6))
b7= Button(root, text=' ',font=(20),height= 3,width=6, bg= 'systembuttonface',command=lambda:click(b7))
b8= Button(root, text=' ',font=(20),height= 3,width=6, bg= 'systembuttonface',command=lambda:click(b8))
b9= Button(root, text=' ',font=(20),height= 3,width=6, bg= 'systembuttonface',command=lambda:click(b9))
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

mainloop()
