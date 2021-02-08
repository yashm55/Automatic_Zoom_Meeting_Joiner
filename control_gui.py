
#  Importing necessary libraries , bot and database.
from sqlite3.dbapi2 import Cursor
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import tkinter as tk
import live_date
from PIL import Image, ImageTk, ImageOps
import bot
import database
import sqlite3
import webbrowser
from datetime import datetime
import time

conn = sqlite3.connect("automate_zoom.db")

firsttime = True

status = True



# Fetches current time. 

status_label_text = ""

def live_time():
    current_time = live_date.get_current_time()
    timeLabel.config(text = current_time)
    root.after(1000, live_time)


# Updates database and keeps bot running so as to constantly get updates and store them approprietly.
def update_db():
    global status_label_text
    global firsttime
    if firsttime == True:
        status_label_text = "Bot is Running..."
        update_status()
        firsttime = False
    status1 = bot.run_bot(running = status)
    if status1 != "Empty":
        status_label_text = status1
    root.after(5000, update_db)


# Checks the time grabbed from the Zoom meeting details messages and compares it to current time, if any time grabbed is exactly
# equal to current time, then this function opens the zoom link associated with that time. 
def check_time():
    current_datetime = live_date.get_current_datetime()
    cursor = conn.execute("SELECT * FROM meeting_details")
    result = cursor.fetchall()
    for row in result:
        if row[3] == current_datetime:
            webbrowser.open(row[2])
            database.clear_row(row[1])
    root.after(5000, check_time)
        

# Function to clear the entire schedule from the database.
def clear_schedule():
    global status_label_text
    status_label_text =  database.clear_table()


# Function for the GUI button "Stop Bot", which when pressed, stops the bot from grabbing new messages and details and storing 
# them in the database.
def stop_bot():
    global status
    global status_label_text
    status = False
    stopBot.config(text = """Start
Bot""")
    status_label_text =  "Bot is Not Running..."
    stopBot.config(command = start_bot)


# Function for the GUI button "Start Bot", which when pressed, allows the bot to grab new messages and details and then stores
# them in the local database.
def start_bot():
    global status
    global status_label_text
    status = True
    stopBot.config(text = """Stop
Bot""")
    status_label_text =  "Bot is Running..."
    stopBot.config(command = stop_bot)


# Function for the GUI button "Close"(which appears after you press, the GUI button "Todays Schedule") which closes the Todays
# Schedule pane, and shows the default logo.
def close_func():
    image1 = ImageTk.PhotoImage(Image.open("Automating_zoom.png"))
    imageLabel.place(x = 117, y = 10, height = 195, width = 340)
    seeSchedule.config(text = """Today's
Schedule""", command=todays_schedule)
    deleteMeeting.config(text = """Delete
Meeting""", command=delete_meeting)
    delete.place_forget()
    edit.place_forget()

last_index = 0


# Fetches all the meeting details(messages read by the bot during it was running) from the database, and shows it in a new pane, 
# instead of the app logo.
def todays_schedule():
    global last_index
    Cursor = conn.execute("SELECT * FROM meeting_details")
    result = Cursor.fetchall()
    x = 0
    main_list.delete(x, last=last_index)
    for row in result:
        content = row[1]+"|"+row[3]
        main_list.insert(x, content)
        x += 1
        last_index = x
    imageLabel.place_forget()
    seeSchedule.config(text = "close", command=close_func)
    edit.place(x = 7, y = 60, height = 40, width = 100)


