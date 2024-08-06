@app.route('/get_data')
def get_data():
    form = loginForm()
    #dict
    #dict.update({"ownsPython": User.query.filter_by(username = form.username.data).first().javascriptOwner})
    #dict.update({"ownsJava" : User.query.filter_by(username = form.username.data).first().pythonOwner})
    #dict.update({"ownsPython" : User.query.filter_by(username = form.username.data).first().ownsJavascript})
    #dict = jsonify(dict)
    data = {
        "ownsPython": str(User.query.filter_by(username = form.username.data).first().javascriptOwner),
        "ownsJava" : str(User.query.filter_by(username = form.username.data).first().pythonOwner),
        "ownsPython" : str(User.query.filter_by(username = form.username.data).first().ownsJavascript)
    }
    return jsonify(data)