import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
API_KEY = os.getenv("API_KEY")
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Sample loads data
SAMPLE_LOADS = [
    {
        "load_id": "L001",
        "origin": "Chicago, IL",
        "destination": "Dallas, TX",
        "equipment_type": "Dry Van",
        "pickup_date": "2024-01-15T08:00:00Z",
        "loadboard_rate": 2500,
        "miles": 925,
        "weight": 45000
    },
    {
        "load_id": "L002",
        "origin": "Atlanta, GA",
        "destination": "Miami, FL",
        "equipment_type": "Reefer",
        "pickup_date": "2024-01-16T09:00:00Z",
        "loadboard_rate": 3200,
        "miles": 660,
        "weight": 40000
    },
    {
        "load_id": "L003",
        "origin": "Los Angeles, CA",
        "destination": "Phoenix, AZ",
        "equipment_type": "Flatbed",
        "pickup_date": "2024-01-17T10:00:00Z",
        "loadboard_rate": 1800,
        "miles": 370,
        "weight": 48000
    },
    {
        "load_id": "L004",
        "origin": "New York, NY",
        "destination": "Boston, MA",
        "equipment_type": "Dry Van",
        "pickup_date": "2024-01-18T11:00:00Z",
        "loadboard_rate": 1200,
        "miles": 215,
        "weight": 42000
    },
    {
        "load_id": "L005",
        "origin": "Houston, TX",
        "destination": "Denver, CO",
        "equipment_type": "Reefer",
        "pickup_date": "2024-01-19T07:00:00Z",
        "loadboard_rate": 2800,
        "miles": 880,
        "weight": 38000
    },
    {
        "load_id": "L006",
        "origin": "Chicago, IL",
        "destination": "Atlanta, GA",
        "equipment_type": "Dry Van",
        "pickup_date": "2024-01-20T09:00:00Z",
        "loadboard_rate": 2200,
        "miles": 715,
        "weight": 44000
    }
]
