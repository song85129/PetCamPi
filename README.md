# PetCamPi

A python based pet monitor with telegram

## Description

A simple python code that will capture picture or video based on the command received from telegram.

Current commands available:

1. **/time** reply with a message with current time
2. **/pet_pic** reply with a picture taken right after received the command
3. **/pet_vid** reply with a 10s video in the form of gif shot right after received the command

## Prerequisite

### 1. Telepot

Telepot is a telegram bot. Here is the steps on how to use it:

1. Search for a user called BotFather
2. Get a bot account, text him **/newbot**, answer his questions.
3. At the end of the process, a token will be given, this token represents the bot account, keep it safe.
4. Install Telepot on Raspberry pi
    'sudo apt-get install python-pip'
    'sudo pip install telepot'
5. Text BotFather **/setcommands** to set the comment shown above

### 2. gpac

Telegram bot has a limit on the maximum size of the video file it can send. I tried with different sizes and it turned out that if the file is too big, bot will send the file but when I open it on my phone, it just shows black images in the video.
Also I need to convert the raw video h264 to mp4 for telepot to send the video file. So gpac is used to convert the video.
To install it
    'sudo apt-get update'
    'sudo apt-get install gpac' 
After several test and trials, I found the current setting is at the limit.

Please feel free to play the setting and let me know if you have different idea.

## Usage 

1. Put your telegram user id in the id_lib list in line 16

2. Put the telegram bot token in line 49

Then run it, you should be able to get it working, it is pretty straight forward.
Please play with the settings and share what you think is best for it.
I also used logging package to put logs into a .log file
