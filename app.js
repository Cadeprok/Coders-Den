const render_data = document.querySelector('renderCourses');

const data = fetch('/get_data')
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error('Error fetching user data:', error);
    });


function renderProducts(){
    data.forEach((data_entry) => {
    if (data_entry.value){
    render_data.innerHTML += `
    `
    }
    else{

    }
    })  
}
