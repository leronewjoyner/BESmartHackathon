from multiprocessing.connection import wait
from tkinter import W
import requests
from datetime import datetime
import json

def waitTimeFinder():
	def getWaitTimes():
		response = requests.get("https://www.tsawaittimes.com/api/airport/Izu2gTMXZEPT9cvoE2PrOCfxwmFyIgZc/DFW")
		data = response.json()
		return data['estimated_hourly_times']

	def getCurrTime():
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		return current_time

	def mapTimeToIndex(raw_time):
		time = raw_time().strip()
		hour = int(time[:2])
		meridian = time[8:]
		# Special-case '12AM' -> 0, '12PM' -> 12 (not 24)
		if (hour == 12):
			hour = 0
		if (meridian == 'PM'):
			hour += 12
		return hour - 1

	waitTimes = getWaitTimes()
	now = mapTimeToIndex(getCurrTime)
	return waitTimes[now]['waittime']


