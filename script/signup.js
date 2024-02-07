var menu = document.querySelector('nav ul');
var menuBar = document.querySelector('nav .menu-icon')
var iconmenu = document.querySelector('nav .menu-icon img')

menuBar.addEventListener('click',function(){
    menu.classList.toggle('active')
});

document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(this);

    fetch('http://localhost:5001/registro', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            document.getElementById('registroMensagem').innerText = "Seja bem-vindo!";
            document.getElementById('registroMensagem').style.color = "green";
            document.getElementById('registroMensagem').style.display = "block";
        } else {
            document.getElementById('registroMensagem').innerText = "Erro ao registrar.";
            document.getElementById('registroMensagem').style.color = "red";
            document.getElementById('registroMensagem').style.display = "block";
            throw new Error('Erro ao registrar');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});
