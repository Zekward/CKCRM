import os
import gspread
import json
import base64


def get_gspread_client():
    """ Decode environment-stored credentials and return gspread client """
    creds_base64 = os.getenv('GOOGLE_CREDENTIALS')
    if not creds_base64:
        raise ValueError("Missing GOOGLE_CREDENTIALS")
    
    creds_json = base64.b64decode(creds_base64).decode('utf-8')
    credentials_info = json.loads(creds_json)
    
    return gspread.service_account_from_dict(credentials_info)

def get_sheet_records(sheet_name='MVP CRM Tracker'):
    """ Fetch all records from from the first worksheet in a given Google Sheet."""
    gc = get_gspread_client()
    sh = gc.open(sheet_name)
    worksheet = sh.sheet1
    return worksheet.get_all_records()

def transform_row_to_client(row):
    """ Convert gs row to structured client dictionary """
    return {
        "name": row.get("Name", "N/A"),
        "email": row.get("Email", "N/A"),
        "phone": row.get("Enter your number", "N/A"),
        "car_model": row.get("Make and Model", "N/A"),
        "service": row.get("Which services are you interested in?", "N/A"),
        "stage": row.get("Status", "New Lead"),
        "source": "Typeform",  # Hardcoded source
        "submitted_at": row.get("Submitted At", "N/A"),
    }

def group_clients_by_stage(clients):
    stages = ["New Lead", "Contact", "Booked", "Closed", "Ghosted", "Followed Up"]
    grouped = {stage: [] for stage in stages}

    for client in clients:
        stage = client.get("stage", "New Lead")
        if stage in grouped:
            grouped[stage].append(client)
        else:
            grouped.setdefault(stage, []).append(client)
    
    return grouped

def sort_clients(clients, sort_key, order="asc"):
    reverse = (order == "desc")

    def safe_key(client):
        if not isinstance(client, dict):
            return ""
        value = client.get(sort_key, "")
        if sort_key == "submitted_at":
            from datetime import datetime
            try:
                return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            except:
                return datetime.min
        return value.lower() if isinstance(value, str) else value

    return sorted(clients, key=safe_key, reverse=reverse)


def load_clients():
    rows = get_sheet_records()
    clients = [transform_row_to_client(row) for row in rows]

    return clients

