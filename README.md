# Zoom Automation
This program focuses on automating the zoom meetings which these days we all mostly have. We already know that there exists such program that does automate this process, but our 
implementation is a bit different and will **_work best for those people who have to join multiple meetings in a day and the meeting's credentials are different everytime_**. 

# Getting Started
These instructions will get you a copy of the project up and runnning on your local machine for using / testing or development purposes.

### Prerequisites
Things you are going to need to get this program up and running on your machine.

```
(1) Python 3

(2) Zip extracting software, such as winrar or 7Zip.

(3) Telegram

(4) Network connection

(5) Windows 8.1 or higher. (10 recommended)
```

---

## Windows

Head to [this link](https://www.python.org/downloads/) and click on the yellow button saying "Download Python 3.x.x", **_"x"_** here represents the version, it might be 
different based on when you decide to use this.


Go to the location on your PC where you downloaded the python setup, and then double-click it to begin it's installation, at the time of writting this documentation
you can refer the steps and reference images below:-

---

1. After double-clicking the python installation file, and granting it privileges, an installation window of Python will appear, on that window, on the bottom
left corner will be a box and text stating "Add Python [version] to PATH", **Please make sure, that you check that box, as it's very important.**

![ss1](https://user-images.githubusercontent.com/42169204/107082107-b714d900-6819-11eb-8050-019fadf942a2.PNG)


2. After that, click on "Customize installation", and in there, make sure, all of the boxes are checked, and click "Back", and then "Install Now".

![ss2](https://user-images.githubusercontent.com/42169204/107082351-0d821780-681a-11eb-9cf3-2ac63fcb5b12.PNG)


3. Now, click [this link](https://github.com/evil5198/AutoZoom) and then click "Code" and download it as ZIP. After the download is complete, extract it.

![ss3](https://user-images.githubusercontent.com/42169204/107082427-2b4f7c80-681a-11eb-9145-456811abe34c.PNG)
---
![ss4](https://user-images.githubusercontent.com/42169204/107082507-4b7f3b80-681a-11eb-9f0a-547a7d170852.png)



4. Now, open the folder and double-click the setup file and wait for it to finish installing dependenicies, after it finishes installing dependencies, a message will be printed stating "Dependencies Installed!" and the window will close itself after 5 seconds.


![ss5](https://user-images.githubusercontent.com/42169204/107082633-79648000-681a-11eb-867d-d56afced1afd.PNG)

---

**_If this somehow doesn't work for you, you can do the following step._**

- Open the same folder and press (Shift + right click) click the option saying "Open PowerShell window here", now type the following command:-

![ss](https://user-images.githubusercontent.com/42169204/107117671-f129bd80-68a1-11eb-801d-741996c66269.PNG)


```
python setup.py
```

- It will download and install the dependencies and if everything goes right, you will see a last message saying "Dependencies Installed!", now you can close that window and follow the instructions below.

![ss1](https://user-images.githubusercontent.com/42169204/107117816-da379b00-68a2-11eb-8931-3bffbfab51c5.png)

---

5. Now, follow the Telegram steps.

---

## Setting up Telegram Bot

```
*Before following the steps mentioned below, create a telegram account, if you don't have one.
```

1. Open your telegram app, and on the top right corner, you will see a search icon, tap that and it will open a search bar. There search for "BotFather", the search
result should yeild you a profile by name "BotFather" with a blue tick besides the name.


![ss6](https://user-images.githubusercontent.com/42169204/107082716-9dc05c80-681a-11eb-8f6a-61b8297cc004.jpg)


2. Tap on that profile and start the bot, after that, type "/newbot" and send it to the bot. The BotFather will ask you to name your bot, type the name which you
want to assign to your bot next, the BotFather will ask you to assign a username to your bot, read the instructions from the BotFather and name appropriately. If 
you have followed all of the steps correctly, BotFather will reply and give you a API Token for your bot, copy it.

**_Also please don't try to copy the exact name, username or API token, these images are for reference only._**\
**_Make sure that the username which you assign to your bot is unique, if the username is already taken, BotFather will prompt to try again and use another username._**

![ss7](https://user-images.githubusercontent.com/42169204/107083085-23440c80-681b-11eb-9d3e-98a5aabc0308.jpg)



---

## Assigning your Bot token inside code


1. Now open the folder you extracted few steps before, and in there locate a file named "bot", right click it and click "Edit with IDLE".

![ss8](https://user-images.githubusercontent.com/42169204/107083145-3951cd00-681b-11eb-8c0a-f82dd0efddcd.png)



2. After doing the first step, the code file will be opened. There, within the first 10 lines of the code there will be a line having the following:-
```
token = ""
```

![ss9](https://user-images.githubusercontent.com/42169204/107084303-e24cf780-681c-11eb-84e0-464b8f462fe2.PNG)


3. Inside the quotes paste the API Token of your bot which was provided by BotFather. After doing that, save the file (CTRL + S) and close the file.

![ss10](https://user-images.githubusercontent.com/42169204/107084329-eaa53280-681c-11eb-90e0-d36aea0bf772.PNG)

4. That's it, you have successfully configured everything, now you can read the Usage.

---

# Usage

1. Open up the folder which you extracted, and in there look for a file by name "control_gui", and double-click it. This will start the program and you will see a window 
like this:- 

**_And in background another black window will be opnened (CMD), DO NOT CLOSE THAT WINDOW, you can minimize it instead._**

![ss11](https://user-images.githubusercontent.com/42169204/107084630-4ff92380-681d-11eb-9279-0b2dc7dfea5b.PNG)
---

---
![ss3](https://user-images.githubusercontent.com/42169204/107257256-7f4ba280-6a60-11eb-99c6-9788fe817617.png)



2. Now open telegram and again press on the search icon and search your bot by it's username, once your bot has appeared on the search results, tap on it and start the bot.

![ss13](https://user-images.githubusercontent.com/42169204/107084739-6ef7b580-681d-11eb-8087-f9dbcfd41e8e.jpg)
---

---
![ss14](https://user-images.githubusercontent.com/42169204/107084773-7dde6800-681d-11eb-8678-4f8cedc2b4b9.jpg)

```
*The following steps will only work if you have followed the step 1 and the results match. 
```

3. Forward or send your bot the messages of zoom meeting's details. 

![ss15](https://user-images.githubusercontent.com/42169204/107084808-8afb5700-681d-11eb-8e6e-203b48a2ecbc.jpg)

4. After doing the above step, in the "Bot Status" pane, you will see that the meeting has been added, if you have added multiple meetings at a time, or you just want
to confirm that the meeting has been added, click the "Today's Schedule" Button.

![ss16](https://user-images.githubusercontent.com/42169204/107111423-0ee12d80-6876-11eb-8520-1ba820f1f55b.png)

---

![ss17](https://user-images.githubusercontent.com/42169204/107111434-24eeee00-6876-11eb-9ebe-4e7f8d553281.png)


5. If you want to clear entire schedule of the day, click "Clear Todays Schedule", this will remove all of the meetings of that day and they won't be automated.
**_This only removes the meetings from the programs database and not the actual meeting itself. This button is usually used when all your meetings have been canceled and you
don't want to join the meetings._**


6. If you want to delete a particular meeting from the day's schedule, so that it won't be joined, click "**_Todays Schedule >> Delete Meetings_**

![ss18](https://user-images.githubusercontent.com/42169204/107111735-608ab780-6878-11eb-806d-23733c627c0c.PNG)

7. **_Select the meeting you want to remove >> and then click Delete_**"

![ss20](https://user-images.githubusercontent.com/42169204/107111853-48fffe80-6879-11eb-95c9-6758c9ed979a.PNG)

### DO NOT CLOSE the main app if you want your meetings to be automated, closing the app will do as it sugggests, close the entire program.
### Keep it running till all of your meetings have been automatically joined, after that, you can can close all windows.
### This program will run correctly only if your local machine's time and date is set correctly and is accurate.

---

## Built With

- [Python 3](https://www.python.org/)
- [SQlite 3](https://www.sqlite.org/index.html)

## License 

This project is licensed under the GNU  License - see the [License.md](https://) file for details.




