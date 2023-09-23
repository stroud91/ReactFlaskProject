from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

ALLOWED_EXTENSIONS = {'jpg', 'png'}

# is image extension valid?
def valid_image_url(form, field):
    file = field.data
    if '.' in file and file.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
        raise ValidationError("Invalid Image File Extension")

class NewImage(FlaskForm):
    image_url = StringField('image_url', validators=[DataRequired(), valid_image_url])
    image_preview = BooleanField('image_preview', validators=[DataRequired()])
    submit = SubmitField('submit')