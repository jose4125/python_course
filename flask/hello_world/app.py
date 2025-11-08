from flask import Flask, request, render_template, url_for, redirect, abort, jsonify, session

app = Flask(__name__)

app.secret_key = 'My_secret_key!'

@app.route('/login', methods =['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']

        # add user to the session
        session['username'] = user
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    app.logger.info(f'=== user {session["username"]} logged out successfully')
    session.pop('username')
    return redirect(url_for('login'))

@app.route('/')
def home():
    app.logger.info(f'=== we are in the path: {request.path}')
    has_sesssion = session.get('username') or None

    if 'username' in session:
        app.logger.info(f'=== User {session["username"]} has a session')
        return render_template('home.html', has_sesssion = has_sesssion, username = session['username'])

    return 'User has no session'

@app.route('/hello/<name>')
def hello(name: str):
    return f'Hello {name.upper()}!'

@app.route('/age/<int:age>')
def age(age: int):
    return f'Age is {age}'

@app.route('/show/<name>', methods = ['POST'])
def show_name(name: str):
    return f'your name is: {name}'

@app.route('/show_home/<username>')
def show_home(username: str):
    return render_template('home.html', username = username)

@app.route('/redirect_url')
def redirect_url():
    return redirect(url_for('home'))

@app.route('/redirect_show_home')
def redirect_show_home():
    return redirect(url_for('show_home', name = 'jose'))

@app.route('/api/show_name/<name>')
def api_show_name(name: str):
    return jsonify({
        'data': [
            {'name': name, 'age': 34},
            {'name': 'jose', 'age': 22}
        ]
    })

@app.route('/not_found')
def not_found():
    return abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found_page.html', error = e), 404
