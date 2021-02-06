# Importing necessary library.
import sqlite3

# Following code block creates the database "automate_zoom" and connnects to the database, and creates a new Table meeting_details
# containing columns id, topic, zoom_links and meeting_time to store the respective data, if the database already exists,
# it simply connects to the database. 
connect = sqlite3.connect("automate_zoom.db")
cursor = connect.cursor()
try:
    cursor.execute("""CREATE TABLE meeting_details 
    (
    id integer PRIMARY KEY AUTOINCREMENT,
    topic text,
    zoom_links text,
    meeting_time text
    )""")
except Exception as e:
    pass


# Adds/ Inserts a new row containing meeting details extracted from a single message.
def add_entry(link, time, topic):
    try:
        duplicate = connect.execute("SELECT topic FROM meeting_details WHERE zoom_links = ?", (link,))
        print("duplicate")
        for row in duplicate:
            return None
        connect.execute("INSERT INTO meeting_details (topic, zoom_links, meeting_time ) VALUES (?, ?, ?)", (topic, link, time,))
        connect.commit()
        print("added")
    except Exception as ex:
        pass


# Functon used to delete a row from the database i.e a meeting from the shedule.
# This is the back-end logic used for the "delete" function.
def clear_row(topic):
    try:
        cursor.execute("DELETE FROM meeting_details WHERE topic = ?",(topic,))
        connect.commit()
    except Exception as ex:
        pass


# Function used to clear the entire table containing meeting details.
# This is the back-end logic for the "clear_schedule" function.
def clear_table():
    try:
        cursor.execute("DELETE FROM meeting_details")
        connect.commit()
    except Exception as ex:
        pass
    return "Cleared Today's Schedule"


connect.commit()