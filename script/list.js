// Adding an event listener for when the DOM content is loaded
document.addEventListener('DOMContentLoaded', function() {
     // Retrieving the token from localStorage
    const token = localStorage.getItem('token'); 

    // Sending a GET request to fetch animal data with authorization header
    fetch('http://localhost:5001/animais', {
        headers: {
            'Authorization': `Bearer ${token}` 
        }
    })
    .then(response => response.json())
    .then(data => {
        // Getting elements for displaying animal names, details, and back button
        const namesList = document.getElementById('animal-names-list');
        const detailsContainer = document.getElementById('animal-details');
        const backButton = document.getElementById('back-to-list');
        
        // Iterating through the fetched data
        data.forEach(animal => {
            // Creating list item for each animal name
            const nameItem = document.createElement('li');
            nameItem.textContent = animal.nome;
            namesList.appendChild(nameItem);

            // Adding click event listener to show animal details when clicked
            nameItem.addEventListener('click', () => {
                // Hiding the list and showing details container
                namesList.style.display = 'none';
                detailsContainer.style.display = 'block';
                // Filling details container with animal information
                detailsContainer.innerHTML = `
                    <h2>${animal.nome}</h2>
                    <p>ID: ${animal.id}</p>
                    <p>Idade: ${animal.idade}</p>
                    <p>Raça: ${animal.raca}</p>
                    <p>Tipo: ${animal.tipo}</p>
                    <p>Observações: ${animal.observacoes}</p>
                `;
                // Showing the back button
                backButton.style.display = 'block';
            });
        });

        // Adding click event listener to back button to return to the list
        backButton.addEventListener('click', () => {
            / Showing the list, hiding details container, and hiding back button
            const namesList = document.getElementById('animal-names-list');
            const detailsContainer = document.getElementById('animal-details');
            namesList.style.display = 'block';
            detailsContainer.style.display = 'none';
            backButton.style.display = 'none';
        });
    })
    .catch(error => console.error('Error:', error));
});
