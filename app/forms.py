from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length

class SignUp(FlaskForm):
    username = StringField("username:", validators=[DataRequired(), Length(min = 3)])
    password = PasswordField("password:", validators=[DataRequired(), Length(min = 8, max = 30)])
    submit = SubmitField("sign up")

class SignIn(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min = 3)])
    password = PasswordField("password", validators=[DataRequired(), Length(min = 8, max = 30)])
    submit = SubmitField("sign in")

class AddCharacter(FlaskForm):
    character_name = StringField("character name", validators=[DataRequired()])
    character_gs = SelectField("gear score", choices=[(340, "340"), (460, "460"), (840, "840"), (960, "960"), (1325, "1325"), (1370, "1370"), (1400, "1400")])
    submit = SubmitField("add character")

class DeleteCharacter(FlaskForm):
    delete_character = SelectField("delete", choices=[(1, "yes")])
    submit = SubmitField("delete character?")
