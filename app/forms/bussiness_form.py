from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from urllib.parse import urlparse
from app.models import Business


def business_name_exists(form, field):
    business_name = field.data
    business = Business.query.filter(Business.name == business_name).first()
    if business:
        raise ValidationError("Business with this name already exists.")

def valid_zip_code(form, field):
    if not field.data.isdigit() or len(field.data) != 5:
        raise ValidationError("Invalid ZIP Code.")

def valid_phone_number(form, field):
    if not field.data.isdigit() or len(field.data) != 10:
        raise ValidationError("Invalid phone number.")


# def valid_url(form, field):
#     try:
#         result = urlparse(field.data)
#         if not all([result.scheme, result.netloc]):
#             raise ValueError()
#     except ValueError:
#         raise ValidationError("Invalid URL.")



class BusinessForm(FlaskForm):
    # class Meta:
    #     csrf = False
    name = StringField('Business Name', validators=[
        Length(min=1, max=50),
        DataRequired(),
        business_name_exists
    ])

    address = StringField('Address', validators=[
        Length(min=1, max=255),
        DataRequired()
    ])

    city = StringField('City', validators=[
        Length(min=1, max=50),
        DataRequired()
    ])

    state = StringField('State', validators=[
        Length(min=1, max=25),
        DataRequired()
    ])

    zip_code = StringField('Zip Code', validators=[
        Length(min=1, max=10),
        DataRequired(),
        valid_zip_code
    ])

    phone_number = StringField('Phone Number', validators=[
        Length(min=1, max=30),
        DataRequired(),
        valid_phone_number
    ])

    category_id = IntegerField('Category ID', validators=[DataRequired()])

    owner_id = IntegerField('Owner ID', validators=[DataRequired()])

    website = StringField('Website', validators=[
        Length(min=1, max=255),
        DataRequired(),
        # valid_url
    ])

    about = StringField('About', validators=[
        Length(min=1, max=500),
        DataRequired()
    ])

    type = StringField('Type', validators=[
        Length(min=1, max=255),
        DataRequired()
    ])
