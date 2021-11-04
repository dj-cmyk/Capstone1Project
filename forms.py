from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField, FileField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import InputRequired


class HeadpieceForm(FlaskForm):
    '''docstring'''

    name = StringField('Name', 
                validators=[InputRequired()])
    description = TextAreaField('Description',
                validators=[InputRequired()])
    quantity = IntegerField('Quantity', 
                validators=[InputRequired()])
    image_url = FileField('Image URL Of Headpiece',  
                validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    current_location = StringField('Current Location',
                validators=[InputRequired()])
    storage_location = StringField('Storage Location',
                validators=[InputRequired()])


class SearchForm(FlaskForm):
    '''docstring'''

    production = SelectField('Production Name')
    level = SelectField('Ballet Level')