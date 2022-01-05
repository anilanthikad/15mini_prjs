from tkinter import *
from tkcalendar import *


root = Tk()
root.title('calendar')
root.geometry('600x400')

cal = Calendar(root, year=2022, month=4, day=15)
cal.pack(pady=70)

root.mainloop()
