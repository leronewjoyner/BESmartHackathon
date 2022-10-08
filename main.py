import requests
from datetime import datetime

def getWaitTimes():
	response = requests.get("https://www.tsawaittimes.com/api/airport/Izu2gTMXZEPT9cvoE2PrOCfxwmFyIgZc/ATL")
	data = response.json()
	return data

def getCurrTime():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	return current_time