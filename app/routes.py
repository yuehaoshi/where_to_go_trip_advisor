""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    """ recieved post requests for entry updates """

    data = request.get_json()
    try:
        if "description" in data:
            db_helper.update_task_entry(task_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/tropical", methods=['POST'])
def tropical():
    try:
        data = db_helper.get_tropical_city()
        result = {'success': True, 'response': 'Search City', "res": data}
    except:
        result = {'success': True, 'response': 'Search City'}
    return jsonify(result)


@app.route("/culture", methods=['POST'])
def culture():
    try:
        data = db_helper.get_culture_city()
        result = {'success': True, 'response': 'Search City', "res": data}
    except:
        result = {'success': True, 'response': 'Search City'}
    return jsonify(result)


@app.route("/accommodation", methods=['POST'])
def accommodation():
    try:
        data = db_helper.get_good_accommodation()
        result = {'success': True, 'response': 'Search City', "res": data}
    except:
        result = {'success': True, 'response': 'Search City'}
    return jsonify(result)

@app.route("/searchcity/<string:city_name>", methods=['POST'])
def search_city(city_name):
    try:
        data = db_helper.search_city(city_name)
        result = {'success': True, 'response': 'Search City', "res": data}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/clear", methods=['POST'])
def clear_table():
    return jsonify({'success': True})

@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)