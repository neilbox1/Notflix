from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.args.get('emailuser'):
         return render_template('home.html', userName=request.args.get('emailuser'))
    return render_template('login.html')
  

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

if __name__ == '__main__':
   app.run()
   
 