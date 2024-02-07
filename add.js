// Retrieving the token from localStorage
const token = localStorage.getItem('token'); 

        // Adding a submit event listener to the animal form
        document.getElementById('animalForm').addEventListener('submit', function(event) {
            // Preventing the default form submission behavior
            event.preventDefault();
            
            // Creating a new FormData object from the form
            var formData = new FormData(this);
            
            // Sending a POST request to add a new animal with authorization header
            fetch('http://localhost:5001/animal', {
                method: 'POST',
                body: formData,
                headers: {
                    'Authorization': `Bearer ${token}` 
                }
            })
            .then(response => {
                // Checking if the response is OK
                if (response.ok) {
                    // Displaying a message for successfully adding the animal and resetting the form
                    document.getElementById('animalAdicionado').style.display = 'block';
                    this.reset();
                }
            })
            .catch(error => {
                console.error('Erro:', error);
            });
        });