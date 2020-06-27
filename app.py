from flask import Flask, render_template, redirect, url_for, request,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.secret_key='fwekbfkhwehfh132jlhfweh'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///login.db'
db=SQLAlchemy(app)

@app.route('/home')
def welcome():
    return render_template('index.html')  # render a template

# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)