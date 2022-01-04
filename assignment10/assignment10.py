from flask import Blueprint, render_template, request, redirect
from interact_with_DB import interact_db

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')

@assignment10.route('/assignment10')
def index():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', usersList=users)

@assignment10.route('/new_name', methods=["post"])
def change_name():
    name = request.form['userName']
    email = request.form['userEmail']
    query = "UPDATE users SET name='%s' WHERE email='%s';" % (name,email)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

@assignment10.route('/new_email', methods=["post"])
def change_email():
    name = request.form['userName']
    email = request.form['userEmail']
    query = "UPDATE users SET email='%s' WHERE name='%s';" % (email,name)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

@assignment10.route('/insert_to_db', methods=["post"])
def insert_func():
    name = request.form['userName']
    email = request.form['userEmail']
    query = "INSERT INTO users(name,email) VALUES ('%s', '%s' );" %(name, email)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

@assignment10.route('/delete_from_db', methods=["post"])
def delete_func():
    id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % id
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

