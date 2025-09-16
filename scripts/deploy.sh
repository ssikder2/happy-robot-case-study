#!/bin/bash

# Change to project root directory
cd "$(dirname "$0")/.."

echo "Deploying Freight API to Fly.io"

# Check if flyctl is installed
if ! command -v flyctl &> /dev/null
then
    echo "Installing flyctl..."
    curl -L https://fly.io/install.sh | sh
    export PATH="$HOME/.fly/bin:$PATH"
fi

# Check if user is logged in
if ! flyctl auth whoami &> /dev/null
then
    echo "Logging into Fly.io..."
    flyctl auth login
fi

# Set API key as secret (user must provide their own)
echo "Setting API key as secret..."

# Check if .env file exists and has API_KEY
if [ -f ".env" ] && grep -q "API_KEY=" .env; then
    # Extract API key from .env file
    api_key=$(grep "API_KEY=" .env | cut -d '=' -f2 | tr -d '"' | tr -d "'")
    echo "Using API key from .env file"
else
    echo "No .env file found or API_KEY not set in .env"
    echo "Please enter your API key (or press Enter to use a generated one):"
    read -s api_key
    if [ -z "$api_key" ]; then
        # Generate a secure random API key
        api_key=$(openssl rand -hex 32)
        echo "Generated API key: $api_key"
        # Save to .env file for future use
        echo "API_KEY=$api_key" > .env
        echo "Saved API key to .env file"
    fi
fi

flyctl secrets set API_KEY="$api_key"

# Deploy to Fly.io
echo "Deploying to Fly.io..."
flyctl deploy --config fly.toml --dockerfile Dockerfile.fly

echo "Deployment complete!"
echo "Your API is available at: https://freight-api-happy-robot.fly.dev/"
echo "Health check: https://freight-api-happy-robot.fly.dev/health"
echo "Search endpoint: https://freight-api-happy-robot.fly.dev/search-loads"
