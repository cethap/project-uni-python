from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
  if not session.get('logged_in'):
    return render_template('login.html')
  else:
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
  if request.form['password'] == 'password' and request.form['username'] == 'admin':
    session['logged_in'] = True
  else:
    flash('wrong password!')
  return index()

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)