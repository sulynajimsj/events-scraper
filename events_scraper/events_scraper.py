import requests
from datetime import datetime, timedelta
from typing import List, Dict, Any

class EventsFetcher:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://app.ticketmaster.com/discovery/v2/events.json"

    def get_events(self, city: str = 'San Francisco', days_ahead: int = 30, limit: int = 15) -> List[Dict[str, Any]]:
        start_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        end_date = (datetime.now() + timedelta(days=days_ahead)).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        params = {
            'apikey': self.api_key,
            'city': city,
            'startDateTime': start_date,
            'endDateTime': end_date,
            'sort': 'date,asc',
            'size': limit
        }

        response = requests.get(self.base_url, params=params)
        data = response.json()

        events = []
        if '_embedded' in data and 'events' in data['_embedded']:
            for event in data['_embedded']['events']:
                event_info = {
                    'name': event.get('name', ''),
                    'url': event.get('url', ''),
                    'date': event['dates']['start'].get('localDate', '') if 'dates' in event and 'start' in event['dates'] else '',
                    'time': event['dates']['start'].get('localTime', '') if 'dates' in event and 'start' in event['dates'] else '',
                    'venue': event['_embedded']['venues'][0]['name'] if '_embedded' in event and 'venues' in event['_embedded'] and event['_embedded']['venues'] else '',
                    'genre': event['classifications'][0]['genre']['name'] if 'classifications' in event and event['classifications'] and 'genre' in event['classifications'][0] else '',
                    'price_range': f"{event['priceRanges'][0]['min']} - {event['priceRanges'][0]['max']} {event['priceRanges'][0]['currency']}" if 'priceRanges' in event and event['priceRanges'] else 'N/A'
                }
                events.append(event_info)

        return events