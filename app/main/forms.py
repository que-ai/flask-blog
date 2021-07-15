"""
Form表单
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    """
    定义表单类
    """
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
