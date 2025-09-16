async function loadDashboard() {
    try {
        const response = await fetch('/metrics/dashboard');
        const data = await response.json();

                    // Update metrics
                    document.getElementById('total-calls').textContent = data.total_calls;
                    document.getElementById('booking-success-rate').textContent = data.booking_success_rate + '%';

        // Update recent calls and call details
        updateRecentSearches(data.recent_calls);
        updateInquiryDetails(data.latest_call);

    } catch (error) {
        console.error('Error loading dashboard:', error);
    }
}


function updateRecentSearches(calls) {
    const container = document.getElementById('recent-searches-list');
    if (calls.length === 0) {
        container.innerHTML = '<div class="search-item">No recent calls</div>';
        return;
    }

    container.innerHTML = calls.map(call => `
        <div class="search-item">
            <div>
                <div class="search-route">MC: ${call.mc_number || 'N/A'} - ${call.call_outcome || 'Unknown'}</div>
                <div class="search-time">${call.timestamp} - Pickup: ${call.pickup_time || 'Not specified'}</div>
            </div>
            <div class="search-result" style="color: ${getOutcomeColor(call.call_outcome)}">${call.origin_city || 'Unknown'}, ${call.origin_state || 'Unknown'} → ${call.destination_city || 'Any'}, ${call.destination_state || 'Any'}</div>
        </div>
    `).join('');
}

function getOutcomeColor(outcome) {
    switch(outcome) {
        case 'negotiation': return '#f39c12';
        case 'transfer_to_sales': return '#3498db';
        case 'call_ended': return '#e74c3c';
        default: return '#7f8c8d';
    }
}

function updateInquiryDetails(call) {
    const container = document.getElementById('inquiry-details-content');
    if (!call) {
        container.innerHTML = '<div class="no-data">No recent call data available</div>';
        return;
    }

    container.innerHTML = `
        <div class="detail-row">
            <span class="detail-label">Call Time:</span>
            <span class="detail-value">${call.timestamp}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">MC Number:</span>
            <span class="detail-value">${call.mc_number}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Call Outcome:</span>
            <span class="detail-value" style="color: ${getOutcomeColor(call.call_outcome)}; font-weight: bold;">${call.call_outcome}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Carrier Sentiment:</span>
            <span class="detail-value">${call.carrier_sentiment}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Negotiation Rounds:</span>
            <span class="detail-value">${call.negotiation_rounds}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Final Rate:</span>
            <span class="detail-value">$${call.final_rate}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Pickup Time:</span>
            <span class="detail-value">${call.pickup_time}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Origin:</span>
            <span class="detail-value">${call.origin_city}, ${call.origin_state}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Destination:</span>
            <span class="detail-value">${call.destination_city}, ${call.destination_state}</span>
        </div>
        <div class="detail-row">
            <span class="detail-label">Equipment Type:</span>
            <span class="detail-value">${call.equipment_type}</span>
        </div>
    `;
}

// Load dashboard on page load
loadDashboard();


// Prevent any layout shifts
document.addEventListener('DOMContentLoaded', function() {
    // Ensure all elements are properly positioned
    const elements = document.querySelectorAll('.metric-card, .search-item, .detail-row');
    elements.forEach(el => {
        el.style.transform = 'translateZ(0)';
    });
});
