"""Ryan Bui 2331822"""
from flask import Blueprint, render_template
from app.main.forms import EmailForm
from Emailer import em

main_bp = Blueprint("main", __name__, template_folder="templates")

@main_bp.route("/", methods=['POST', 'GET'])
def home():
    """Render the home page."""
    form = EmailForm()
    if form.validate_on_submit():
        em.receiver=form.recipient.data
        form.recipient.data = ''
        return render_template('tracker.html', form=form)
    return render_template('home.html', form=form)

@main_bp.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

@main_bp.route('/tracker', methods=['POST', 'GET']  )
def tracker():
    """Render the email tracker page."""
    form = EmailForm()
    print('hi')
    if form.validate_on_submit():
        em.atacker=form.recipient.data
        em.sendWarning()
        return render_template('error.html')
    return render_template('home.html', form=form)

