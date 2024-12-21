from flask import Blueprint, render_template, flash, redirect, url_for
from utils.form import FormAgenda
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
def index():    
    form = FormAgenda()
    if form.validate_on_submit():
        enviar_dados(resposta=form)
        return redirect(url_for('home.index'))
    return render_template('base.html', form=form)

def enviar_dados(resposta):
    nome = resposta.nome.data
    numero = resposta.numero.data
    email = resposta.email.data
    assunto = resposta.assunto.data
    mensagem = resposta.mensagem.data
    msg = f"O cliente: {nome}, Numero: {numero} enviou uma mensagem: {mensagem}"

    enviar_agendamento(email=email, assunto=assunto, mensagem=msg)
    flash(f"Email enviado como {nome}. Entraremos em contato pelo número {numero}.")

    return redirect(url_for('home.index'))

def enviar_agendamento(email, assunto, mensagem):
    smtp_host = "smtp.gmail.com" 
    smtp_port = 587 
    email_usuario = "gustavoismael1907@gmail.com"
    email_senha = "zvsj czqh uiqx lanu"

    remetente = email_usuario
    destinatario = email
    assunto = assunto
    mensagem = mensagem

    # Criar o corpo do e-mail
    email_msg = MIMEMultipart()
    email_msg["From"] = remetente
    email_msg["To"] = destinatario
    email_msg["Subject"] = assunto
    email_msg.attach(MIMEText(mensagem, "plain"))

    try:
        servidor = smtplib.SMTP(smtp_host, smtp_port)
        servidor.starttls()
        servidor.login(email_usuario, email_senha)
        servidor.sendmail(remetente, destinatario, email_msg.as_string())
    finally:
        servidor.quit()