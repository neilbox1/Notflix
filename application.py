from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.args.get('user'):
         return render_template('home.html', userName=request.args.get('user'))
    return render_template('login.html')
  

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET'] )
def register():
    return render_template('register.html')


@app.route('/recommended', methods=['GET', 'POST'] )
def recommended():
    return render_template('recommendation.html')

if __name__ == '__main__':
   app.run()
   
 