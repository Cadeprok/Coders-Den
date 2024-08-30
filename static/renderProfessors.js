const professor_information = [
    {
        'id' : 0,
        'name' : 'Mia Collins',
        'img_src' : '../static/img/prof1.jpg',
        'description' : 'Specializes in cybersecurity policy, risk management, and coding best practices for secure software development. Known for her strategic insights and engaging lectures.',
        'credentials' : 'Masters in Information Systems, PhD in Cybersecurity'
    },
    {
        'id' : 1,
        'name' : 'Liam Thompson',
        'img_src' : '../static/img/prof2.webp',
        'description' : 'Focuses on cybersecurity data analytics, machine learning applications, and secure coding practices. Renowned for his hands-on approach and data-driven teaching style.',
        'credentials' : 'Masters in Data Science, PhD in Cybersecurity'
    },
    {  
        'id' : 2,
        'name' : 'Noah Bennett',
        'img_src' : '../static/img/prof3.jpg',
        'description' : 'Expert in hardware security, embedded systems, and secure coding for hardware-related applications. Recognized for his innovative research and practical, lab-based instruction.',
        'credentials' : 'Masters in Computer Engineering, PhD in Information Security'
    }
];


const instructorElement = document.getElementById('instructors');


for (let i = 0; i < professor_information.length; i++){
    let professor = professor_information[i];
    instructorElement.innerHTML += `
                <div class="card" style="width: 18rem;">
                    <img class="card-img-top" src="${professor['img_src']}" alt="Card image cap">
                    <div class="card-body">
                    <h5 class="card-title">${professor['name']}</h5>
                    <p class="card-text"> ${professor['description']} </p>
                    </div>
                    <ul class="list-group list-group-flush">
                    <li class="list-group-item"> ${professor['credentials']} </li>
                    </ul>
                </div>  
    `
};
