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







      function renderProducts(){
          data.forEach((data_entry) => {
          if (data_entry.value){
          render_data.innerHTML += `
                  <div class="cardBorder item">
                    <div>
                      <img src="{{url_for('static', filename='img/prof1.jpg')}}">
                    </div>
                    <div>
                      <h1>test</h1>
                      <h2>test</h2>
                      <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Alias esse culpa rerum, voluptate nisi ea dignissimos consequuntur ipsam ratione iusto nobis voluptatum maxime. Repudiandae, illum voluptate? Dolores, culpa accusantium asperiores ex, sint quia, nam ad animi accusamus ipsa molestiae quidem!</p>
                    </div>
                    <div class="purchaseButton">
                      <button href="{{url_for(${String(data_entry.key)})}}">
                        Learn
                      </button>
                    </div>
                </div>
          `
          }
          else{
              `
              <div class="cardBorder item">
                  <div>
                      <img src="{{url_for('static', filename='img/prof1.jpg')}}">
                  </div>
                  <div>
                      <h1>test</h1>
                      <h2>test</h2>
                      <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Alias esse culpa rerum, voluptate nisi ea dignissimos consequuntur ipsam ratione iusto nobis voluptatum maxime. Repudiandae, illum voluptate? Dolores, culpa accusantium asperiores ex, sint quia, nam ad animi accusamus ipsa molestiae quidem!</p>
                  </div>
                  <div class="purchaseButton">
                  <button href='{{url_for('shoppingcart')}}>
                      Purchase
                  </button>
                  </div>
              </div>
              `
          }
          })  
        }
    







    @app.route('/api/get_data/<user_id>', methods=['GET'])
def get_data(user_id):
    user = load_user(user_id)
    print('hello')
    data = {
        "ownsPython": str(user.javascriptOwner),
        "ownsJava" : str(user.pythonOwner),
        "ownsPython" : str(user.javaOwner)
    }
        #"ownsPython": str(User.query.filter_by(user.username).first().javascriptOwner),
        #"ownsJava" : str(User.query.filter_by(user.username).first().pythonOwner),
        #"ownsPython" : str(User.query.filter_by(user.username).first().ownsJavascript)
    return jsonify(data)









    try:
        form = loginForm()  
        username = form.username.data
        
        user = User.query.filter_by(username=username).first()
        if user is None:
            raise ValueError("User not found")
        

        data = {
            "ownsPython": str(user.pythonOwner),
            "ownsJava": str(user.javaOwner),  # Fixed key
            "ownsJavascript": str(user.ownsJavascript)
        }
        
        return jsonify(data)
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
    







                /*if(value){
              url = `{{ ${user_id}/${getPurchasing(key)} }}`
              buttonText += 'Learn'
            }
            else{
              url = `{{ ${user_id}/shoppingCart(${key}) }}`
              buttonText += `Purchase`
            }
            javascriptOwner = db.Column(db.Boolean, default=False, nullable=False)
            pythonOwner = db.Column(db.Boolean, default=False, nullable=False)
            javaOwner = db.Column(db.Boolean, default=False, nullable= False)*/