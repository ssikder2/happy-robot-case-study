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
        "pickup_datetime": "2024-01-15T08:00:00Z",
        "delivery_datetime": "2024-01-16T14:00:00Z",
        "equipment_type": "Dry Van",
        "loadboard_rate": 2500,
        "notes": "Standard dry van load, no special requirements",
        "weight": 45000,
        "commodity_type": "General Freight",
        "num_of_pieces": 24,
        "miles": 925,
        "dimensions": "53' x 8'6\" x 9'6\""
    },
    {
        "load_id": "L002",
        "origin": "Atlanta, GA",
        "destination": "Miami, FL",
        "pickup_datetime": "2024-01-16T09:00:00Z",
        "delivery_datetime": "2024-01-17T16:00:00Z",
        "equipment_type": "Reefer",
        "loadboard_rate": 3200,
        "notes": "Temperature controlled, maintain 36-38°F",
        "weight": 40000,
        "commodity_type": "Perishable Food",
        "num_of_pieces": 18,
        "miles": 660,
        "dimensions": "53' x 8'6\" x 9'6\""
    },
    {
        "load_id": "L003",
        "origin": "Los Angeles, CA",
        "destination": "Phoenix, AZ",
        "pickup_datetime": "2024-01-17T10:00:00Z",
        "delivery_datetime": "2024-01-17T18:00:00Z",
        "equipment_type": "Flatbed",
        "loadboard_rate": 1800,
        "notes": "Oversized load, requires permits",
        "weight": 48000,
        "commodity_type": "Construction Materials",
        "num_of_pieces": 12,
        "miles": 370,
        "dimensions": "48' x 8'6\" x 12'"
    },
    {
        "load_id": "L004",
        "origin": "New York, NY",
        "destination": "Boston, MA",
        "pickup_datetime": "2024-01-18T11:00:00Z",
        "delivery_datetime": "2024-01-18T19:00:00Z",
        "equipment_type": "Dry Van",
        "loadboard_rate": 1200,
        "notes": "Local delivery, same day service",
        "weight": 42000,
        "commodity_type": "Electronics",
        "num_of_pieces": 36,
        "miles": 215,
        "dimensions": "53' x 8'6\" x 9'6\""
    },
    {
        "load_id": "L005",
        "origin": "Houston, TX",
        "destination": "Denver, CO",
        "pickup_datetime": "2024-01-19T07:00:00Z",
        "delivery_datetime": "2024-01-20T15:00:00Z",
        "equipment_type": "Reefer",
        "loadboard_rate": 2800,
        "notes": "Frozen goods, maintain -10°F",
        "weight": 38000,
        "commodity_type": "Frozen Food",
        "num_of_pieces": 22,
        "miles": 880,
        "dimensions": "53' x 8'6\" x 9'6\""
    },
    {
        "load_id": "L006",
        "origin": "Chicago, IL",
        "destination": "Atlanta, GA",
        "pickup_datetime": "2024-01-20T09:00:00Z",
        "delivery_datetime": "2024-01-21T17:00:00Z",
        "equipment_type": "Dry Van",
        "loadboard_rate": 2200,
        "notes": "White glove delivery required",
        "weight": 44000,
        "commodity_type": "Furniture",
        "num_of_pieces": 8,
        "miles": 715,
        "dimensions": "53' x 8'6\" x 9'6\""
    }
]