# Function to show a new window for editing meeting time.
def OpenEdit_window():
    selected = ()
    try:
        selected = main_list.get(main_list.curselection()[0])
        splitted = selected.split('|')
    except:
        pass
        

    if len(selected) != 0: 
        newWindow = Toplevel(root)
        newWindow.title("Edit Meeting")
        newWindow.geometry("350x300")
        newWindow.resizable(0, 0)

        l = Label(newWindow, text = """Enter the time in the same format as that in the zoom messages.""" , fg = "Red")
        l2 = Label(newWindow, text = "Year:")
        l3 = Label(newWindow, text = "Month:")
        l4 = Label(newWindow, text = "Day:")
        l5 = Label(newWindow, text = "Time:")
        e = Entry(newWindow, width = 15, borderwidth = 5)
    
    

    
        rn = datetime.now()
        Month = rn.month

        Mo = tk.StringVar()
        MonthChosen = ttk.Combobox(newWindow, width = 10, textvariable = Mo)

        if Month ==1:
            MonthChosen['values'] = ('Jan')

        elif Month ==2:
            MonthChosen['values'] = ('Feb')

        elif Month ==3:
            MonthChosen['values'] = ('Mar')

        elif Month ==4:
            MonthChosen['values'] = ('Apr')

        elif Month ==5:
            onthChosen['values'] = ('May')

        elif Month ==6:
            MonthChosen['values'] = ('Jun')

        elif Month ==7:
            MonthChosen['values'] = ('Jul')

        elif Month ==8:
            MonthChosen['values'] = ('Aug')
    
        elif Month ==9:
            MonthChosen['values'] = ('Sep')

        elif Month ==10:
            MonthChosen['values'] = ('Oct')
    
        elif Month ==11:
            MonthChosen['values'] = ('Nov')

        elif Month ==12:
            MonthChosen['values'] = ('Dec')
    
        MonthChosen.current(0)

    
        n = tk.StringVar()
        dayChosen = ttk.Combobox(newWindow, width = 10, textvariable = n)

        if Month == 1:

            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28', 
                                '29', 
                                '30', 
                                '31')
        
        elif Month == 2:

            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28')
    
        elif Month ==3:
            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')

        elif Month ==4:
            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30')
    
        elif Month ==5:
            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')

        elif Month ==6:
            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30')

        elif Month ==7:
            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')

        elif Month ==8:
            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')

        elif Month ==9:
            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30')

        elif Month ==10:
            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')

        elif Month ==11:
            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30')

        elif Month ==12:
            dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')
        dayChosen.current(0)

    
        m = tk.StringVar()
        amPm = ttk.Combobox(newWindow, width = 5, textvariable = m)
        amPm['values'] = ('AM',
                      'PM')
        amPm.current(0)

        year = rn.year
        y = tk.StringVar()
        yearChosen = ttk.Combobox(newWindow, width = 10, textvariable = y)
        yearChosen['values'] = (year)
        yearChosen.current(0)
    else:
        messagebox.showwarning("Select meeting", "You have to select a meeting to use this function.")

    def save():
        month = MonthChosen.get()    
        Day = dayChosen.get()
        edited_time = e.get()
        meridiem = amPm.get()

        edited_schedule = f"{month} {Day}, {year} {edited_time} {meridiem}"
        print(selected)
        # cursor = conn.execute("SELECT * FROM meeting_details")
        if len(edited_time) != 0:
            cursor = conn.execute("UPDATE meeting_details SET meeting_time = ? WHERE meeting_time = ?", (edited_schedule, splitted[1]))
            conn.commit()
            newWindow.destroy()
            global last_index
            Cursor = conn.execute("SELECT * FROM meeting_details")
            result = Cursor.fetchall()
            x = 0
            main_list.delete(x, last=last_index)
            for row in result:
                content = row[1]+"|"+row[3]
                main_list.insert(x, content)
                x += 1
            last_index = x
        else:
            messagebox.showwarning("Enter time", "You cannot save without entering time.")
    
    save = Button(newWindow, text = "Save", width = 20, borderwidth = 5, command = save)

    

    l.place(x = 0, y = 0)
    l2.place(x = 20, y = 40)
    yearChosen.place(x = 70, y = 40)
    l3.place(x = 20, y = 90)
    MonthChosen.place(x = 70, y = 90)
    l4.place(x= 20, y=130)
    dayChosen.place(x= 70, y = 130)
    l5.place(x=20, y=190)
    e.place(x =70, y = 190)
    amPm.place(x=190, y=190)
    save.place(x = 40, y = 240)
    
    newWindow.mainloop()


