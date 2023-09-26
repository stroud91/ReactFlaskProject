from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "gif"}

# is image extension valid?
def valid_image_url(form, field):
    file = field.data
    if '.' in file and file.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
        raise ValidationError("Invalid Image File Extension")

class NewImage(FlaskForm):
    # image_url = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    image_url = StringField("image_url", validators=[DataRequired()])
    image_preview = StringField('image_preview', validators=[DataRequired()])
    submit = SubmitField('submit')