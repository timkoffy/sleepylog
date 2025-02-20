
from fileinput import close
from locale import windows_locale
from os import write
from tkinter import *
from tkinter import ttk
import pyglet,tkinter

root = Tk()
root.title("sleepylog")
root.geometry('420x650')
root.resizable(width=1, height=1)

pyglet.font.add_file('Itim-Regular.ttf')



def day_to_y(day):
    y1=day*20
    y0=y1-20
    return f'{y0},{y1}'

def boxDraw(x0,x1,y):
    #box = canvas3.create_rectangle(x0,y0,x1,y1, fill=colorBoxID, outline=colorBoxOutlineID, width=3)
    y=y.split(',')
    y0=y[0]
    y1 = y[1]

    box = canvas3.create_rectangle(x0, y0, x1, y1, fill=colorBoxID, width=0)

def boxDraw_back(x0,x1,y):
    #box = canvas3.create_rectangle(x0,y0,x1,y1, fill=colorBoxID, outline=colorBoxOutlineID, width=3)
    y=y.split(',')
    y0=int(y[0])
    y1=int(y[1])

    box = canvas3.create_rectangle(x0-3, y0-3, x1+3, y1+3, fill=colorBoxOutlineID, width=0)


colorID = '#555258'
colorID_High = '#F0F0F0'
colorCanvasID = '#201B24'
colorBoxID = '#431368'
colorBoxOutlineID = '#9000FF'

padLabelX=3
padLabelY=1


canvas1=Canvas(bg="#201B24",  width=420, height=40)
canvas1.pack(anchor=CENTER, expand=0)
canvas1.create_text(210, 20, font="Itim 20", anchor='center', text="Sleepy log", fill=colorID_High)

canvas2=Canvas(bg="#201B24",  width=420, height=40)
canvas2.pack(anchor=CENTER, expand=0)
canvas2.create_text(20, 21, font="Itim 10", anchor='center', text="19", fill=colorID)
canvas2.create_text(40, 21, font="Itim 10", anchor='center', text="20", fill=colorID)
canvas2.create_text(60, 21, font="Itim 10", anchor='center', text="21", fill=colorID)
canvas2.create_text(80, 21, font="Itim 10", anchor='center', text="22", fill=colorID)
canvas2.create_text(100, 21, font="Itim 10", anchor='center', text="23", fill=colorID_High)
canvas2.create_text(120, 20, font="Itim 12", anchor='center', text="0", fill=colorID)
canvas2.create_text(140, 20, font="Itim 12", anchor='center', text="1", fill=colorID)
canvas2.create_text(160, 20, font="Itim 12", anchor='center', text="2", fill=colorID)
canvas2.create_text(180, 20, font="Itim 12", anchor='center', text="3", fill=colorID)
canvas2.create_text(200, 20, font="Itim 12", anchor='center', text="4", fill=colorID)
canvas2.create_text(220, 20, font="Itim 12", anchor='center', text="5", fill=colorID)
canvas2.create_text(240, 20, font="Itim 12", anchor='center', text="6", fill=colorID)
canvas2.create_text(260, 20, font="Itim 12", anchor='center', text="7", fill=colorID_High)
canvas2.create_text(280, 20, font="Itim 12", anchor='center', text="8", fill=colorID)
canvas2.create_text(300, 20, font="Itim 12", anchor='center', text="9", fill=colorID)
canvas2.create_text(320, 21, font="Itim 10", anchor='center', text="10", fill=colorID)
canvas2.create_text(340, 21, font="Itim 10", anchor='center', text="11", fill=colorID)
canvas2.create_text(360, 21, font="Itim 10", anchor='center', text="12", fill=colorID)
canvas2.create_text(380, 21, font="Itim 10", anchor='center', text="13", fill=colorID)
canvas2.create_text(400, 21, font="Itim 10", anchor='center', text="14", fill=colorID)

canvas3=Canvas(bg="#201B24",  width=420, height=200,scrollregion=(0,0,5000,5000))
vbar=Scrollbar(canvas3, orient=VERTICAL)
vbar.pack(anchor=E,expand=1,fill=Y)
vbar.config(command=canvas3.yview)
canvas3.config(yscrollcommand=vbar.set)
canvas3.pack(anchor=CENTER,expand=1,fill=BOTH)

canvas3.create_line(100,0,100,5000,fill=colorID, width=3, dash = (10, 10))
canvas3.create_line(260,0,260,5000,fill=colorID, width=3, dash = (10, 10))

def time_to_x(x):
    if x == 19: return 20
    if x == 20: return 40
    if x == 21: return 60
    if x == 22: return 80
    if x == 23: return 100
    if x == 0: return 120
    if x == 1: return 140
    if x == 2: return 160
    if x == 3: return 180
    if x == 4: return 200
    if x == 5: return 220
    if x == 6: return 240
    if x == 7: return 260
    if x == 8: return 280
    if x == 9: return 300
    if x == 10: return 320
    if x == 11: return 340
    if x == 12: return 360
    if x == 13: return 380
    if x == 14: return 400

x2list=[]
x1list=[]
ylist=[]

with open("currentday.txt", 'r') as currentday_file:
    next(currentday_file)
    for currentdayvalue in currentday_file.readlines():
        ylist.append([z for z in currentdayvalue.strip()])

with open("sleepylognight.txt", 'r') as sleepylognight_file:
    for x1_day_value in sleepylognight_file:
        x1list.append([q for q in x1_day_value.strip()])

with open("sleepylogday.txt", 'r') as sleepylogday_file:
    for x2_day_value in sleepylogday_file:
        x2list.append([w for w in x2_day_value.strip()])

output_x1list = [time_to_x(int(''.join(sublist_x1))) for sublist_x1 in x1list]
output_x2list = [time_to_x(int(''.join(sublist_x2))) for sublist_x2 in x2list]
output_ylist = [int(''.join(sublist_y)) for sublist_y in ylist]

for dayvalueMAIN in range(len(output_ylist)):
    boxDraw_back(output_x1list[dayvalueMAIN],output_x2list[dayvalueMAIN],day_to_y(output_ylist[dayvalueMAIN]))

for dayvalueMAIN in range(len(output_ylist)):
    boxDraw(output_x1list[dayvalueMAIN],output_x2list[dayvalueMAIN],day_to_y(output_ylist[dayvalueMAIN]))

def clear_all():
    #очистка всех файлов
    with open('sleepylognight.txt', 'w'):
        pass
    with open('sleepylogday.txt', 'w'):
        pass
    with open('currentday.txt', 'w') as file:
        file.write('0')
    exit()




canvas4=Canvas(bg="#201B24",  width=420, height=50)
canvas4.pack(anchor=N,expand=0)

btn = ttk.Button(text="clear_all",command=clear_all)
canvas4.create_window(10, 10, anchor=NW, window=btn, width=100, height=30)



root.mainloop()