from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

from app.services.data_loader import load_clients, append_new_client
from app.services.transformers import group_clients_by_stage
from app.services.sort_utils import sort_clients

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])

def dashboard():
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        car_model = request.form.get('car_model')
        service = request.form.get('service')
        stage = request.form.get('stage')
        submitted_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source = "Manual"

        # Add client
        append_new_client({
            "Name": name,
            "Email": email,
            "Enter your number": phone,
            "Make and Model": car_model,
            "Which services are you interested in?": service,
            "Status": stage,
            "Source": source,
            "Submitted At": submitted_at
        })

        query_string = request.query_string.decode()
        redirect_url = url_for('views.dashboard')
        if 'group_by=stage' in query_string:
            redirect_url += '?group_by=stage'
        return redirect(redirect_url)
    
    
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