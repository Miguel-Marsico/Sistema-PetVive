// Adding a submit event listener to the login form
document.getElementById('loginForm').addEventListener('submit', function(event) {
     // Preventing the default form submission behavior
    event.preventDefault();

    // Creating a new FormData object from the form
    var formData = new FormData(this);

    // Sending a POST request to the login endpoint with form data
    fetch('http://localhost:5001/login', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        // Checking if the response is OK
        if (response.ok) {
            return response.json(); 
        } else {
            // Displaying an error message for invalid credentials
            document.getElementById('credenciaisIncorretas').style.display = 'block';
            throw new Error('Credenciais inválidas');
        }
    })
    .then(data => {
        // Storing the username and access token in localStorage
        localStorage.setItem('username', formData.get('username')); 
        localStorage.setItem('token', data.access_token);
        // Redirecting the user to the principal page
        window.location.href = 'principal-page.html';
    })
    .catch(error => {
        // Displaying the error message in the result element
        document.getElementById('result').innerText = error.message;
    });
});
