from wtforms import Form
from wtforms import IntegerField, StringField, PasswordField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    id=IntegerField('id')
    nombre=StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4, max=20, message="Ingrese nombre valido")
    ])
    apaterno=StringField("Apaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])
    email=EmailField("Correo", [
        validators.DataRequired(message='El correo es requerido'),
        validators.Email(message="Ingresa correo valido")
    ])