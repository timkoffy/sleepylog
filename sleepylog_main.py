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

coefficient_x=0

def day_to_y(day):
    y1=day*20
    y0=y1-20
    return f'{y0},{y1}'

def box_draw(x0,x1,y):
    y=y.split(',')
    y0=y[0]
    y1 = y[1]
    box = canvas3.create_rectangle(x0, y0, x1, y1, fill=colorBoxID, width=0)

def box_draw_back(x0,x1,y):
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
canvas1.pack(anchor=N, expand=0, fill=X)
canvas1.create_text(210, 20, font="Itim 20", anchor='center', text="Sleepy log", fill=colorID_High)

canvas2=Canvas(bg="#201B24",  width=420, height=40)
canvas2.pack(anchor=N, expand=0, fill=X)

canvas3=Canvas(bg="#201B24",  width=420, height=200,scrollregion=(0,0,5000,5000))
vbar=Scrollbar(canvas3, orient=VERTICAL)
vbar.pack(anchor=E,expand=1,fill=Y)
vbar.config(command=canvas3.yview)
canvas3.config(yscrollcommand=vbar.set)
canvas3.pack(anchor=CENTER,expand=1,fill=BOTH)

canvas3.create_line(100,0,100,5000,fill=colorID, width=3, dash = (10, 10))
canvas3.create_line(260,0,260,5000,fill=colorID, width=3, dash = (10, 10))

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


def main_draw_func(event):
    canvas3.update()
    global coefficient_x
    coefficient_x = root.winfo_width() / 420
    print(coefficient_x)

    def time_to_x(x):
        times = [19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for d in range(1, 20):
            if x == times[d]:
                return (20 * d + 20) * coefficient_x

    output_x1list = [time_to_x(int(''.join(sublist_x1))) for sublist_x1 in x1list]
    output_x2list = [time_to_x(int(''.join(sublist_x2))) for sublist_x2 in x2list]
    output_ylist = [int(''.join(sublist_y)) for sublist_y in ylist]

    canvas1.delete('all')
    canvas2.delete('all')
    canvas3.delete('all')

    canvas1.create_text(210*coefficient_x, 20, font="Itim 20", anchor='center', text="Sleepy log", fill=colorID_High)

    canvas2.create_text(20*coefficient_x, 20, font="Itim 10", anchor='center', text="19", fill=colorID)
    canvas2.create_text(40*coefficient_x, 20, font="Itim 10", anchor='center', text="20", fill=colorID)
    canvas2.create_text(60*coefficient_x, 20, font="Itim 10", anchor='center', text="21", fill=colorID)
    canvas2.create_text(80*coefficient_x, 20, font="Itim 10", anchor='center', text="22", fill=colorID)
    canvas2.create_text(100*coefficient_x, 20, font="Itim 10", anchor='center', text="23", fill=colorID_High)
    canvas2.create_text(120*coefficient_x, 20, font="Itim 10", anchor='center', text="00", fill=colorID)
    canvas2.create_text(140*coefficient_x, 20, font="Itim 10", anchor='center', text="01", fill=colorID)
    canvas2.create_text(160*coefficient_x, 20, font="Itim 10", anchor='center', text="02", fill=colorID)
    canvas2.create_text(180*coefficient_x, 20, font="Itim 10", anchor='center', text="03", fill=colorID)
    canvas2.create_text(200*coefficient_x, 20, font="Itim 10", anchor='center', text="04", fill=colorID)
    canvas2.create_text(220*coefficient_x, 20, font="Itim 10", anchor='center', text="05", fill=colorID)
    canvas2.create_text(240*coefficient_x, 20, font="Itim 10", anchor='center', text="06", fill=colorID)
    canvas2.create_text(260*coefficient_x, 20, font="Itim 10", anchor='center', text="07", fill=colorID_High)
    canvas2.create_text(280*coefficient_x, 20, font="Itim 10", anchor='center', text="08", fill=colorID)
    canvas2.create_text(300*coefficient_x, 20, font="Itim 10", anchor='center', text="09", fill=colorID)
    canvas2.create_text(320*coefficient_x, 20, font="Itim 10", anchor='center', text="10", fill=colorID)
    canvas2.create_text(340*coefficient_x, 20, font="Itim 10", anchor='center', text="11", fill=colorID)
    canvas2.create_text(360*coefficient_x, 20, font="Itim 10", anchor='center', text="12", fill=colorID)
    canvas2.create_text(380*coefficient_x, 20, font="Itim 10", anchor='center', text="13", fill=colorID)
    canvas2.create_text(400*coefficient_x, 20, font="Itim 10", anchor='center', text="14", fill=colorID)

    canvas3.create_line(100*coefficient_x, 0, 100*coefficient_x, 5000, fill=colorID, width=3, dash=(10, 10))
    canvas3.create_line(260*coefficient_x, 0, 260*coefficient_x, 5000, fill=colorID, width=3, dash=(10, 10))

    for dayvalueMAIN in range(len(output_ylist)):
        box_draw_back(output_x1list[dayvalueMAIN],output_x2list[dayvalueMAIN],day_to_y(output_ylist[dayvalueMAIN]))

    for dayvalueMAIN in range(len(output_ylist)):
        box_draw(output_x1list[dayvalueMAIN],output_x2list[dayvalueMAIN],day_to_y(output_ylist[dayvalueMAIN]))

canvas3.bind("<Configure>",main_draw_func)

def clear_all():
    clear_root = Tk()
    clear_root.title("warning!")
    clear_root.geometry('460x150')
    clear_root.resizable(width=0, height=0)

    clear_text=Label(clear_root, text="all your logs WILL BE DELETED, do u understand that?", font="Itim 12")
    clear_text.pack(expand=1)
    clear_button=Button(clear_root, text="yes, i understand", font="Itim 12", command=clear_all_really)
    clear_button.pack(expand=1)


def clear_all_really():
    #очистка всех файлов
    with open('sleepylognight.txt', 'w'):
        pass
    with open('sleepylogday.txt', 'w'):
        pass
    with open('currentday.txt', 'w') as file:
        file.write('0')
    exit()

canvas4=Canvas(bg="#201B24",  width=420, height=50)
canvas4.pack(anchor=N,expand=0, fill=X)

btn = ttk.Button(text="clear_all",command=clear_all)
canvas4.create_window(10, 10, anchor=NW, window=btn, width=100, height=30)

root.mainloop()
