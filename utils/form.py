from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField
from wtforms.validators import DataRequired

class FormAgenda(FlaskForm):
    nome = StringField(validators=[DataRequired()])
    numero = IntegerField(validators=[DataRequired()])
    email = EmailField(validators=[DataRequired()])
    assunto = StringField(validators=[DataRequired()])
    mensagem = StringField(validators=[DataRequired()])
    submit = SubmitField('Agendar')