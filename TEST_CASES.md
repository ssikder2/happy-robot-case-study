# Call Flow Test Cases

## Overview
This document outlines 14 comprehensive test cases for the Freight Dynamics Express Inbound Carrier Sales voice AI call flows using HappyRobot.

## Test Environment
- **HappyRobot Campaign**: `https://v2.platform.happyrobot.ai/deployments/bq6illq0wbh8/0u3xukbqeahp`
- **API Integration**: `https://freight-api-happy-robot.fly.dev`
- **Dashboard**: `https://freight-api-happy-robot.fly.dev/dashboard`

---

## Test Case 1: Complete Successful Booking
**Scenario**: Carrier calls, gets verified, finds suitable load, negotiates rate, and books successfully

**Call Flow**:
1. **Greeting**: "Hi, this is Paul from Freight Dynamics Express. How can I help you find a load today?"
2. **MC Verification**: Carrier provides MC number (e.g., "MC123456")
3. **Load Preferences**: 
   - Origin: "Chicago, Illinois"
   - Destination: "Dallas, Texas" 
   - Equipment: "Dry Van"
   - Pickup: "Tomorrow morning"
4. **Load Search**: AI searches and finds matching loads
5. **Load Presentation**: "I found a great load for you - Chicago to Dallas, Dry Van, $2,800"
6. **Negotiation**: Carrier asks for $3,000, AI counters with $2,900
7. **Agreement**: Carrier accepts $2,900
8. **Transfer**: "Perfect! Let me transfer you to our sales team to finalize the booking"

**Expected Result**: 
- Call outcome: `successful_booking`
- Carrier sentiment: `positive`
- Negotiation rounds: 2
- Final rate: $2,900
- Data appears on dashboard

---

## Test Case 2: Quick Acceptance (No Negotiation)
**Scenario**: Carrier immediately accepts the initial rate

**Call Flow**:
1. **Greeting & Verification**: Standard opening
2. **Load Search**: Finds Chicago to Atlanta load at $3,200
3. **Load Presentation**: "I have a Chicago to Atlanta load, Dry Van, $3,200"
4. **Immediate Acceptance**: "That sounds good, I'll take it"
5. **Transfer**: "Excellent! Transferring you to sales now"

**Expected Result**:
- Call outcome: `successful_booking`
- Negotiation rounds: 0
- Final rate: $3,200

---

## Test Case 3: Multi-Round Negotiation
**Scenario**: Extended negotiation with multiple counter-offers

**Call Flow**:
1. **Initial Offer**: $2,500
2. **Carrier Counter**: "I need at least $2,800"
3. **AI Counter**: "I can do $2,650"
4. **Carrier Counter**: "How about $2,750?"
5. **AI Final**: "Best I can do is $2,700"
6. **Agreement**: "Deal!"

**Expected Result**:
- Call outcome: `successful_booking`
- Negotiation rounds: 3
- Final rate: $2,700

---

## Test Case 4: Maximum Rounds Reached
**Scenario**: No agreement after 3 negotiation rounds

**Call Flow**:
1. **Initial Offer**: $2,500
2. **Carrier Counter**: "I need $3,000"
3. **AI Counter**: "I can do $2,600"
4. **Carrier Counter**: "Still need $3,000"
5. **AI Counter**: "Best I can do is $2,700"
6. **Carrier Counter**: "No, I need $3,000"
7. **AI Response**: "I understand. Unfortunately, I can't go that high. I'll keep your information for future loads that might work better."

**Expected Result**:
- Call outcome: `negotiation_failed`
- Negotiation rounds: 3
- Final rate: 0

---

## Test Case 5: Carrier Walks Away
**Scenario**: Carrier decides not to continue after initial offer

**Call Flow**:
1. **Initial Offer**: $2,200
2. **Carrier Response**: "That's too low, I'm not interested"
3. **AI Counter**: "I could potentially go up to $2,400"
4. **Carrier Response**: "No thanks, I'll pass"
5. **AI Response**: "No problem. I'll keep your information for future opportunities."

**Expected Result**:
- Call outcome: `negotiation_failed`
- Negotiation rounds: 1
- Final rate: 0

---

## Test Case 6: Immediate Decline
**Scenario**: Carrier declines without negotiating

**Call Flow**:
1. **Load Presentation**: "I have a Miami to New York load, Reefer, $3,500"
2. **Carrier Response**: "No, I don't do that route"
3. **AI Response**: "I understand. Would you like to hear about other routes I have available?"
4. **Carrier Response**: "No, I'm not interested in any loads right now"
5. **AI Response**: "No problem. I'll keep your information for future opportunities."

**Expected Result**:
- Call outcome: `carrier_declined`
- Negotiation rounds: 0
- Final rate: 0

