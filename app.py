from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

users = {
    'admin': '321123'
}
@app.route('/')
@app.route('/main')
def main():
    if 'username' in session:
        return render_template('main.html', username=session['username'])
    return redirect(url_for('auth'))

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/image')
def image():
    return render_template('image.html')

@app.route('/users')
def users_page():
    return render_template('users.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('main'))
        return 'Неверный логин иили пароль'
    return render_template('auth.html')
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('main'))

@app.route('/listin') 
def listin(): 
    search_list = [ 
        'Дебюсси - Лунный свет',  
        'Нюша - выше', 
        "Stairway to Heaven - Led Zeppelin" 
    ] 
    return render_template('listin.html', search_list=search_list, mytext='Песни')

if __name__ == '__main__':
    app.run(debug=True)
