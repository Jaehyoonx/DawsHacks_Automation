from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class EmailForm(FlaskForm):
    """Form for entering an email address."""
    recipient = StringField(
        "Recipient Email",
        validators=[DataRequired(), Email(message="Invalid email address")]
    )
    submit = SubmitField("Search")
