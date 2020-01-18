from flask import render_template, request, session, url_for, flash, redirect
from sensorapp import app, mongo ,usermodel


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username=request.form['username']
        password=request.form['pass']
        if usermodel.validate(username,password):
            session['user']=username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html')

@app.route("/dashboard",methods=['GET'])
def dashboard():
    if request.method == 'GET' or request.method == 'POST':
        loggedin='user' in  session
        return render_template('dashboard.html', loggedin=loggedin)

@app.route("/live-dashboard",methods=['GET'])
def livedashboard():
    if request.method == 'GET' or request.method == 'POST':
        return render_template('livedashboard.html')

@app.route("/history-dashboard",methods=['GET'])
def historydashboard():
    loggedin='user' in  session
    if request.method == 'GET' or request.method == 'POST':
        return render_template('hisotrydashboard.html', loggedin=loggedin)

@app.route("/equipment",methods=['GET'])
def equipment():
    loggedin = 'user' in session
    if request.method == 'GET' or request.method == 'POST':
        return render_template('equipments.html', loggedin=loggedin)

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html',roles=['admin','normal'])
    else:
        username=request.form['username']
        password=request.form['pass']
        role=request.form['roles']
        doc={'_id':username,'user':username,'password':password,'role':role}
        id=usermodel.addUserData(doc)
        return redirect(url_for('home'))

@app.route("/logout",methods=['GET'])
def logout():
    session.pop('user',None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)