#  Function for a button "Add", which let's you add a meeting, directly through the program itself.
def add():
    newAddWindow = Toplevel(root)
    newAddWindow.title("Add Meeting")
    newAddWindow.geometry("500x400")
    newAddWindow.resizable(0, 0)

    l = Label(newAddWindow, text = """Enter the time in the same format as that in the zoom messages.""" , fg = "Red")
    l2 = Label(newAddWindow, text = "Topic:")
    l3 = Label(newAddWindow, text = "Link:")
    l4 = Label(newAddWindow, text = "Year:")
    l5 = Label(newAddWindow, text = "Month:")
    l6 =Label(newAddWindow, text = "Day:")
    l7 = Label(newAddWindow, text = "Time:")
    ti = Entry(newAddWindow, width = 15, borderwidth = 5)
    to = Entry(newAddWindow, width = 20, borderwidth = 5)
    li = Entry(newAddWindow, width = 30, borderwidth = 5)
    
    

    
    rn = datetime.now()
    Month = rn.month

    Mo = tk.StringVar()
    MonthChosen = ttk.Combobox(newAddWindow, width = 10, textvariable = Mo)

    if Month ==1:
        MonthChosen['values'] = ('Jan')

    elif Month ==2:
        MonthChosen['values'] = ('Feb')

    elif Month ==3:
        MonthChosen['values'] = ('Mar')

    elif Month ==4:
        MonthChosen['values'] = ('Apr')

    elif Month ==5:
        MonthChosen['values'] = ('May')

    elif Month ==6:
        MonthChosen['values'] = ('Jun')

    elif Month ==7:
        MonthChosen['values'] = ('Jul')

    elif Month ==8:
        MonthChosen['values'] = ('Aug')
    
    elif Month ==9:
        MonthChosen['values'] = ('Sep')

    elif Month ==10:
        MonthChosen['values'] = ('Oct')
    
    elif Month ==11:
        MonthChosen['values'] = ('Nov')

    elif Month ==12:
        MonthChosen['values'] = ('Dec')
    
    MonthChosen.current(0)

    
    n = tk.StringVar()
    dayChosen = ttk.Combobox(newAddWindow, width = 10, textvariable = n)

    if Month == 1:

        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28', 
                                '29', 
                                '30', 
                                '31')
        
    elif Month == 2:

        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28')
    
    elif Month ==3:
        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')

    elif Month ==4:
        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30')
    
    elif Month ==5:
        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')

    elif Month ==6:
        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30')

    elif Month ==7:
        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')

    elif Month ==8:
        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')

    elif Month ==9:
        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30')

    elif Month ==10:
        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')

    elif Month ==11:
        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30')

    elif Month ==12:
        dayChosen['values'] = ('1', 
                                '2', 
                                '3', 
                                '4', 
                                '5', 
                                '6', 
                                '7', 
                                '8', 
                                '9', 
                                '10', 
                                '11', 
                                '12', 
                                '13', 
                                '14', 
                                '15', 
                                '16', 
                                '17', 
                                '18', 
                                '19', 
                                '20', 
                                '21', 
                                '22', 
                                '23', 
                                '24', 
                                '25', 
                                '26', 
                                '27', 
                                '28',
                                '29',
                                '30',
                                '31')
    dayChosen.current(0)

    
    m = tk.StringVar()
    amPm = ttk.Combobox(newAddWindow, width = 5, textvariable = m)
    amPm['values'] = ('AM',
                      'PM')
    
    amPm.current(0)

    year = rn.year
    y = tk.StringVar()
    yearChosen = ttk.Combobox(newAddWindow, width = 10, textvariable = y)
    yearChosen['values'] = (year)
    yearChosen.current(0)

    def save():
        topic = to.get()
        link = li.get()
        month = MonthChosen.get()    
        Day = dayChosen.get()
        edited_time = ti.get()
        meridiem = amPm.get()

        edited_schedule = f"{month} {Day}, {year} {edited_time} {meridiem}"
        
        cursor = conn.execute("INSERT INTO meeting_details (topic, zoom_links, meeting_time) VALUES (?, ?, ?)", (topic, link, edited_schedule,))
        conn.commit()
        
        if topic and link and edited_time is not None:
            newAddWindow.destroy()
    save = Button(newAddWindow, text = "Add", width = 20, borderwidth = 5, command = save)

    l.place(x = 0,y = 0)
    l2.place(x = 20, y = 50)
    to.place(x = 70, y = 50)
    l3.place(x = 20, y = 100)
    li.place(x = 70, y = 100)
    l4.place(x = 20, y = 150)
    yearChosen.place(x = 70, y = 150)
    l5.place(x = 20, y = 200)
    MonthChosen.place(x = 70, y = 200)
    l6.place(x= 20, y=250)
    dayChosen.place(x= 70, y = 250)
    l7.place(x=20, y=300)
    ti.place(x =70, y = 300)
    amPm.place(x=200, y=300)
    save.place(x = 70, y = 330)
    newAddWindow.mainloop()




