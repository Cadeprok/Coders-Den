const render_data = document.querySelector('renderCourses');
let data = null;
/*const data = fetch('http://localhost:5000/get_data')
    .then((response) => {return response.json()})
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error('Error fetching user data:', error);
    });*/

    try {
        const response = await fetch('http://127.0.0.1:5000/api/get_data');
        const data = await response.json();  // Convert response to JSON

        console.log('Data:', data);

        // return data; 
    } catch (error) {
        console.error('Error:', error);
    }

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




