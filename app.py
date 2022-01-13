from flask import Flask, render_template, redirect, url_for, request, session, jsonify
import requests
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key='123'

from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


Users_dict = {'user1': {'name': 'Lior', 'email': 'lior@gmail.com'}, 'user2': {'name': 'Hila', 'email': 'hila@gmail.com'},
         'user3': {'name': 'Daniel', 'email': 'daniel@gmail.com'}, 'user4': {'name': 'Gadi', 'email': 'gadi@gmail.com'},
         'user5': {'name': 'Gaya', 'email': 'gaya@gmail.com'}}

@app.route('/')
def cv_Page():
    flag=True
    if flag:
        return render_template('cv.html')
    else:
        return redirect(url_for('movies_templates'))

@app.route('/assignment8')
def movies_templates():
    #DB
    return render_template('assignment8.html', MoviesList=('The Ugly Truth','The Curious Case of Benjamin Button','The Avengers','X-Men'))


@app.route('/assignment9', methods=['POST', 'GET'])
def assignment9_func():
    if request.method == 'GET':
        if 'Email' in request.args:
            useremail = request.args['Email']
            if useremail != "":
                for j in Users_dict:
                    if useremail in Users_dict[j].values():
                        return render_template('assignment9.html', foundUser=Users_dict[j])
                    else:
                        return render_template('assignment9.html', notFound='error')
            else:
                return render_template('assignment9.html', allUsers=Users_dict)
        else:
            return render_template('assignment9.html')

    if request.method == 'POST':
        if ' logOut ' in request.form:
            session['userName'] = ''
        if 'username' in request.form:
            username = request.form['username']
            session['userName'] = username
            return redirect('/assignment9')
        return render_template('assignment9.html')

@app.route('/assignment11/users')
def users_json_func():
    users_dict = {}
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    for user in users:
        users_dict[f'user_{user.id}'] = {
            'name': user.name,
            'email': user.email,
        }
    return jsonify(users_dict)

def user_by_id(id):
    res = requests.get(f'https://reqres.in/api/users/{id}')
    res_json = res.json()
    return res_json



@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def req_func():
    if "user_id" in request.args:
        if request.args['user_id'] == '':
            return render_template('assignment11.html', dict='')
        user_req = int(request.args['user_id'])
        user = user_by_id(user_req)
    else:
        user = ''
    return render_template('assignment11.html', dict=user)


if __name__ == '__main__':
    app.run()
