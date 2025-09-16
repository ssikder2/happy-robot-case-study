# API Reference

## Base URL
```
https://freight-api-happy-robot.fly.dev
```
*Note: Fly.io provides stable HTTPS URL*

## Authentication
All endpoints require API key authentication via Bearer token:
```
Authorization: Bearer 351a609402d763180c4ec24bfb5741893cce0f75cd4602b3d8723be8bc579d7a
```

## Endpoints

### Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-09-15T21:38:09.098070"
}
```

### Search Loads
```http
POST /search-loads
Content-Type: application/json
Authorization: Bearer <your-api-key>
```

**Request Body:**
```json
{
  "origin_city": "Chicago",
  "origin_state": "IL",
  "destination_city": "Dallas", 
  "destination_state": "TX",
  "equipment_type": "Dry Van",
  "pickup_datetime": "2024-01-15T08:00:00Z"
}
```

**Response:**
```json
{
  "loads": [
    {
      "load_id": "L001",
      "origin": "Chicago, IL",
      "destination": "Dallas, TX",
      "pickup_datetime": "2024-07-20T08:00:00Z",
      "delivery_datetime": "2024-07-22T17:00:00Z",
      "equipment_type": "Dry Van",
      "loadboard_rate": 2500.0,
      "notes": "Fragile goods, handle with care",
      "weight": 40000,
      "commodity_type": "Electronics",
      "num_of_pieces": 20,
      "miles": 900,
      "dimensions": "53ft"
    }
  ],
  "load_count": 1,
  "selected_load_id": "L001",
  "initial_rate": 2500.0
}
```

## Error Responses

### 401 Unauthorized
```json
{
  "detail": "Invalid API key"
}
```

### 500 Internal Server Error
```json
{
  "detail": "API key not configured"
}
```

## Sample Loads

| Load ID | Origin | Destination | Equipment | Rate | Miles |
|---------|--------|-------------|-----------|------|-------|
| L001 | Chicago, IL | Dallas, TX | Dry Van | $2,500 | 900 |
| L002 | Atlanta, GA | Miami, FL | Reefer | $3,200 | 660 |
| L003 | Los Angeles, CA | Phoenix, AZ | Flatbed | $1,800 | 370 |
| L004 | New York, NY | Boston, MA | Dry Van | $1,200 | 220 |
| L005 | Houston, TX | Denver, CO | Reefer | $2,800 | 850 |
| L006 | Chicago, IL | Atlanta, GA | Dry Van | $2,200 | 720 |

## Equipment Types
- `Dry Van`
- `Reefer` 
- `Flatbed`

## Testing with curl

```bash
# Health check
curl https://freight-api-happy-robot.fly.dev/health

# Search loads
curl -X POST https://freight-api-happy-robot.fly.dev/search-loads \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer 351a609402d763180c4ec24bfb5741893cce0f75cd4602b3d8723be8bc579d7a' \
  -d '{
    "origin_city": "Chicago",
    "origin_state": "IL",
    "destination_city": "Dallas",
    "destination_state": "TX", 
    "equipment_type": "Dry Van"
  }'
```
