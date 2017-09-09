import config
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token=config.UBER_SERVER_TOKEN)
client = UberRidesClient(session)



def getTripPrice(start, end, seat=1):
	response = client.get_price_estimates(
	    start_latitude=start[0],
	    start_longitude=start[1],
	    end_latitude=end[0],
	    end_longitude=end[1],
	    seat_count=seat
	)

	return response.json.get('prices')



print getTripPrice((33.885931,-84.0556346), (33.7756178,-84.3984737))
