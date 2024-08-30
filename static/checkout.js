import { courses } from './courses.js';
    const render_checkout = document.getElementById("render_cart_data");
    const buyingElement = document.querySelector(".variableStorage");
    console.log(purchasing);
    console.log(buyingElement);
    for (var i = 0; i < courses.length; i++){
        const iteration = courses[i];
        if(iteration.name === purchasing){
        render_cart_data.innerHTML += `
            <div class="center-screen">
                    <div class="checkOutContainer">
                        <div class="center">
                                {{ form.hidden_tag() }}
                            <div class="margin">
                                <div class="checkoutTop item">
                                    {{ form.cc_number }}
                                </div>
                                <div class="checkoutMiddle item">
                                    {{ form.first_name }}
                                    {{ form.last_name }}
                                    {{ form.expiration_date }}
                                </div>
                                <div class="checkoutBottom item">
                                    {{ form.security_code }}
                                    {{ form.purchasing }}
                                    
                                </div>




                                <div style='text-align: center; padding-top: 20px;'>
                                    <div style='display: inline-block; vertical-align: top;'>
                                        <img src="{{ url_for('static', filename='${iteration.img_source}') }}" style="height:50%; width: 50%;">
                                    </div>
                                    <div>
                                        Price: $${iteration.cost}
                                    </div>
                                </div>
                                <div class="submit item">
                                    {{ form.submit }}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `
    }
}