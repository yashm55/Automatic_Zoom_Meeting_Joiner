# Importing necessary libraries and our database.
from datetime import time
import requests
import json
import database

# Enter the TOKEN of your bot provided by BotFather inside the quotes.
token = ""
base = f"https://api.telegram.org/bot{token}/"


# Function to get updates from the telegram bot api 
def getUpdates(offset = None):
    url = base + "getUpdates?timeout=0"
    if offset:
        url = url + f"&offset={offset+1}"
    r = requests.get(url)
    return json.loads(r.content)


def sendReply(msg, chat_id):
    url = base + f"sendMessage?chat_id={chat_id}&text={msg}"
    if msg is not None:
        requests.get(url)


# Extracts the meeting time from the message (Zoom meeting details message) that we sent to the telegram bot as a string.
def get_time(message):
    final_string_time = "Empty"
    try:
        splitted = message.split()
        time_index = splitted.index("Time:")
        final_list_time = splitted[time_index +1 : time_index +6]
        final_string_time = final_list_time[0] + " " + final_list_time[1] +" " + final_list_time[2] + " " + final_list_time[3] + " " + final_list_time[4]
    except:
        pass
    return final_string_time


# Extracts the topic of the meeting from message that we sent to the telegram bot as a string.
# This will be later used for deleting specific meetings from the schedule.
def get_topic(message):
    topic = "Empty"
    try:
        splitted = message.split()
        topic_index = splitted.index("Topic:")
        time_index = splitted.index("Time:")
        topic_list = splitted[topic_index +1 : time_index]
        string_topic = ""
        for i in topic_list:
            string_topic += i + " "
        topic = string_topic
    except:
        pass
    return topic


# Extracts the link of the Zoom meeting.
def get_link(message):
    link = "Empty"
    try:
        splitted = message.split()
        for item in splitted:
            if "http" in item:
                link = item
                return link
    except:
        pass
    return link


updateID = None

# Main function to keep the bot running.
def run_bot(running = True):
    if running == False:
        return None
    global updateID
    schedule = "Empty"
    link = "Empty"
    topic = "Empty"
    updates = getUpdates(offset=updateID)
    try:
        updates = updates["result"]
    except:
        pass
    if updates:
        for item in updates:
            updateID = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            if message is not None:
                schedule = get_time(message)
                link = get_link(message)
                topic = get_topic(message)
                print(schedule+"\n"+link+"\n"+topic)
            if topic != "Empty":
                database.add_entry(link, schedule, topic)
                return f"Added {topic}"
            else:
                return "Empty"

if __name__ == '__main__':
    run_bot()