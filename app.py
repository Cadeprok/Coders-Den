from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')   



if __name__ == '__main__':
    app.run(debug=True)


# https://www.geeksforgeeks.org/login-and-registration-project-using-flask-and-mysql/
# https://www.youtube.com/watch?v=2mbHyB2VLYY