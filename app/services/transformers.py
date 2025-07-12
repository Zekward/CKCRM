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