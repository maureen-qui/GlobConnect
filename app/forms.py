from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class GroupCreationForm(FlaskForm):
    group_name = StringField('Group Name', validators=[DataRequired()])
    group_description = TextAreaField('Group Description', validators=[DataRequired()])
    submit = SubmitField('Create Group')
