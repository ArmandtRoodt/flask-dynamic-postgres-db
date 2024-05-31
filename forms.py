from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateDatabaseForm(FlaskForm):
    db_name = StringField('Database Name', validators=[DataRequired()])
    submit = SubmitField('Create Database')
