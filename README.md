# EventFinder

A Flask web application that helps users find live events happening tonight in their city using the Ticketmaster Discovery API.

## Features

- Search for live events by city
- Find concerts, comedy shows, sports games, and more
- Focus on events happening today/tonight
- Direct links to buy tickets

## Quick Start

**The `keys.py` file is already included for easy testing!** Just run:

```bash
pip install -r requirements.txt
python app.py
```
Then go to `http://localhost:5001`

## Setup Instructions

### 1. Clone and setup
```bash
git clone <your-repo-url>
cd final-project
pip install -r requirements.txt
```

### 2. Run the app
```bash
python app.py
```
Open your browser and go to `http://localhost:5001`

### 3. (Optional) Get your own API key
If you want to use your own API key:
1. Go to [Ticketmaster Developer API](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/)
2. Sign up for a free account
3. Create a new app to get your Consumer Key
4. Replace the API key in `keys.py`:
```python
API_KEY = "your_api_key_here"
```

## How to use

1. Type in a city name (like "Seattle" or "New York")
2. Click "Search Events" 
3. Browse the results!
