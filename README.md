# Freight Dynamics Express - Inbound Carrier Sales API

A FastAPI-based load search service for freight brokers to find and match carriers with available loads.

## Current Solution

**Deployment**: Docker container on Fly.io with built-in HTTPS  
**Status**: Production Ready  
**HTTPS URL**: `https://freight-api-happy-robot.fly.dev/`

## Project Structure

```
happy-robot-case-study/
├── src/                    # Source code
│   ├── main.py            # FastAPI application
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # Docker configuration
├── scripts/               # Deployment scripts
│   └── deploy.sh          # Fly.io deployment script
├── docs/                  # Documentation
│   ├── API_REFERENCE.md   # API documentation
│   └── DEPLOYMENT.md      # Deployment guide
├── Dockerfile.fly         # Fly.io Dockerfile
├── fly.toml              # Fly.io configuration
└── FDE Technical Challenge - Inbound Carrier Sales (1).pdf
```

## Quick Start

1. **Deploy to Fly.io**: `./scripts/deploy.sh`
2. **Use in HappyRobot**: `https://freight-api-happy-robot.fly.dev/search-loads`

## API Endpoints

### Health Check
```http
GET /health
```

### Search Loads
```http
POST /search-loads
Content-Type: application/json
Authorization: Bearer 351a609402d763180c4ec24bfb5741893cce0f75cd4602b3d8723be8bc579d7a

{
  "origin_city": "Chicago",
  "origin_state": "IL", 
  "destination_city": "Dallas",
  "destination_state": "TX",
  "equipment_type": "Dry Van",
  "pickup_datetime": "2024-01-15T08:00:00Z"
}
```

## Docker Deployment

### Build and Run Locally
```bash
cd src
docker build -t freight-api .
docker run -p 8000:8000 -e API_KEY=your-api-key-here freight-api
```

### Production Deployment (Fly.io)
1. Deploy to Fly.io: `./scripts/deploy.sh` (or `fly deploy`)
2. Use the provided HTTPS URL for HappyRobot integration

## Security

- **API Key Authentication**: All endpoints require valid API key
- **HTTPS**: Secure communication via Fly.io's built-in SSL
- **Input Validation**: Pydantic models validate all requests

### API Key Setup

1. **Generate a secure API key**:
   ```bash
   # Option 1: Generate with OpenSSL
   openssl rand -hex 32
   
   # Option 2: Generate with Python
   python3 -c "import secrets; print(secrets.token_hex(32))"
   ```

2. **Set as Fly.io secret**:
   ```bash
   flyctl secrets set API_KEY=your-generated-key-here
   ```

3. **For local development**, create a `.env` file:
   ```bash
   # Create .env file with your API key
   echo "API_KEY=your-generated-key-here" > .env
   
   # Or copy from the example
   cp .env.example .env
   # Then edit .env and replace the API key with your own
   ```

## HappyRobot Integration

**HTTPS Endpoint**: `https://freight-api-happy-robot.fly.dev/search-loads`  
**API Key**: Set via environment variable `API_KEY` or Fly.io secrets

Configure this URL in your HappyRobot "Search for Loads" tool for seamless integration.

## Testing

Test the API with curl:
```bash
# Health check
curl https://freight-api-happy-robot.fly.dev/health

# Search loads
curl -X POST https://freight-api-happy-robot.fly.dev/search-loads \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer 351a609402d763180c4ec24bfb5741893cce0f75cd4602b3d8723be8bc579d7a' \
  -d '{"origin_city":"Chicago","origin_state":"IL","destination_city":"Dallas","destination_state":"TX","equipment_type":"Dry Van"}'
```

## Requirements

- Python 3.11+
- Docker
- Fly.io CLI (for deployment)

## Documentation

- **[API Reference](docs/API_REFERENCE.md)** - Complete API documentation
- **[Deployment Guide](docs/DEPLOYMENT.md)** - Step-by-step deployment

## Maintenance

- **Fly.io URL**: Static HTTPS URL - no changes needed
- **API Key**: Store securely and rotate periodically
- **Load Data**: Update sample loads in `src/main.py` as needed
