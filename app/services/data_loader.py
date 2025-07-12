from .gspread_client import get_gspread_client
from .transformers import transform_row_to_client

def get_sheet_records(sheet_name='MVP CRM Tracker'):
    """ Fetch all records from from the first worksheet in a given Google Sheet."""
    gc = get_gspread_client()
    sh = gc.open(sheet_name)
    worksheet = sh.sheet1
    return worksheet.get_all_records()

def load_clients():
    rows = get_sheet_records()
    clients = [transform_row_to_client(row) for row in rows]
    return clients

def append_new_client(client_data):
    gc = get_gspread_client()
    sheet = gc.open('MVP CRM Tracker').sheet1

    row = [
        client_data.get("Name", ""),
        client_data.get("Email", ""),
        client_data.get("Enter your number", ""), 
        client_data.get("Make and Model", ""),
        client_data.get("Which services are you interested in?", ""),
        "",  # Message (optional)
        client_data.get("Submitted At", ""),
        "",  # Token (leave empty)
        client_data.get("Status", "New Lead")
    ]

    sheet.append_row(row)