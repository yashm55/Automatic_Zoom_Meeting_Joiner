
#  Importing necessary libraries , bot and database.
from sqlite3.dbapi2 import Cursor
from tkinter import *
import live_date
from PIL import Image, ImageTk, ImageOps
import bot
import database
import sqlite3
import webbrowser

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

    root.wm_iconbitmap("Auto_zoom logo.ico")

    controllWindow = LabelFrame(root, text = "ScheduleControls")
    controllWindow.place(x = 10, y = 10, height = 230, width = 580)

    seeSchedule = Button(controllWindow, text = """Todays
Schedule""", command=todays_schedule)
    seeSchedule.place(x = 7, y = 10, height = 40, width = 100)

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
    main_list.place(x = 117, y = 10, height = 195, width = 340)

    image1 = ImageTk.PhotoImage(Image.open("Automating_zoom.png"))
    imageLabel = Label(controllWindow, image = image1)
    imageLabel.place(x = 117, y = 10, height = 195, width = 340)

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