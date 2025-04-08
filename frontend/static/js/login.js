// User Database Simulation
let users = JSON.parse(localStorage.getItem('users')) || [];

// Login Handler
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    const user = users.find(u => u.email === email && u.password === password);
    
    fetch("/api/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw new Error(err.message || "Login failed"); });
        }
        return response.json();
    })
    .then(data => {
        localStorage.setItem("token", data.token);
        window.location.href = "dashboard.html";
    })
    .catch(error => {
        document.getElementById("error-message").innerText = error.message;
        document.getElementById("error-message").style.display = "block";
    });
});

// Registration Handler
document.getElementById('registerForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const newUser = {
        name: formData.get(0),
        email: formData.get(1),
        password: formData.get(2)
    };

    if(users.some(u => u.email === newUser.email)) {
        alert('User already exists with this email!');
        return;
    }

    users.push(newUser);
    localStorage.setItem('users', JSON.stringify(users));
    alert('Registration successful! Please login.');
    this.reset();
});

// Session Check
window.addEventListener('load', () => {
    const currentUser = localStorage.getItem('currentUser');
    if(currentUser) {
        window.location.href = 'dashboard.html';
    }
});

// Form Validation
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', (e) => {
        if(!form.checkValidity()) {
            e.preventDefault();
            alert('Please fill all required fields!');
        }
    });
});