# Function for the GUI button "Delete Meetings" which allows the user to select the meeting from todays schedule(meeting details) 
# they want to delete from the database. 
def delete_meeting():
    global last_index
    Cursor = conn.execute("SELECT * FROM meeting_details")
    result = Cursor.fetchall()
    x = 0
    main_list.delete(x, last=last_index)
    for row in result:
        content = row[1]+"|"+row[3]
        main_list.insert(x, content)
        x += 1
        last_index = x
    imageLabel.place_forget()
    delete.place(x = 470, y = 60, height = 40, width = 100)
    deleteMeeting.config(text = "close", command=close_func)


# Function for the GUI button "Delete", which appears after the user selects the meeting they want to delete from todays schedule
# and allows the user to delete the selected meeting from that days schedule.
def delete():
    global status_label_text
    selected = main_list.get(main_list.curselection()[0])
    selected = selected.split("|") 
    database.clear_row(selected[0])
    status_label_text = f"Removed {selected[0]}"
    global last_index
    Cursor = conn.execute("SELECT * FROM meeting_details")
    result = Cursor.fetchall()
    x = 0
    main_list.delete(x, last=last_index)
    for row in result:
        content = row[1]+"|"+row[3]
        main_list.insert(x, content)
        x += 1
        last_index = x
    imageLabel.place_forget()



def update_status(check = True):
    global status_label_text
    statusLabel.config(text = status_label_text)
    root.after(1000, update_status)
    

# Code block for the GUI (Graphical User Interface)
if __name__ == '__main__':
    root = Tk()
    
    root.title("Automate Zoom")

    root.geometry("600x500")

    root.resizable(0, 0)

    # edit_window = Toplevel(root)
    # edit_window.geometry("100x100")

    root.wm_iconbitmap("Auto_zoom logo.ico")

    controllWindow = LabelFrame(root, text = "ScheduleControls")
    controllWindow.place(x = 10, y = 10, height = 230, width = 580)

    seeSchedule = Button(controllWindow, text = """Todays
Schedule""", command=todays_schedule)
    seeSchedule.place(x = 7, y = 10, height = 40, width = 100)
    Add = Button(controllWindow, text = "Add", command = add, borderwidth = 3)
    Add.place(x = 230, y = 160, height = 40, width = 100)
    edit = Button(controllWindow, text = "Edit", command = OpenEdit_window)
    clearSchedule = Button(controllWindow, text = """Clear Todays
schedule""", command=clear_schedule)
    clearSchedule.place(x = 7, y = 110, height = 40, width = 100)

    deleteMeeting = Button(controllWindow, text = """Delete
Meetings""", command=delete_meeting)
    deleteMeeting.place(x = 470, y = 10, height = 40, width = 100)

    stopBot = Button(controllWindow, text = """Stop
Bot""", command=stop_bot)
    stopBot.place(x = 470, y = 110, height = 40, width = 100)

    main_list = Listbox(controllWindow, selectmode = SINGLE)
    main_list.place(x = 117, y = 10, height = 145, width = 340)

    image1 = ImageTk.PhotoImage(Image.open("Automating_zoom.png"))
    imageLabel = Label(controllWindow, image = image1)
    imageLabel.place(x = 117, y = 10, height = 145, width = 340)

    delete = Button(controllWindow, text="Delete", command=delete)

    

    timeWindow = LabelFrame(root, text = "Time")
    timeWindow.place(x = 10, y = 240, height = 160, width = 580, )

    timeLabel = Label(timeWindow, text = "00:00 AM")
    timeLabel.place(x = 120, y = 25)
    timeLabel.config(font = ("courier", 50))

    statusWindow = LabelFrame(root, text = "Status")
    statusWindow.place(x = 10, y = 400, height = 90, width = 580)

    statusLabel = Label(statusWindow, text = "", font = 20)
    statusLabel.place(x = 10, y = 15)



    live_time()
    update_db()
    check_time()
    root.mainloop()
    conn.close()