    <script type="text/javascript">
      render_data.innerHTML = ``;
      const user_id = "{{ user_id }}";
      var purchasing = '';
      const url = `/get_data/${user_id}`
      
      function getPurchasing(key){
        if (key === 'pythonOwner'){
          return 'python';
        }
        else if(key === 'javascriptOwner'){
          return 'javascript';
        }
        else{
          return 'java';
        }
      }

      function getCourse(key){
        if(key === 'ownsJava'){
          return 'javacourse';
        }
        else if(key === 'ownsJavascript'){
          return 'javascriptcourse';
        }
        else{
          return 'pythoncourse';
        }
      }


      async function fetchAndRenderData() {
        try {
          const response = await fetch(url);
          if(!response.ok){
            throw new Error('Network response was not ok');
          }
          data = await response.json();  // Convert response to JSON
          console.log(1);
          console.log(data);
          console.log(2);

        } catch (error) {
            console.error('Error:', error);
        }
        console.log(data);
        // return data;

        let user_url;
        let buttonText;
        let count = 0;
          for(const [key, values] of Object.entries(data)){
            count += 1;
            
            if(values){
              // userdash/${user_id}
              purchasing = getCourse(key);
              user_url = `/userdash/${user_id}/${purchasing}`;
              buttonText = 'Learn';
            }
            else{
              user_url = `/checkout`;
              buttonText = 'Purchase';
            }
            render_data.innerHTML += 
                `<div class="cardBorder item">
                    <div>
                      <img src="{{ url_for('static', filename='img/prof1.jpg') }}">
                    </div>
                    <div>
                      <h1>test</h1>
                      <h2>test</h2>
                      <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Alias esse culpa rerum, voluptate nisi ea dignissimos consequuntur ipsam ratione iusto nobis voluptatum maxime. Repudiandae, illum voluptate? Dolores, culpa accusantium asperiores ex, sint quia, nam ad animi accusamus ipsa molestiae quidem!</p>
                    </div>
                    <div class="purchaseButton">
                      <a href="${user_url}">
                        <button tyle="submit" id="sendInformation">
                            ${buttonText}
                        </button>
                      </a>
                    </div>
                </div>`


      }
    }
    sendInformation.addEventListener('submit', function(e){
        e.preventDefault();
        const purchasingValue = purchasing.value;

        localStorage.setItem('purchasing-value',purchasingValue);

        window.location.href= "../checkout.html";
      })


      /*function renderContent(renderData){
          console.log(renderData);
          data = Object.entries(renderData);
          console.log(data);
          let url;
          let buttonText;

          for(const [key, values] of data){
            if(key == 'javascriptOwner' )
            for(const [key, value] of data){
              console.log(4);
              console.log(key + ' : ' + value + '1');
              console.log(5);
              if(value === 'True'){
                url = `${user_id}/${getCourse(key)}`;
                buttonText = 'Learn';
              }
              else{
                url = `shoppingcart`;
                buttonText = 'Purchase';
              }
              console.log(key + ':' + value)

      }
    }*/
      //console.log('fetchData');
      // let renderData = fetchData();
      // console.log('renderData');
      fetchAndRenderData();
  </script>