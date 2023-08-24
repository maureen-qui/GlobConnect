from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for users (Replace with a database in the actual app)
users = []

@app.route('/')
def index():
    return 'Welcome to BizCollab App'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users.append({'username': username, 'password': password})
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = next((u for u in users if u['username'] == username and u['password'] == password), None)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session['username'] = user['username']
            return f'Welcome, {user["username"]}!'  
      else:
            return 'Invalid credentials. Please try again.'
    return render_template('login.html')

@app.route('/logout')
  def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
