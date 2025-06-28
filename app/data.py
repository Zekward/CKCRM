import csv
import os
import gspread


def load_clients():
    gc = gspread.service_account(filename=os.path.join(os.path.dirname(__file__), '..', 'credentials.json'))

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