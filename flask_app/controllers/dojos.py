from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo


@app.route('/dojos')
def dojos():
    return render_template("dojos.html", all_dojos=Dojo.get_all())

@app.route('/add-dojo', methods=['POST'])
def add_dojo():
    data = {
        "name": request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojo-ninjas/<int:dojo_id>')
def dojo_ninjas(dojo_id):
    data ={
        "id": dojo_id 
    }

    return render_template("dojo_ninjas.html", dojo=Dojo.get_dojo_with_ninjas(data))
