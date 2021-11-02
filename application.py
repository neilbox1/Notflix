from flask import Flask, render_template, request
from flask_sqlalchemy import  SQLAlchemy
from passlib.hash import pbkdf2_sha256 as encrypt
from werkzeug.utils import redirect
app = Flask(__name__)


######## DB stuff start
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///var/all_users.db'
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)
class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = { 'extend_existing': True }
    username = db.Column(db.Text, primary_key=True)   
######## DB stuff end
  

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.args.get('user'):
         return render_template('home.html', userName=request.args.get('user'))

    return render_template('login.html')
  

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'] )
def register():
    if request.method == 'POST':
        name = request.form.get("registerUser")
        e_mail = request.form["emailuser"]
        password = request.form["emailpass"]
        encrypted_pass = encrypt.hash(password)
        newuser = Users(username=name, email=e_mail, password=encrypted_pass)
        db.session.add(newuser)
        db.session.commit()
        print(e_mail + name + encrypted_pass)
        ##### STILL NEED ERROR HANDLING
        return render_template('home.html', userName=name)
        # return redirect()
    # print("Total number of users is", Users.query.count())
    # school = Users.query.filter_by(username='test').first()
    # print("user's name is", school.username)

    return render_template('register.html')
    
@app.route('/login', methods=['GET', 'POST'] )
def login():
    return render_template('login.html')


@app.route('/recommendation', methods=['GET', 'POST'] )
def recommended():
    return render_template('recommendation.html')

if __name__ == '__main__':
   app.run()
   
 