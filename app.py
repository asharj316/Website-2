from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Home')
def home():
    return render_template('Home.html')

@app.route('/About')
def about():
    return render_template('About us.html')

@app.route('/Membership')
def Membership():
    return render_template('Membership.html')

if __name__ == '_main_':
    app.run(debug=True)