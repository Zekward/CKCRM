import os
import gspread
import json
import base64



def load_clients():

    creds_base64 = os.getenv('GOOGLE_CREDENTIALS')
    if not creds_base64:
        raise ValueError("Missing GOOGLE_CREDENTIALS")
    
    creds_json = base64.b64decode(creds_base64).decode('utf-8')
    credentials_info = json.loads(creds_json)
    gc = gspread.service_account_from_dict(credentials_info)

    sh = gc.open('MVP CRM Tracker')

    worksheet = sh.sheet1
    rows = worksheet.get_all_records()

    clients = []

    for row in rows:
        clients.append({
            "name": row.get("Name", "N/A"),
                "email": row.get("Email", "N/A"),
                "phone": row.get("Enter your number", "N/A"),
                "car_model": row.get("Make and Model", "N/A"),
                "service": row.get("Which services are you interested in?", "N/A"),
                "stage": "New Lead",  # Default stage for now
                "source": "Typeform",  # Hardcoded source
                "submitted_at": row.get("Submitted At", "N/A"),
        })
    
    return clients