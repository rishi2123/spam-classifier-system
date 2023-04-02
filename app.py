from flask import Flask,render_template,request,redirect,url_for,session,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'T'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rishi123*'
app.config['MYSQL_DB'] = 'cia2'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    print("Here-0")
    if request.method == 'POST':
        print("Here-1")
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('select * from users where username = %s and password = %s',(username,password))
        us_acc = cursor.fetchone()

        if us_acc:
            print("Here-2")
            return render_template('index.html')
        else:
            return render_template('login.html')

    print("Here-3")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
