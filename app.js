// const element = document.getElementById('output');


fetch('/get_data')
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => {
        console.error('Error fetching user data:', error);
    });