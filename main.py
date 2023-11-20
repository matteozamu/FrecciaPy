import json
import sys
import time
import urllib3
import ui
import re

ui = ui.UI()

# ui.print()
url = 'https://d6o.portalefrecce.it/PortaleFrecce/infoViaggioActionJson'

while True:
  try:
    http = urllib3.PoolManager()
    response = http.request('GET', url)
  except Exception as e:
    # print(f"An error occurred: {e}")
    print("You are not connected to the Frecciarossa WiFi :(\nPlease, connect to it")
    sys.exit(-1)

  try:
    json_response = json.loads(response.data)
  except Exception as e:
    print("An error occured reading the data :(")
    sys.exit(-1)

  if json_response['isGpsValid'] == True:
    ui.gps['speed'] = json_response['speed']
    ui.trackLine = json_response['trackline']
    
    pattern = r'\d+'
    matches = re.findall(pattern, json_response['delay2'])
    if matches:
      ui.gps['delay'] = "+" + matches[0] + " min"
    else:
      ui.gps['delay'] = "On Time"

    ui.stops = json_response['statoPercorso']

    ui.print()
    time.sleep(0.5)

  else:
    ui.printError()
