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
root.minsize(420,200)

pyglet.font.add_file('Itim-Regular.ttf')

coefficient_x=0
times = [19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

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

def time_to_index(x):
    for d in range(1, 20):
        if x == times[d]:
            return d

def average_sleep_time_func():
    delta_day = []
    indexed_x1 =[]
    indexed_x2 =[]

    output1_x1list = [int(''.join(sublist1_x1)) for sublist1_x1 in x1list]
    output1_x2list = [int(''.join(sublist1_x2)) for sublist1_x2 in x2list]

    for i in range(len(output1_x1list)):
        indexed_x1.append(time_to_index(output1_x1list[i]))
        indexed_x2.append(time_to_index(output1_x2list[i]))

    for delta in range(len(output1_x1list)):
        delta_day.append(indexed_x2[delta]-indexed_x1[delta])

    if sum(delta_day) > 0:
        return round(sum(delta_day) / len(delta_day), 4)
    else:
        return 0

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

canvas4=Canvas(bg="#201B24",  width=420, height=50)
canvas4.pack(anchor=N,expand=0, fill=X)

text_average_sleep_time=canvas4.create_text(200*coefficient_x, 20, text=f'average sleep time: {average_sleep_time_func()}', anchor=E, fill=colorID, font="Itim 10")

btn = ttk.Button(text="clear_all",command=clear_all)
canvas4.create_window(10, 10, anchor=NW, window=btn, width=100, height=30)

def main_draw_func(event):
    canvas3.update()
    global coefficient_x
    coefficient_x = root.winfo_width() / 420
    print(coefficient_x)

    def time_to_x(x):
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

    time_text = ['19','20','21','22','23','00','01','02','03','04','05','06','07','08','09','10','11','12','13','14']
    for canvas2_time_text_number in range(len(time_text)):
        if time_text[canvas2_time_text_number]=='23' or time_text[canvas2_time_text_number]=='07':
            canvas2.create_text((canvas2_time_text_number * 20 + 20) * coefficient_x, 20, font="Itim 10", anchor='center', text=time_text[canvas2_time_text_number], fill=colorID_High)
        else: canvas2.create_text((canvas2_time_text_number*20+20)* coefficient_x, 20, font="Itim 10", anchor='center', text=time_text[canvas2_time_text_number], fill=colorID)


    canvas3.create_line(100*coefficient_x, 0, 100*coefficient_x, 5000, fill=colorID, width=3, dash=(10, 10))
    canvas3.create_line(260*coefficient_x, 0, 260*coefficient_x, 5000, fill=colorID, width=3, dash=(10, 10))

    for dayvalueMAIN in range(len(output_ylist)):
        box_draw_back(output_x1list[dayvalueMAIN],output_x2list[dayvalueMAIN],day_to_y(output_ylist[dayvalueMAIN]))

    for dayvalueMAIN in range(len(output_ylist)):
        box_draw(output_x1list[dayvalueMAIN],output_x2list[dayvalueMAIN],day_to_y(output_ylist[dayvalueMAIN]))

    canvas4.coords(text_average_sleep_time, 400*coefficient_x, 20)

canvas3.bind("<Configure>",main_draw_func)

root.mainloop()