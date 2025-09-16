from datetime import datetime

# In-memory metrics storage (in production, use a database)
metrics_data = {
    "total_searches": 0, # Kept for search-loads endpoint, but not displayed on dashboard
    "successful_matches": 0,
    "failed_matches": 0,
    "total_calls": 0,
    "negotiations": 0,
    "transfers_to_sales": 0,
    "calls_ended": 0,
    "search_history": [], # This now stores call records only
}

def track_call(call_data):
    """Track a call event in metrics"""
    # Update call metrics
    metrics_data["total_calls"] += 1
    
    # Update specific metrics based on call outcome
    if call_data.get("call_outcome") == "negotiation":
        metrics_data["negotiations"] += 1
    elif call_data.get("call_outcome") == "transfer_to_sales":
        metrics_data["transfers_to_sales"] += 1
    elif call_data.get("call_outcome") == "call_ended":
        metrics_data["calls_ended"] += 1
    
    # Add to call history
    call_record = {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "call_outcome": call_data.get("call_outcome", "unknown"),
        "carrier_sentiment": call_data.get("carrier_sentiment", "neutral"),
        "negotiation_rounds": call_data.get("negotiation_rounds", 0),
        "final_rate": call_data.get("final_rate", 0),
        "mc_number": call_data.get("mc_number", "N/A"),
        "pickup_time": call_data.get("pickup_time", "Not specified"),
        "origin_city": call_data.get("origin_city", "Unknown"),
        "origin_state": call_data.get("origin_state", "Unknown"),
        "destination_city": call_data.get("destination_city", "Any"),
        "destination_state": call_data.get("destination_state", "Any"),
        "equipment_type": call_data.get("equipment_type", "Unknown")
    }
    
    metrics_data["search_history"].append(call_record)
    
    # Keep only last 100 calls
    if len(metrics_data["search_history"]) > 100:
        metrics_data["search_history"] = metrics_data["search_history"][-100:]

def get_dashboard_metrics():
    """Get comprehensive dashboard metrics"""
    # Get recent calls (all except the most recent one since it's shown above)
    # Only show calls that have actual call data (not search data)
    recent_calls = []
    if len(metrics_data["search_history"]) > 1:
        # Filter to only show actual call records (those with call_outcome)
        call_records = [call for call in metrics_data["search_history"] if "call_outcome" in call]
        if len(call_records) > 1:
            recent_calls = call_records[:-1][::-1]  # Exclude the most recent call, show all others

    # Get latest call details (only if it's an actual call record)
    latest_call = None
    if metrics_data["search_history"]:
        latest_record = metrics_data["search_history"][-1]
        # Only show if it's a call record (has call_outcome)
        if "call_outcome" in latest_record:
            latest_call = {
                "timestamp": latest_record["timestamp"],
                "mc_number": latest_record.get("mc_number", "N/A"),
                "call_outcome": latest_record.get("call_outcome", "Unknown"),
                "carrier_sentiment": latest_record.get("carrier_sentiment", "Unknown"),
                "negotiation_rounds": latest_record.get("negotiation_rounds", 0),
                "final_rate": latest_record.get("final_rate", 0),
                "pickup_time": latest_record.get("pickup_time", "Not specified"),
                "origin_city": latest_record.get("origin_city", "Unknown"),
                "origin_state": latest_record.get("origin_state", "Unknown"),
                "destination_city": latest_record.get("destination_city", "Any"),
                "destination_state": latest_record.get("destination_state", "Any"),
                "equipment_type": latest_record.get("equipment_type", "Unknown")
            }

    # Calculate booking success rate (successful bookings out of total calls)
    # Only count actual call records
    call_records = [call for call in metrics_data["search_history"] if "call_outcome" in call]
    successful_bookings = sum(1 for call in call_records 
                            if call.get("call_outcome") == "successful_booking")
    total_calls = len(call_records)
    booking_success_rate = (successful_bookings / total_calls * 100) if total_calls > 0 else 0

    return {
        "total_calls": metrics_data["total_calls"],
        "booking_success_rate": round(booking_success_rate, 1),
        "recent_calls": recent_calls,
        "latest_call": latest_call
    }

def reset_metrics():
    """Reset all metrics to zero"""
    global metrics_data
    metrics_data = {
        "total_searches": 0,
        "successful_matches": 0,
        "failed_matches": 0,
        "total_calls": 0,
        "negotiations": 0,
        "transfers_to_sales": 0,
        "calls_ended": 0,
        "search_history": [],
    }