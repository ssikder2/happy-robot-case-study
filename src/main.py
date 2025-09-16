from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import uvicorn

from models import LoadSearchRequest, LoadSearchResponse
from config import API_KEY, SAMPLE_LOADS
from dashboard import metrics_data, track_call, get_dashboard_metrics, reset_metrics

# Initialize FastAPI app
app = FastAPI(title="Freight Load Search API", version="1.0.0")

# Security
security = HTTPBearer()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# API Key validation
def verify_api_key(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API key not configured. Set API_KEY environment variable or Fly.io secret.")
    
    if credentials.credentials != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return credentials.credentials

# API Endpoints
@app.get("/")
async def root():
    return {"message": "Freight Load Search API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/search-loads", response_model=LoadSearchResponse)
async def search_loads(
    request: LoadSearchRequest,
    api_key: str = Depends(verify_api_key)
):
    # Simple matching logic
    matching_loads = []
    
    for load in SAMPLE_LOADS:
        match = True
        
        # Check equipment type
        if request.equipment_type.lower() != load["equipment_type"].lower():
            match = False
        
        # Check origin (simple city match)
        if request.origin_city.lower() not in load["origin"].lower():
            match = False
            
        # Check destination (simple city match) - only if destination is specified
        if request.destination_city and request.destination_city.lower() not in load["destination"].lower():
            match = False
        
        if match:
            matching_loads.append(load)
    
    # Track search metrics (simplified)
    metrics_data["total_searches"] += 1
    if matching_loads:
        metrics_data["successful_matches"] += 1
    else:
        metrics_data["failed_matches"] += 1
    
    return LoadSearchResponse(
        loads=matching_loads,
        load_count=len(matching_loads),
        selected_load_id=matching_loads[0]["load_id"] if matching_loads else None,
        initial_rate=matching_loads[0]["loadboard_rate"] if matching_loads else 0
    )

# Dashboard endpoints
@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Serve the dashboard HTML page"""
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/metrics/dashboard")
async def get_dashboard_metrics_endpoint():
    """Get comprehensive dashboard metrics"""
    return get_dashboard_metrics()

@app.post("/metrics/reset")
async def reset_metrics_endpoint():
    """Reset all metrics to zero (for testing/demo purposes)"""
    reset_metrics()
    return {"status": "metrics reset"}


@app.post("/call-data")
async def receive_call_data(request: Request):
    """Receive call data from HappyRobot and update metrics"""
    try:
        data = await request.json()
        
        # Track the call data
        track_call(data)
        
        return {"status": "call data received", "call_id": datetime.now().strftime("%H:%M:%S")}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing call data: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
