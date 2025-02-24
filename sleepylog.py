from tkinter import *
from tkinter import ttk
import tkinter as tk
import pyglet
import json

color_gray = '#555258'
color_almost_white_id = '#F0F0F0'
color_canvas_id = '#201B24'
color_box_id = '#422C4B'
color_box_outline_id = '#D474F2'
color_button_bg='#322939'

root = Tk()
root.title("sleepylog")
root.geometry('700x540')
root.resizable(width=1, height=1)
root.minsize(670,440)

style = ttk.Style()
style.theme_use('clam')
style.configure("Vertical.TScrollbar", gripcount=0,
                background=color_gray, darkcolor=color_canvas_id, lightcolor=color_canvas_id,
                troughcolor=color_canvas_id, bordercolor=color_canvas_id, arrowcolor=color_canvas_id)
style.configure("TFrame", background=color_canvas_id)
style.configure('TSpinbox',
                relief="flat")

pyglet.font.add_file('Itim-Regular.ttf')

coefficient_x=0
time_int_values = [19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 0, 0.5,
                   1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5,
                   8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5,
                   14, 14.5]
begin_time_str_values = ["19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30",
               "23:00", "23:30", "00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00",
               "03:30", "04:00"]
stop_time_str_values = ["04:30", "05:00", "05:30", "06:00", "06:30", "07:00",
               "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00",
               "11:30", "12:00", "12:30", "13:00", "13:30", "14:00"]

def day_to_y(day):
    y1=day*20+3
    y0=y1-20
    return f'{y0},{y1}'

def box_draw(x0,x1,y):
    y=y.split(',')
    y0=y[0]
    y1 = y[1]
    canvas3.create_rectangle(x0, y0, x1, y1, fill=color_box_id, width=0)

def box_draw_back(x0,x1,y):
    y=y.split(',')
    y0=int(y[0])
    y1=int(y[1])
    canvas3.create_rectangle(x0 - 3, y0 - 3, x1 + 3, y1 + 3, fill=color_box_outline_id, width=0)

def clear_all():
    clear_root = Tk()
    clear_root.title("warning!")
    clear_root.geometry('460x150')
    clear_root.resizable(width=0, height=0)

    def clear_all_really():
        with open('data.json', 'w') as file:
            json.dump([{}], file)
        delayed_draw(event=None)
        clear_root.destroy()

    clear_text=Label(clear_root, text="all your logs WILL BE DELETED, do u understand that?", font="Itim 12")
    clear_text.pack(expand=1)
    clear_button=Button(clear_root, text="yes, i understand", font="Itim 12", command=clear_all_really)
    clear_button.pack(expand=1)

