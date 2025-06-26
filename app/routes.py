from flask import Blueprint, render_template
from .data import load_clients

views = Blueprint('views', __name__)

@views.route('/')

def dashboard():
    clients = load_clients()
    return render_template('dashboard.html', clients=clients)