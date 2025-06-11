import requests
from datetime import datetime, timedelta
from keys import API_KEY 

def fetch_events(city):
    today = datetime.now().strftime('%Y-%m-%dT00:00:00Z')
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%dT00:00:00Z')

    url = 'https://app.ticketmaster.com/discovery/v2/events.json'
    params = {
        'apikey': API_KEY,
        'city': city,
        'startDateTime': today,
        'endDateTime': tomorrow,
        'sort': 'date,asc',
        'size': 10
    }

    response = requests.get(url, params=params)
    data = response.json()

    events = []
    if '_embedded' in data:
        for event in data['_embedded']['events']:
            # extract date
            date = 'TBD'
            if 'dates' in event and 'start' in event['dates']:
                date_str = event['dates']['start'].get('localDate')
                if date_str:
                    try:
                        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                        date = date_obj.strftime('%B %d, %Y')
                    except ValueError:
                        pass
            
            # extract genre
            genre = 'General'
            if 'classifications' in event and event['classifications']:
                classification = event['classifications'][0]
                genre_name = classification.get('genre', {}).get('name')
                segment_name = classification.get('segment', {}).get('name')
                if genre_name and genre_name != 'Undefined':
                    genre = genre_name
                elif segment_name and segment_name != 'Undefined':
                    genre = segment_name
            
            # extract venue
            venue_name = 'Unknown Venue'
            if '_embedded' in event and 'venues' in event['_embedded'] and event['_embedded']['venues']:
                venue_name = event['_embedded']['venues'][0].get('name', 'Unknown Venue')
            
            events.append({
                'name': event.get('name', 'Unknown Event'),
                'venue': venue_name,
                'date': date,
                'time': event.get('dates', {}).get('start', {}).get('localTime', 'TBD'),
                'genre': genre,
                'url': event.get('url', '#') 
            })

    return events

