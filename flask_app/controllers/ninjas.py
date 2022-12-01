from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja 
from flask_app.models.dojo import Dojo


@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html", all_dojos=Dojo.get_all())

@app.route('/add-ninja', methods=['POST'])
def add_ninja():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect('/dojos')

@app.route('/edit/<int:ninja_id>')
def edit_ninja(ninja_id):
    data = {
        "id": ninja_id 
    }
    ninja=Ninja.get_one_with_dojo(data)
    print("__this is dojo__", ninja.dojo)
    return render_template("edit_ninja.html", ninja=ninja)

@app.route('/update-ninja/<int:ninja_id>/<int:dojo_id>', methods=['POST'])
def update_ninja(ninja_id, dojo_id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "id": ninja_id
    }
    dojo_data = {
        "id": dojo_id
    }

    Ninja.update(data)
    return render_template("dojo_ninjas.html", dojo=Dojo.get_dojo_with_ninjas(dojo_data))


@app.route('/delete/<int:ninja_id>/<int:dojo_id>')
def delete(ninja_id, dojo_id):
    data = {
        "id": ninja_id
    }
    
    dojo_data ={
        "id": dojo_id
    }

    Ninja.destroy(data)
    return render_template("dojo_ninjas.html", dojo=Dojo.get_dojo_with_ninjas(dojo_data))