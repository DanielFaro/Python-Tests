import singer
import urllib.request
import json
import datetime
from datetime import datetime, timezone, timedelta
from ast import literal_eval

#check state from state json and make that the new start date

with open ('config.json') as json_config:
    data = json.load(json_config)

#with open ('state.json') as json_state:
    #state_time = json.load(json_state)
    #last_timerequest = state_time["timestamp"]
    #last_timerequest = None


api_key = data["api_key"]
start_date = data["start_date"]
now = datetime.now(timezone.utc)
currenttimerequest = start_date

#st = literal_eval(start_date)
#futuredate = st + timedelta(hours=2)
#print(futuredate)

#if last_timerequest == None:
 #   currenttimerequest = start_date
#else:
 #   currenttimerequest = last_timerequest 


schema = {
	"properties": {
		"weather": {"type": "string"},
		"timestamp": {"type": "string", "format": "date-time"}
	}
}


for location in data["locations"]:
    lat = location["lat"]
    long = location["long"]
    lat_long = lat + "," + long
    website = 'https://api.darksky.net/forecast/' + api_key + "/" + lat_long
    print(website)

    #while currenttimerequest < now:

    with urllib.request.urlopen(website) as response:
        weather = response.read().decode('utf-8').strip()
        weather = json.loads(weather)
        summary = weather["currently"]["summary"]
        print(summary)
        singer.write_schema('my_weather', schema, 'weather')
        singer.write_records('my_weather', [{'weather': summary, 'timestamp': currenttimerequest}])
        #singer.write_state({'timestamp': currenttimerequest})
        #hour = datetime.timedelta(hours=1)
        #currenttime = now + timedelta(hours=1)
        #print(currenttime)





