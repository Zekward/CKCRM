from flask import Blueprint, render_template, request
from .data import load_clients, group_clients_by_stage, sort_clients

views = Blueprint('views', __name__)

@views.route('/')

def dashboard():
    # Load all clients from Google Sheets
    clients = load_clients()

    # Get query parameters
    sort_by = request.args.get('sort')
    order = request.args.get('order', 'asc') 
    group_by_stage = request.args.get('group_by') == 'stage'

    # If group view is requested
    if group_by_stage:
        grouped_clients = group_clients_by_stage(clients)

        # Sort each stage group individually
        for stage in grouped_clients:
            grouped_clients[stage] = sort_clients(
                grouped_clients[stage],
                sort_key=sort_by or 'submitted_at', 
                order=order
            )
        
        return render_template(
            'dashboard.html',
            grouped_clients=grouped_clients,
            sort_by=sort_by,
            order=order,
            group_by_stage=True
        )

    # Otherwise, sort flat list
    if sort_by:
        clients = sort_clients(clients, sort_key=sort_by, order=order)

    return render_template(
        'dashboard.html',
        clients=clients,
        sort_by=sort_by,
        order=order,
        group_by_stage=False
    )