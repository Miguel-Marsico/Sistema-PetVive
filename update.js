// Adding a submit event listener to the update form
document.getElementById('updateForm').addEventListener('submit', function(event) {
    // Preventing the default form submission behavior
    event.preventDefault();

    // Creating a new FormData object
    var formData = new FormData();

    // Retrieving values from input fields and appending to formData if not empty
    var id = document.getElementById('id').value;
    formData.append('id', id);

    var nome = document.getElementById('nome').value;
    if (nome !== "") formData.append('nome', nome);

    var idade = document.getElementById('idade').value;
    if (idade !== "") formData.append('idade', idade);

    var raca = document.getElementById('raca').value;
    if (raca !== "") formData.append('raca', raca);

    var tipo = document.getElementById('tipo').value;
    if (tipo !== "") formData.append('tipo', tipo);

    var observacoes = document.getElementById('observacoes').value;
    if (observacoes !== "") formData.append('observacoes', observacoes);

    // Retrieving the token from localStorage
    const token = localStorage.getItem('token'); // Recupera o token JWT do armazenamento local

    // Sending a PUT request to update the animal with authorization header
    fetch('http://localhost:5001/animal/' + id, {
        method: 'PUT',
        body: formData,
        headers: {
            'Authorization': `Bearer ${token}` // Inclui o token nos cabeçalhos
        }
    })
    // Checking if the response is OK
    .then(response => {
        if (response.ok) {
            // Displaying a message for successfully updating the animal and resetting the form
            document.getElementById('animalAtualizado').style.display = 'block';
            this.reset();
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});

// Adding a submit event listener to the delete form
document.getElementById('deleteForm').addEventListener('submit', function(event) {
    // Preventing the default form submission behavior
    event.preventDefault();

    // Retrieving the id of the animal to delete
    var id = document.getElementById('idDeletar').value;

    // Retrieving the token from localStorage
    const token = localStorage.getItem('token'); // Recupera o token JWT do armazenamento local

    // Sending a DELETE request to delete the animal with authorization header
    fetch('http://localhost:5001/deletar_animal/' + id, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${token}` // Inclui o token nos cabeçalhos
        }
    })
    .then(response => {
        // Checking if the response is OK
        if (response.ok) {
            // Displaying a message for successfully deleting the animal and resetting the form
            document.getElementById('animalDeletado').style.display = 'block';
            this.reset();
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});