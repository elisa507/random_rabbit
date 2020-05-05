from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField)


class OptionalFields(FlaskForm):
    """Contact form."""

    min_n = StringField('Min number: ')
    max_n = StringField('Max number: ')
    max_t = StringField('Max number: ')
    submit = SubmitField('Submit')
