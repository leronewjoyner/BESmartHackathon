import requests
import json

def waitTimeFinder(time,code):
	def getWaitTimes():
		#api call
		baseUrl = "https://www.tsawaittimes.com/api/airport/Izu2gTMXZEPT9cvoE2PrOCfxwmFyIgZc/"
		url = baseUrl + code
		response = requests.get(url)
		data = response.json()
		return data['estimated_hourly_times']

	def mapTimeToIndex(time):
		#military time to index in departure time time list within json file
		#subtracting two hours because end user is supposed to arrive two hours early
		time = time.strip()
		hour = int(time[:2])
		meridian = time[8:]
		# Special-case '12AM' -> 0, '12PM' -> 12 (not 24)
		if (hour == 12):
			hour = 0
		if (meridian == 'PM'):
			hour += 12
		if hour == 0:
			return 21
		elif hour == 1:
			return 22
		elif hour == 2:
			return 23
		else:
			return hour - 3

	waitTimes = getWaitTimes()
	departureTime = mapTimeToIndex(time)
	return waitTimes[departureTime]['waittime']


