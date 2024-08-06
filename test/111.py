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