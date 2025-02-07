from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

#VALIDACIONES PERSONALIZADAS

def no_palabra(form, field):

    if field.data == 'admin':
        raise ValidationError('El campo username no puede ser admin')
    if not field.data[0].isalpha():
        raise ValidationError('No se puede empezar por algo que no sea una letra')

class Persona(FlaskForm):

    username = StringField('username', validators=[DataRequired(), Length(min=3, max=10), no_palabra])

    email = EmailField('email', validators=[DataRequired(),Length(min=5, max=12), Email()])

    telefono = StringField('telefono', validators=[DataRequired(),Length(min=9, max=14)])

    password = PasswordField('contraseña', validators=[DataRequired(), Length(min=8, max=12),EqualTo('confirm', message='Password must be the same, tontopolla')])

    confirm = PasswordField('Repeat password', validators=[
        DataRequired(),
        Length(min=8, max=14),
    ])

    submit = SubmitField('Enviar')

class PersonaMacro(FlaskForm):

    username = StringField('username', validators=[DataRequired(), Length(min=3, max=10), no_palabra])

    email = EmailField('email', validators=[DataRequired(),Length(min=5, max=12), Email()])

    telefono = StringField('telefono', validators=[DataRequired(),Length(min=9, max=14)])

    password = PasswordField('contraseña', validators=[DataRequired(), Length(min=8, max=12),EqualTo('confirm', message='Password must be the same, tontopolla')])

    confirm = PasswordField('Repeat password', validators=[
        DataRequired(),
        Length(min=8, max=14),
    ])

    submit = SubmitField('Enviar')