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
    response = urllib3.request.urlopen(url)
  except Exception as e:
    # print(f"An error occurred: {e}")
    print("You are not connected to the Frecciarossa WiFi :(\nPlease, connect to it")
    sys.exit(-1)
      
  json_string = json.loads((response.read()).decode('utf-8'))

  json_response = json.loads(json_string)

  if json_response['isGpsValid'] == True:
    ui.gps['speed'] = json_response['speed']
    ui.trackLine = json_response['trackline']
    
    match = re.search(r'\+(\d+)min', json_response['delay2'])
    if match:
      ui.gps['delay'] = "+" + match.group(1) + " min"
    else:
      ui.gps['delay'] = "On Time"

    ui.stops = json_response['statoPercorso']

    ui.print()
    time.sleep(0.5)

  else:
    ui.printError()
