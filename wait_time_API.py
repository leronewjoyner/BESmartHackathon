import requests
import json
#api key: Izu2gTMXZEPT9cvoE2PrOCfxwmFyIgZc
def waitTimeFinder(hour,code):
	baseUrl = "https://www.tsawaittimes.com/api/airport/Izu2gTMXZEPT9cvoE2PrOCfxwmFyIgZc/"
	url = baseUrl + str(code)
	response = requests.get(url)
	waitTimeData = response.json()['rightnow_description']
	return waitTimeData

