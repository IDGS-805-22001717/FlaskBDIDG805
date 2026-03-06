from flask import render_template, request, redirect, url_for, flash
from . import cursos
from models import Alumnos, Maestros, db, Cursos
import forms

@cursos.route("/perfil/cursos", methods=["GET", "POST"])
def perfil(nombre):
    return f"Perfil de  {nombre}"


@cursos.route("/cursos", methods=["GET", "POST"])
def cursos_list():
    create_form = forms.UserForm(request.form)
    cursos = Cursos.query.all()
    return render_template("cursos/listadoCurs.html", form = create_form, cursos = cursos)

@cursos.route("/cursos/crearCurs", methods=['GET', 'POST'])
def cursos_crear():
    maestros_disponibles = Maestros.query.all()
    
    if request.method == 'POST':
        nuevo_curso = Cursos(
            nombre=request.form.get('nombre'),
            descripcion=request.form.get('descripcion'),
            maestro_id=request.form.get('maestro_id')
        )
        db.session.add(nuevo_curso)
        db.session.commit()
        return redirect(url_for('cursos.cursos_list'))
        
    return render_template("cursos/crearCurs.html", maestros=maestros_disponibles)

@cursos.route("/cursos/inscribirAlum", methods=['GET', 'POST'])
def inscribir_alumno():
    if request.method == 'POST':
        curso_id = request.form.get('curso_id')
        alumno_id = request.form.get('alumno_id')
        
        curso = db.session.query(Cursos).filter(Cursos.id == curso_id).first()
        alumno = db.session.query(Alumnos).filter(Alumnos.id == alumno_id).first()
        
        if curso and alumno:
            if alumno not in curso.alumnos:
                curso.alumnos.append(alumno)
                db.session.commit()
            
        return redirect(url_for('cursos.detalles_curso', id=curso.id))
    
    cursos_lista = Cursos.query.all()
    alumnos_lista = Alumnos.query.all()
    return render_template("cursos/inscribirAlum.html", cursos=cursos_lista, alumnos=alumnos_lista)

@cursos.route("/cursos/detallesCurs", methods=['GET'])
def detalles_curso():
    curso_id = request.args.get('id')
    curso = db.session.query(Cursos).filter(Cursos.id == curso_id).first()
    
    if not curso:
        return redirect(url_for('cursos.cursos_list'))

    todos_los_alumnos = Alumnos.query.all()
    
    alumnos_disponibles = [alumno for alumno in todos_los_alumnos if alumno not in curso.alumnos]
    
    return render_template("cursos/detalleCurs.html", curso=curso, alumnos_disponibles=alumnos_disponibles)

@cursos.route("/cursos/perfil_alumno", methods=['GET'])
def perfil_alumno():
    
    alumno_id = request.args.get('id')
    alumno = db.session.query(Alumnos).filter(Alumnos.id == alumno_id).first()
    
    
    return render_template("cursos/perfil_alumno.html", alumno=alumno)
