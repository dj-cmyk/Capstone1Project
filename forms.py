from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, IntegerField, FileField, BooleanField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import InputRequired, AnyOf


class PropAndHeadpieceForm(FlaskForm):
    '''docstring'''

    name = StringField('Name', 
                validators=[InputRequired()])
    description = TextAreaField('Description',
                validators=[InputRequired()])
    quantity = IntegerField('Quantity', 
                validators=[InputRequired()])
    image_url = FileField('Image URL Of Headpiece',  
                validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    current_location = StringField('Current Location',
                validators=[InputRequired()])
    storage_location = StringField('Storage Location',
                validators=[InputRequired()])


class ProductionForm(FlaskForm):
    '''docstring'''

    name = StringField('Name', 
                validators=[InputRequired()])
    last_performed = IntegerField('Year of Last Performance')
    image_url = FileField('Image URL Of Production', 
                validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    is_current = BooleanField('Is Current Production', 
                default=False, validators=[AnyOf([True, False])])


 
