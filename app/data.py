import csv
import os

def load_clients():
    clients = []
    csv_path = os.path.join(os.path.dirname(__file__), 'typeform_leads_test.csv')

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
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