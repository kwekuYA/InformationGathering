#Importing modules
import sys
import requests 
import socket
import json

#Checking for zero arguements
if len( sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <url>")
    sys.exit(1)


#Banner Grabbing
req = requests.get("https://"+ sys.argv[1])
print("\n"+str(req.headers)+"\n")

#Getting IP address of the target 

gethostby_ = socket.gethostbyname(sys.argv[1])
print("The IP address of "+sys.argv[1]+" is "+ gethostby_ +"\n")

#Getting the location using the ipinfo API in a JSON format
req_two= requests.get("https://ipinfo.io/"+gethostby_+ "/json")
resp_ = json.loads(req_two.text)

print("City: " + resp_["city"] )
print("Location: " + resp_["loc"] )
print("Region " + resp_["region"] )
print("Country: " + resp_["country"] )
print("Postal: " + resp_["postal"] )
print("Timezone: " + resp_["timezone"] )
