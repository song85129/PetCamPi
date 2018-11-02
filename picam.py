import sys
import time
import datetime
import telepot
import os
from picamera import PiCamera
import subprocess
import logging
logging.basicConfig(filename='PetCamPi.log',level=logging.INFO) # Logging into the file PetCamPi.log
logging.info('let the time begin')

cmdline=['MP4Box','-fps','25','-add','pet.h264','pet.mp4']; # Converting h264 video from Raspberry pi camera to mp4
camera = PiCamera(); # Initiate Raspberry Pi camera
camera.resolution=(1920, 1080); # Set Camera resolution
camera.exposure_mode='auto'; # Set camera exposure mode
id_lib = [xxxxxx,xxxxxx];  # Set telegram user id (only response commands from user IDs in this library) replace xxxxx with user id

def handle(msg):
	chat_id = msg['chat']['id'] # Extract user id from received message
	logging.info('time: %s id: %s, Message: %s' % (str(datetime.datetime.now()),chat_id, msg['text'])) # log the user id and message it sent
	print(chat_id) 
	if chat_id in id_lib:		# check if user id is in the library
		command = msg['text']
		print('Got command: %s' % command)
			
		if command == '/time':	# If command is /time, send back the current time
			bot.sendMessage(chat_id, str(datetime.datetime.now()))
		elif command == '/pet_pic': #If command is /pet_pic, send back the picture
			camera.start_preview()
			time.sleep(3)
			camera.capture('/home/pi/Documents/picam/pet.jpg')
			camera.stop_preview()
			bot.sendPhoto(chat_id=chat_id,photo=open('/home/pi/Documents/picam/pet.jpg','r'))
		elif command == '/pet_vid': #If command is /pet_vid, send back the video defined below
			camera.resolution=(1280,720); # change video resolution
			subprocess.check_output(['rm','pet.mp4']) # remove the existing video
			camera.start_preview()
			camera.start_recording('/home/pi/Documents/picam/pet.h264',quality=25)
			time.sleep(10) # video time is 10 seconds
			camera.stop_recording()
			camera.stop_preview()
			subprocess.check_output(cmdline)
			bot.sendVideo(chat_id=chat_id, video=open('/home/pi/Documents/picam/pet.mp4','r'))
		elif command == '/guanbi':
			pass			
	else:
		bot.sendMessage(xxxxxxx, chat_id) # if the user id is not in the library, send the user id to the administrator, replace xxxxx with main user id

bot = telepot.Bot('xxxxxxxxxxxxxx') # create a bot for the telegram, replace the string xxxxxxxx in bracket with bot id
bot.message_loop(handle)
print('I am listending...')

while 1:
	time.sleep(10)