def go_func():
    with open('data.json', 'r') as file:
        data = json.loads(file.read())
        last_item = data[0]
        try:
            last_day_number = max(last_item.keys(), key=int)
            last_day = last_item[last_day_number]["day"]
        except ValueError:
            last_day = 0

    day=int(last_day)+1
    begin_time=begin_time_spinbox.get()
    stop_time=stop_time_spinbox.get()

    to_json = {f"{day}": {"day": day, "begin": begin_time, "stop": stop_time}}

    try:
        with open('data.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    if existing_data:
        existing_data[0].update(to_json)
    else:
        existing_data.append(to_json)

    with open('data.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

def average_sleep_time_func():
    delta_day = []
    indexed_x1 = []
    indexed_x2 = []
    output_x1_list_local=[]
    output_x2_list_local=[]
    output_y_list = []
    x1_list = []
    x2_list = []

    def time_to_index(x):
        for d in range(1, 39):
            if x == time_int_values[d]:
                return d

    def time_to_output_x1_local():
        for day in range(len(output_y_list)):
            for time in range(25):
                if x1_list[day][0] == time and x1_list[day][1] == 0:
                    output_x1_list_local.append(time)
                if x1_list[day][0] == time and x1_list[day][1] == 1:
                    output_x1_list_local.append(time + 0.5)

    def time_to_output_x2_local():
        for day in range(len(output_y_list)):
            for time in range(25):
                if x2_list[day][0] == time and x2_list[day][1] == 0:
                    output_x2_list_local.append(time)
                if x2_list[day][0] == time and x2_list[day][1] == 1:
                    output_x2_list_local.append(time + 0.5)

    with open('data.json', 'r') as data_file:
        data = json.loads(data_file.read())
        for i in range(1, len(data[0]) + 1):
            time_str_x1 = data[0][f"{i}"]["begin"]
            hours, minutes = time_str_x1.split(":")
            if minutes == '30': minutes = minutes.replace('30', '1')
            x1_list.append([int(hours), int(minutes)])

    with open('data.json', 'r') as data_file:
        data = json.loads(data_file.read())
        for i in range(1, len(data[0]) + 1):
            time_str_x2 = data[0][f"{i}"]["stop"]
            hours, minutes = time_str_x2.split(":")
            if minutes == '30': minutes = minutes.replace('30', '1')
            x2_list.append([int(hours), int(minutes)])

    with open('data.json', 'r') as data_file:
        data = json.loads(data_file.read())
        for i in range(1, len(data[0]) + 1):
            day_str = data[0][f"{i}"]["day"]
            output_y_list.append(int(day_str))

    time_to_output_x1_local()
    time_to_output_x2_local()

    for i in range(len(output_y_list)):
        indexed_x1.append(time_to_index(output_x1_list_local[i]))
        indexed_x2.append(time_to_index(output_x2_list_local[i]))

    for delta in range(len(output_y_list)):
        delta_day.append(indexed_x2[delta] - indexed_x1[delta])

    if sum(delta_day) > 0:
        return f"{round(sum(delta_day) / len(delta_day)/2, 3):.3f}"
    else:
        return '0.000'

frame_input=ttk.Frame(width=300)
frame_input.pack(side = LEFT ,expand=0,fill=Y)

text_sleepy_log=Label(frame_input, font="Itim 20", text="Sleepy log", fg=color_almost_white_id, bg=color_canvas_id)
text_sleepy_log.pack(anchor=NW, padx=3, pady=0)

text_tonight=Label(frame_input, font="Itim 14", text="tonight i slept...", fg=color_almost_white_id, bg=color_canvas_id)
text_tonight.pack(anchor=N, fill=X)

frame_from_to=ttk.Frame(frame_input,width=300)
frame_from_to.pack()

text_from=Label(frame_from_to, font="Itim 14", text="from", fg=color_almost_white_id, bg=color_canvas_id)
text_from.pack(side="left", padx=3)

begin_time_spinbox = ttk.Spinbox(frame_from_to, values=begin_time_str_values, state="readonly", width=5, font='Itim 12')
begin_time_spinbox.pack(side="left", padx=3)
begin_time_spinbox.set("23:00")

text_from=Label(frame_from_to, font="Itim 14", text="to", fg=color_almost_white_id, bg=color_canvas_id)
text_from.pack(side="left", padx=3)

stop_time_spinbox = ttk.Spinbox(frame_from_to, values=stop_time_str_values, state="readonly", width=5, font='Itim 12')
stop_time_spinbox.pack(side="left", padx=3)
stop_time_spinbox.set("07:00")

button_go=tk.Button(frame_input,text="lets go!",command=go_func,relief='flat',bg=color_button_bg,fg=color_almost_white_id,font=("Itim", 12),width=20)
button_go.pack(pady=5)

canvas1_2=Canvas(frame_input,bg=color_canvas_id,  width=300, height=300,highlightthickness=0)
canvas1_2.pack(side=BOTTOM, expand=0, fill=X)

image_tv = tk.PhotoImage(file="tv.png")
canvas1_2.create_image(5,37,image=image_tv, anchor=NW)

faq_button = tk.Button(text="FAQ",relief='flat',bg=color_button_bg,fg=color_almost_white_id,font=("Itim", 12))
canvas1_2.create_window(5, 260, anchor=NW, window=faq_button, width=142, height=34)
clear_button = tk.Button(text="clear all",command=clear_all,relief='flat',bg=color_button_bg,fg=color_almost_white_id,font=("Itim", 12))
canvas1_2.create_window(153, 260, anchor=NW, window=clear_button, width=142, height=34)

frame_main=ttk.Frame()
frame_main.pack(side = RIGHT , expand=1,fill=BOTH)

canvas2=Canvas(frame_main,bg=color_canvas_id,  width=420, height=40,highlightthickness=0)
canvas2.pack(anchor=N, expand=0, fill=X)

canvas3=Canvas(frame_main,bg=color_canvas_id,  width=420, height=200,scrollregion=(0,0,5000,5000),highlightthickness=0)
vbar=ttk.Scrollbar(canvas3, orient=VERTICAL)
vbar.pack(anchor=E,expand=1,fill=Y)
vbar.config(command=canvas3.yview)
canvas3.config(yscrollcommand=vbar.set)
canvas3.pack(anchor=CENTER,expand=1,fill=BOTH)

canvas3.create_line(100, 0, 100, 5000, fill=color_gray, width=3, dash = (10, 10))
canvas3.create_line(260, 0, 260, 5000, fill=color_gray, width=3, dash = (10, 10))
text_statistics=canvas1_2.create_text(75, 160,
                                            text='statistics:',
                                            anchor=NW, fill=color_box_outline_id, font="Itim 11")
canvas1_2.create_text(40, 178,
                      text=f'average sleep time: {average_sleep_time_func()}',
                      anchor=NW, fill=color_almost_white_id, font="Itim 10",tags="text_average_sleep_time")


def main_draw_func(event):
    canvas3.update()
    global coefficient_x
    coefficient_x = canvas3.winfo_width() / 420
    print(coefficient_x)
    global text_average_sleep_time

    def time_to_x(x):
        for d in range(1, 39):
            if x == time_int_values[d]:
                return (10 * d + 20) * coefficient_x

    def time_to_output_x1():
        for day in range(len(output_y_list)):
            for time in range(25):
                if x1_list[day][0] == time and x1_list[day][1] == 0:
                    output_x1_list.append(time_to_x(time))
                if x1_list[day][0] == time and x1_list[day][1] == 1:
                    output_x1_list.append(time_to_x(time + 0.5))

    def time_to_output_x2():
        for day in range(len(output_y_list)):
            for time in range(25):
                if x2_list[day][0] == time and x2_list[day][1] == 0:
                    output_x2_list.append(time_to_x(time))
                if x2_list[day][0] == time and x2_list[day][1] == 1:
                    output_x2_list.append(time_to_x(time + 0.5))

    x1_list = []
    x2_list = []

    output_x1_list = []
    output_x2_list = []
    output_y_list = []

    with open('data.json', 'r') as data_file:
        data = json.loads(data_file.read())
        for i in range(1, len(data[0]) + 1):
            time_str_x1 = data[0][f"{i}"]["begin"]
            hours, minutes = time_str_x1.split(":")
            if minutes == '30': minutes = minutes.replace('30', '1')
            x1_list.append([int(hours), int(minutes)])

    with open('data.json', 'r') as data_file:
        data = json.loads(data_file.read())
        for i in range(1, len(data[0]) + 1):
            time_str_x2 = data[0][f"{i}"]["stop"]
            hours, minutes = time_str_x2.split(":")
            if minutes == '30': minutes = minutes.replace('30', '1')
            x2_list.append([int(hours), int(minutes)])

    with open('data.json', 'r') as data_file:
        data = json.loads(data_file.read())
        for i in range(1, len(data[0]) + 1):
            day_str = data[0][f"{i}"]["day"]
            output_y_list.append(int(day_str))

    time_to_output_x1()
    time_to_output_x2()

    canvas1_2.delete('text_average_sleep_time')
    canvas2.delete('all')
    canvas3.delete('all')

    time_text = ['19', '20', '21', '22', '23', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                 '11', '12', '13', '14']
    for canvas2_time_text_number in range(len(time_text)):
        if time_text[canvas2_time_text_number] == '23' or time_text[canvas2_time_text_number] == '07':
            canvas2.create_text((canvas2_time_text_number * 20 + 20) * coefficient_x, 20, font="Itim 10",
                                anchor='center', text=time_text[canvas2_time_text_number],
                                fill=color_almost_white_id)
        else:
            canvas2.create_text((canvas2_time_text_number * 20 + 20) * coefficient_x, 20, font="Itim 10",
                                anchor='center', text=time_text[canvas2_time_text_number], fill=color_gray)

    canvas3.create_line(100 * coefficient_x, 0, 100 * coefficient_x, 5000, fill=color_gray, width=3, dash=(10, 10))
    canvas3.create_line(260 * coefficient_x, 0, 260 * coefficient_x, 5000, fill=color_gray, width=3, dash=(10, 10))
    canvas3.create_line(2, 0, 2, 5000, fill=color_button_bg, width=3)
    canvas2.create_line(2, 0, 2, 100, fill=color_button_bg, width=3)

    for day_value_draw_back in range(len(output_y_list)):
        box_draw_back(output_x1_list[day_value_draw_back],
                      output_x2_list[day_value_draw_back],
                      day_to_y(output_y_list[day_value_draw_back]))

    for day_value_draw in range(len(output_y_list)):
        box_draw(output_x1_list[day_value_draw],
                 output_x2_list[day_value_draw],
                 day_to_y(output_y_list[day_value_draw]))
    canvas1_2.create_text(40, 178,text=f'average sleep time: {average_sleep_time_func()}',
                          anchor=NW, fill=color_almost_white_id, font="Itim 10",tags="text_average_sleep_time")

def delayed_draw(event):
    canvas3.after(100, main_draw_func, event)

canvas3.bind("<Configure>", main_draw_func)
root.bind("<Button-1>", delayed_draw)

root.mainloop()