import requests

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

print(data['estimated_hourly_times'])
print(now)

def getWaitTimes():
	response = requests.get("https://www.tsawaittimes.com/api/airport/Izu2gTMXZEPT9cvoE2PrOCfxwmFyIgZc/ATL")
	data = response.json()
	return data