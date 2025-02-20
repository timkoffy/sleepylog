from fileinput import close
from locale import windows_locale
from tkinter import *
from tkinter import ttk

def skipdef():
    import os
    os.system('sleepylog_main.py')
    import sys
    sys.exit(0)

def godef():
    night_value = entrynight.get()
    with open('sleepylognight.txt', 'a') as sleepylognight: sleepylognight.write(night_value + '\n')

    day_value = entryday.get()
    with open('sleepylogday.txt', 'a') as sleepylogday: sleepylogday.write(day_value + '\n')

    currentday_count = open("currentday.txt", 'r')
    last_currentdayvalue = currentday_count.readlines()[-1]
    g = str(int(last_currentdayvalue) + 1)
    with open('currentday.txt', 'a') as currentday:
        currentday.write('\n' + g)
    currentday_count.close()

    skipdef()

root = Tk()
root.title("sleepylog")
root.resizable(width=False, height=False)

Label(text="today i slept...").grid(row=0, column=0, sticky=NW, padx=10, pady=5)

Label(text="from:").grid(row=1, column=0, sticky=E, padx=10, pady=5)

entrynight = ttk.Entry(width=7)
entrynight.grid(row=1, column=1, padx=10)

Label(text="to:").grid(row=1, column=2, sticky=E)

entryday = ttk.Entry(width=7)
entryday.grid(row=1, column=3, padx=10)

Button(text="lets go!",command=godef).grid(row=2, column=2, pady=5)
Button(text="skip",command=skipdef).grid(row=2, column=3, padx=10)

root.mainloop()