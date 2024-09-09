# Ticketmaster Events Fetcher

This Python package allows you to easily fetch and process event data from the Ticketmaster API. It's designed to be simple to use and customize for your specific needs.

## Features

- Fetch events for a specific city (eg. San Francisco)
- Customizable date range
- Comprehensive event information including venue details, ticket information, and more
- Easy-to-use command-line interface
- Exportable JSON output

## Installation

## Usage

1. Set your Ticketmaster API key as an environment variable:

pip install events-scraper

## Usage

python
from events_scraper import EventsFetcher

Initialize the EventsFetcher with your Ticketmaster API key

fetcher = EventsFetcher(api_key='your_api_key_here')
Fetch events
events = fetcher.get_events(city='New York', days_ahead=60, limit=20)

Process the events

for event in events:
print(f"Event: {event['name']}")
print(f"Date: {event['date']}")
print(f"Venue: {event['venue']}")
print(f"Price Range: {event['price_range']}")
print("---")



## API Reference

### `EventsFetcher(api_key: str)`

Initialize the EventsFetcher with your Ticketmaster API key.

### `get_events(city: str = 'San Francisco', days_ahead: int = 30, limit: int = 15) -> List[Dict[str, Any]]`

Fetch events based on the given parameters.

- `city`: The city to fetch events for (default: 'San Francisco')
- `days_ahead`: Number of days ahead to fetch events for (default: 30)
- `limit`: Maximum number of events to fetch (default: 15)

Returns a list of dictionaries containing event information.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

