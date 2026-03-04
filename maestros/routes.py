from flask import render_template, request, redirect, url_for, flash
from . import maestros
from models import db, Maestros
import forms

@maestros.route("/perfil/maestros", methods=["GET", "POST"])
def perfil(nombre):
    return f"Perfil de  {nombre}"


@maestros.route("/maestros", methods=["GET", "POST"])
def maestros_list():
    create_form = forms.UserForm(request.form)
    maestros = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form = create_form, maestros = maestros)

@maestros.route("/maestros/agregarMaes", methods = ['GET', 'POST'])
def maestros_agregar():
			create_form = forms.UserForm2(request.form)
			if request.method == 'POST':
				maes = Maestros(
                    nombre = create_form.nombre.data,
					apellidos = create_form.apellidos.data,
                    especialidad = create_form.especialidad.data,
					email = create_form.email.data,)
				db.session.add(maes)
				db.session.commit()
				return redirect(url_for('maestros.maestros_list'))
			return render_template("maestros/agregarMaes.html", form = create_form)

@maestros.route("/maestros/detallesMaes", methods = ['GET', 'POST'])
def maestros_detalles():
    if request.method=='GET':
        matricula=request.args.get('matricula')
        #select * from alumnos where id=id
        maes = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
        nombre=maes.nombre
        apellidos=maes.apellidos
        especialidad=maes.especialidad
        email=maes.email
    return render_template('maestros/detallesMaes.html',matricula=matricula,nombre=nombre,apellidos=apellidos,especialidad=especialidad,email=email)

@maestros.route("/maestros/modificarMaes", methods = ['GET', 'POST'])
def maestros_modificar():
		create_form = forms.UserForm2(request.form)
		if request.method=='GET':
			matricula=request.args.get('matricula')
			#select * from maestros where matricula=matricula

			maes = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
			create_form.matricula.data=maes.matricula
			create_form.nombre.data=maes.nombre
			create_form.apellidos.data=maes.apellidos
			create_form.especialidad.data=maes.especialidad
			create_form.email.data=maes.email
		if request.method == 'POST':
			matricula = create_form.matricula.data
			maes = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
			maes.nombre = create_form.nombre.data
			maes.apellidos = create_form.apellidos.data
			maes.especialidad = create_form.especialidad.data
			maes.email = create_form.email.data
			db.session.add(maes)
			db.session.commit()
			return redirect(url_for('maestros.maestros_list'))
		return render_template("maestros/modificarMaes.html", form = create_form)

@maestros.route("/maestros/eliminarMaes", methods = ['GET', 'POST'])
def maestros_eliminar():
		create_form = forms.UserForm2(request.form)
		if request.method=='GET':
			matricula=request.args.get('matricula')
			#select * from maestros where matricula=matricula

			maes = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
			create_form.matricula.data=maes.matricula
			create_form.nombre.data=maes.nombre
			create_form.apellidos.data=maes.apellidos
			create_form.especialidad.data=maes.especialidad
			create_form.email.data=maes.email
		if request.method == 'POST':
			matricula = create_form.matricula.data
			maes = db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
			maes.nombre = create_form.nombre.data
			maes.apellidos = create_form.apellidos.data
			maes.especialidad = create_form.especialidad.data
			maes.email = create_form.email.data
			db.session.delete(maes)
			db.session.commit()
			return redirect(url_for('maestros.maestros_list'))
		return render_template("maestros/eliminarMaes.html", form = create_form)