---

## Test Case 7: Equipment Preference Mismatch
**Scenario**: Carrier's equipment preference doesn't match available loads

**Call Flow**:
1. **Equipment Question**: "What type of equipment do you have available?"
2. **Carrier Response**: "I only have Dry Vans"
3. **Load Search**: AI searches for Dry Van loads
4. **No Matches**: "I don't have any Dry Van loads in your area right now"
5. **AI Response**: "I'll keep your information and call you when I have Dry Van loads available"

**Expected Result**:
- Call outcome: `carrier_declined`
- Negotiation rounds: 0
- Final rate: 0

---

## Test Case 8: Invalid MC Number
**Scenario**: Carrier provides invalid MC number

**Call Flow**:
1. **MC Request**: "What's your MC number?"
2. **Carrier Response**: "MC999999" (invalid)
3. **AI Response**: "I'm having trouble verifying that MC number. Could you double-check it?"
4. **Carrier Response**: "That's what I have"
5. **AI Response**: "I'm unable to verify your MC number in our system. This might be due to a recent registration or system update. I'd suggest calling back in a few hours when our system updates. Is there anything else I can help you with today?"

**Expected Result**:
- Call outcome: `verification_failed`
- No load search attempted
- No negotiation data
- No transfer unless specifically requested

---

## Test Case 9: Call ends early for any reason (hangs up, interrupted, etc.)
**Scenario**: Call drops unexpectedly

**Call Flow**:
1. **Normal Start**: Greeting, verification, load search
2. **Negotiation**: "I can offer $2,600 for that load"
3. **Call Drop**: [Connection lost]

**Expected Result**:
- Call outcome: `technical_issue`
- Partial data captured

---

## Test Case 10: System Error During Load Search
**Scenario**: API error when searching for loads

**Call Flow**:
1. **Normal Start**: Greeting, verification
2. **Load Search**: "Let me search for loads for you..."
3. **System Error**: "I'm experiencing technical difficulties. Let me transfer you to our sales team who can help you directly."

**Expected Result**:
- Call outcome: `technical_issue`
- Graceful error handling

---

## Test Case 11: Unclear MC Number
**Scenario**: Carrier provides unclear MC number, AI clarifies and continues

**Call Flow**:
1. **MC Request**: "What's your MC number?"
2. **Carrier Response**: "I think it's MC one two three four six five" (unclear)
3. **AI Clarification**: "Let me confirm - MC123456?"
4. **Carrier Correction**: "No, it's MC123465"
5. **AI Confirmation**: "Got it, MC123465. Let me verify that for you..."
6. **Verification**: Proceeds normally with corrected number

**Expected Result**:
- Successful verification after clarification and correction
- Normal flow continues with accurate MC number

---

## Test Case 12: Multiple Load Options
**Scenario**: Multiple loads available, carrier needs to choose

**Call Flow**:
1. **Load Search**: Finds 3 matching loads
2. **AI Presentation**: "I have three loads for you: Option 1 - Chicago to Dallas, $2,800; Option 2 - Chicago to Houston, $3,100; Option 3 - Chicago to Atlanta, $2,600. Would you be interested in any of these loads?"
3. **Carrier Choice**: "I'll take Option 2, the Houston one"
4. **Negotiation**: Proceeds with selected load

**Expected Result**:
- Call outcome: `successful_booking`
- Correct load selected and booked

---

## Test Case 13: Alternative Route Request
**Scenario**: Carrier doesn't like initial route but accepts alternative

**Call Flow**:
1. **Load Presentation**: "I have a Miami to New York load, Reefer, $3,500"
2. **Carrier Response**: "No, I don't do that route"
3. **AI Response**: "I understand. Would you like to hear about other routes I have available?"
4. **Carrier Response**: "Sure, what else do you have?"
5. **AI Alternative**: "I have a Miami to Dallas load, Dry Van, $3,200"
6. **Carrier Response**: "That sounds good, I'll take it"
7. **Transfer**: "Perfect! Transferring you to sales now"

**Expected Result**:
- Call outcome: `successful_booking`
- Negotiation rounds: 0
- Final rate: $3,200

---

## Test Case 14: Rate Too High
**Scenario**: Carrier asks for rate higher than available

**Call Flow**:
1. **Load Presentation**: "I have a load for $2,500"
2. **Carrier Request**: "I need at least $4,000"
3. **AI Response**: "I understand, but that's significantly above market rate. The best I can do is $2,600"
4. **Carrier Response**: "No thanks"
5. **AI Response**: "I'll keep your information for higher-paying loads"

**Expected Result**:
- Call outcome: `negotiation_failed`
- Professional handling of unrealistic expectations

---
