from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from passlib.hash import pbkdf2_sha256 as encrypt
from flask_login import LoginManager, UserMixin

app = Flask(__name__)


######## DB stuff start
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///var/all_users.db'
app.config['SECRET_KEY'] = 'secret-key-goes-here'
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)
class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = { 'extend_existing': True }
    username = db.Column(db.Text, primary_key=True) 

######## DB stuff end
  

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        entered_name = request.form.get("login_user")
        entered_password = request.form["login_emailpass"]
        valid = validate_query(entered_name)
        if valid:
            success = validate_credentials(entered_name, entered_password)
            if success:
                return render_template("home.html", userName= entered_name)
            flash("Invalid password. Please try again")
            redirect(url_for("root"))
        else:
            flash("User does not exist. Try logging in with an existing account.")
            redirect(url_for("root"))        
    return render_template('index.html')
  

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
        try: 
            db.session.add(newuser)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            flash(f"Username: {name} is already taken. Please choose a different one.")
            return redirect(url_for("register"))
        
        print(e_mail + name + encrypted_pass)
        return render_template('home.html', userName=name)

    return render_template('register.html')


@app.route('/detail', methods=['GET'])
def detail():
    return render_template('detail.html')
    

################ VALIDATION METHODS
def validate_query(name):
    result = Users.query.filter_by(username=name).first()
    if str(result) ==  "None":
        return False
    return True


def validate_credentials(name, pswd):
    result = Users.query.filter_by(username=name).first()
    if encrypt.verify(pswd, result.password):
        return True
    return False
################ VALIDATION METHODS

if __name__ == '__main__':
   app.run()
   
 