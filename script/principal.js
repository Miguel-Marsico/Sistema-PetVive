// Adding an event listener for when the DOM content is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Adding an event listener for when the DOM content is loaded
    var username = localStorage.getItem('username');

    // Checking if the username exists
    if (username) {
        // Displaying the username in the welcome message element
        document.getElementById('welcomeUser').textContent = username; 
    }
});
