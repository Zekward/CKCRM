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