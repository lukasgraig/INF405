import tkinter as tk
from Clock import *

clock = Clock()

screen = tk.Tk()
screen.title("Clock GUI")
screen.geometry("700x500")

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December']

# // MONTH LABEL AND LIST BOX

label1=tk.Label(screen, text="Month")
label1.place(relx=.13, rely= .1)
scroll_bar_month = tk.Scrollbar(screen, orient="vertical")
monthsbox = tk.Listbox(screen, width = 11, exportselection = 0,
        selectmode="single", yscrollcommand = scroll_bar_month.set)
monthsbox.select_set(0)

for x in range(len(months)):
    monthsbox.insert("end",months[x])
monthsbox.select_set(0)

scroll_bar_month = tk.Scrollbar(screen ,orient="vertical")
scroll_bar_month.config(command=monthsbox.yview)

monthsbox.place(relx=.11, rely=.15)
scroll_bar_month.place(relx=.2, rely=.25)

# // DAY LABEL AND LIST BOX

label2=tk.Label(screen, text="Day")
label2.place(relx=.3, rely= .1)

scroll_bar_day = tk.Scrollbar(screen, orient="vertical")
daysbox = tk.Listbox(screen, width = 4, exportselection = 0,
        selectmode="single", yscrollcommand = scroll_bar_day.set)
daysbox.select_set(0)

for day in range(1, 32):
    daysbox.insert("end", day)

scroll_bar_day = tk.Scrollbar(screen ,orient="vertical")
scroll_bar_day.config(command=daysbox.yview)

daysbox.place(relx=.3, rely=.15)
scroll_bar_day.place(relx=.33, rely=.25)

# // YEAR  LABEL AND LIST BOX

label3=tk.Label(screen, text="Year")
label3.place(relx=.4, rely= .1)

scroll_bar_year = tk.Scrollbar(screen, orient="vertical")
yearsbox = tk.Listbox(screen, width = 6, exportselection = 0,
        selectmode="single", yscrollcommand = scroll_bar_year.set)
yearsbox.select_set(0)

for year in range(1900, 2101):
    yearsbox.insert("end", year)

scroll_bar_year = tk.Scrollbar(screen ,orient="vertical")
scroll_bar_year.config(command=yearsbox.yview)

yearsbox.place(relx=.4, rely=.15)
scroll_bar_year.place(relx=.44, rely=.25)


# // HOUR LABEL AND LIST BOX
label4=tk.Label(screen, text="Hour")
label4.place(relx=.5, rely= .1)

scroll_bar_hour = tk.Scrollbar(screen, orient="vertical")
hoursbox = tk.Listbox(screen, width = 6, exportselection = 0,
        selectmode="single", yscrollcommand = scroll_bar_year.set)
hoursbox.select_set(0)

for hour in range(0, 24):
    hoursbox.insert("end", hour)

scroll_bar_hour = tk.Scrollbar(screen ,orient="vertical")
scroll_bar_hour.config(command=hoursbox.yview)

hoursbox.place(relx=.5, rely=.15)
scroll_bar_hour.place(relx=.55, rely=.25)


# // MINUTE LABEL AND LIST BOX
label4=tk.Label(screen, text="Minute")
label4.place(relx=.6, rely= .1)

scroll_bar_minute = tk.Scrollbar(screen, orient="vertical")
hoursbox = tk.Listbox(screen, width = 6, exportselection = 0,
        selectmode="single", yscrollcommand = scroll_bar_minute.set)
hoursbox.select_set(0)

for minute in range(0, 24):
    hoursbox.insert("end", minute)

scroll_bar_minute = tk.Scrollbar(screen ,orient="vertical")
scroll_bar_minute.config(command=hoursbox.yview)

hoursbox.place(relx=.5, rely=.15)
scroll_bar_minute.place(relx=.55, rely=.25)


# // SECOND LABEL AND LIST BOX
label4=tk.Label(screen, text="Second")
label4.place(relx=.7, rely= .1)


quitbutton=tk.Button(screen,text="Quit",command=screen.destroy)
quitbutton.place(relx=.58, rely=.8)

scroll_bar = tk.Scrollbar(screen,orient="vertical")
sportsbox=tk.Listbox(screen,width=14,exportselection=0,selectmode="single",
                     yscrollcommand = scroll_bar.set)




screen.mainloop()
