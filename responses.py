import urllib, json
url = "https://maps.googleapis.com/maps/api/geocode/json?address=disneyland,ca"
response = urllib.urlopen(url)
data = json.loads(response.read())
print data
