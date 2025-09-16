# Deployment Guide

## Current Production Setup

**Architecture**: Docker + Fly.io with built-in HTTPS  
**Status**: Working and tested

## Quick Start

### 1. Deploy to Fly.io

**Option A: Use the deployment script (recommended)**
```bash
./deploy.sh
```

**Option B: Manual deployment**
```bash
# Install Fly.io CLI if not already installed
curl -L https://fly.io/install.sh | sh
export PATH="$HOME/.fly/bin:$PATH"

# Login to Fly.io
fly auth login

# Deploy the application
fly deploy --config fly.toml --dockerfile Dockerfile.fly
```

### 2. Update HappyRobot

Use the Fly.io HTTPS URL in your HappyRobot configuration:
- **URL**: `https://freight-api-happy-robot.fly.dev/search-loads`
- **API Key**: Set via Fly.io secrets (see below)

## Alternative: Local Development

```bash
cd api
docker build -t freight-api .
docker run -p 8000:8000 -e API_KEY=your-api-key-here freight-api
```

## Troubleshooting

### API Not Responding
- Check Fly.io app status: `fly status`
- View logs: `fly logs`
- Check app health: `fly health`

### Authentication Errors
- Verify API key matches exactly
- Check Authorization header format: `Bearer <key>`
- Ensure API_KEY environment variable is set

### Deployment Issues
- Check Dockerfile: `fly deploy --dockerfile Dockerfile.fly`
- Verify fly.toml configuration
- Check Fly.io app logs for errors

## Production Considerations

1. **Monitoring**: Use `fly logs` and `fly status` for monitoring
2. **API Key Rotation**: Implement key rotation strategy
3. **Scaling**: Fly.io auto-scales based on traffic
4. **Database**: Replace sample data with real load database
5. **Custom Domain**: Add custom domain in Fly.io dashboard

## Fly.io Benefits

- **Built-in HTTPS**: Automatic SSL certificates
- **Global CDN**: Fast worldwide access
- **Auto-scaling**: Handles traffic spikes
- **Zero maintenance**: No server management needed
- **Docker native**: Perfect for containerized apps