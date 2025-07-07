from data import group_clients_by_stage

def test_group_clients_by_stage():
    test_clients = [
        {"name": "Alice", "stage": "New Lead"},
        {"name": "Bob", "stage": "Contacted"},
        {"name": "Carol", "stage": "New Lead"},
        {"name": "Dave", "stage": "Booked"},
        {"name": "Eve", "stage": "Followed Up"},
        {"name": "Frank", "stage": "Closed"},
        {"name": "Gina", "stage": "Unknown Stage"}
    ]

    result = group_clients_by_stage(test_clients)

    for stage, clients in result.items():
        print(f"{stage}: {[c['name'] for c in clients]}")
    

if __name__ == "__main__":
    test_group_clients_by_stage()