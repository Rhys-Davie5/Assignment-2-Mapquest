import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "sjYTzp2mAzxK2Cct26xsnaScPfxOtwBg"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break

    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("========================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Miles: " + str(json_data["route"]["distance"]))

        if "realTimeTraffic" in json_data["route"]:
            print("Traffic: " + json_data["route"]["realTimeTraffic"]["congestionSeverity"])
        else:
            print("Traffic information not available for this route.")
        
