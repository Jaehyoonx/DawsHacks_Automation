"""Ryan Bui 2331822"""
from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__, template_folder="templates")


@main_bp.route("/")
def home():
    """Render the home page."""
    context = {
        'main_heading': 'Home'
    }
    return render_template('home.html', context=context)

@main_bp.route('/about')
def about():
    """Render the about page."""
    context = {
        'main_heading': 'About Us'
    }
    return render_template('about.html', context=context)

@main_bp.route('/tracker')
def tracker():
    """Render the email tracker page."""
    context = {
        'main_heading': 'Email Tracker'
    }
    return render_template('tracker.html', context=context)