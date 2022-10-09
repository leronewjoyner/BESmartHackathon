def getGmapsURL(term):
    baseUrl = "https://www.google.com/maps/search/?api=1&query="
    ext = term.split()
    ext = "+".join(ext)
    url = baseUrl + ext
    return url

print(getGmapsURL("bwi gate a10"))