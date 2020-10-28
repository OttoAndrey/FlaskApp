from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Email


class CallbackForm(FlaskForm):
    name = StringField('Имя')
    phone_number = StringField('Телефон', validators=[DataRequired()])
    agree = BooleanField('Согласен с условиями', validators=[DataRequired()])


class RequestForm(FlaskForm):
    name = StringField('Имя')
    email = StringField('Почта', validators=[DataRequired(), Email()])
    agree = BooleanField('Согласен с условиями', validators=[DataRequired()])
