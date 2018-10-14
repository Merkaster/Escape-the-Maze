import tkinter as tk
from tkinter import *



def visualize(x,y):

    root = tk.Tk()
    root.title("drawing lines")
    # create the drawing canvas
    sq = 80
    numsq = 6
    thickevery = 1
    normal = 1
    wide = 2
    canvas = tk.Canvas(root, width=500, height=400, bg='white')
    canvas.pack()
    
    # draw horizontal lines
    x1 = 0
    x2 = 6*sq
    for k in range(0, sq*(numsq+1), sq):
        y1 = k
        y2 = k
        if k % thickevery: w = normal
        else: w = wide
        canvas.create_line(x1, y1, x2, y2, width=w)
        
    # draw vertical lines
    y1 = 0
    y2 = 5*sq
    for k in range(0, sq*(numsq+1), sq):
        x1 = k
        x2 = k
        if k % thickevery: w = normal
        else: w = wide
        canvas.create_line(x1, y1, x2, y2, width=w)
    
    canvas.pack(expand = YES, fill = BOTH)
    
    #Import the icons
    robot = PhotoImage(file='robot.png')
    bomb = PhotoImage(file = 'bomb.png')
    flag = PhotoImage(file = 'Flag.png')
    energy = PhotoImage(file = 'energy.png')
    
    canvas.create_image(x,y,image = robot,anchor = NW)
    canvas.create_image(330,340,image = flag,anchor = NW)
    canvas.create_image(180,20,image = energy,anchor = NW)
    canvas.create_image(180,180,image = energy,anchor = NW)
    canvas.create_image(420,180,image = energy,anchor = NW)
    canvas.create_image(100,340,image = energy,anchor = NW)
    canvas.create_image(100,100,image = bomb,anchor = NW)
    canvas.create_image(330,100,image = bomb,anchor = NW)
    canvas.create_image(20,260,image = bomb,anchor = NW)
    canvas.create_image(260,260,image = bomb,anchor = NW)
    
    #after 0.5 seconds close the window 
    root.after(500, root.destroy)
    root.mainloop()