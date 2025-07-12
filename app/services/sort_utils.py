from datetime import datetime

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