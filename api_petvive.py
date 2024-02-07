# Library import
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flasgger import Swagger
import psycopg2
from abc import ABC, abstractmethod
from flask_cors import CORS
import hashlib

# Defines the Animal class with properties like id, name, age, breed, type, observations, and active status.
class Animal:
    def __init__(self, id, nome, idade, raca, tipo, observacoes, ativo=True):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.tipo = tipo
        self.observacoes = observacoes
        self.ativo = ativo

# Defines the Usuario (User) class with properties like id, username, and password.
class Usuario:
    def __init__(self, id, username, senha):
        self.id = id
        self.username = username
        self.senha = senha

# Defines the abstract base class for Animal Data Access Object with abstract methods for CRUD operations on animals.
class AnimalDAO(ABC):
    @abstractmethod
    def adicionar_animal(self, animal):
        pass

    @abstractmethod
    def retornar_animais(self):
        pass

    @abstractmethod
    def atualizar_animal(self, animal):
        pass

    @abstractmethod
    def deletar_animal(self, id):
        pass

# Defines the abstract base class for User Data Access Object with abstract methods for adding and authenticating users.
class UsuarioDAO(ABC):
    @abstractmethod
    def adicionar_usuario(self, usuario):
        pass

    @abstractmethod
    def autenticar_usuario(self, username, senha):
        pass

# Implements the AnimalDAO interface with PostgreSQL to perform CRUD operations on animals stored in a PostgreSQL database.
class AnimalDAOImplPostgresql(AnimalDAO):
    def __init__(self, dbname, user, password, host='localhost'):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS animais (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(255),
                idade INTEGER,
                raca VARCHAR(255),
                tipo VARCHAR(255),
                observacoes TEXT,
                ativo BOOLEAN DEFAULT TRUE
            )
        ''')
        self.conn.commit()

    def adicionar_animal(self, animal):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO animais (nome, idade, raca, tipo, observacoes, ativo)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (animal.nome, animal.idade, animal.raca, animal.tipo, animal.observacoes, animal.ativo))
        self.conn.commit()

    def retornar_animais(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM animais')
        rows = cursor.fetchall()

        animals = []
        for row in rows:
            animals.append(Animal(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        return animals

    def atualizar_animal(self, animal):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE animais
            SET nome=%s, idade=%s, raca=%s, tipo=%s, observacoes=%s, ativo=%s
            WHERE id=%s
        ''', (animal.nome, animal.idade, animal.raca, animal.tipo, animal.observacoes, animal.ativo, animal.id))
        self.conn.commit()

    def deletar_animal(self, id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM animais WHERE id=%s', (id,))
        self.conn.commit()


# Implements the UsuarioDAO interface with PostgreSQL to add and authenticate users in a PostgreSQL database.
class UsuarioDAOImplPostgresql(UsuarioDAO):
    def __init__(self, dbname, user, password, host='localhost'):
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255),
                senha VARCHAR(255)
            )
        ''')
        self.conn.commit()

    def buscar_usuario_por_nome_de_usuario(self, username):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE username = %s', (username,))
        user = cursor.fetchone()

        if user:
            return Usuario(user[0], user[1], user[2])
        else:
            return None

    def adicionar_usuario(self, usuario):
        cursor = self.conn.cursor()

        hashed_password = hashlib.sha256(usuario.senha.encode()).hexdigest()

        cursor.execute('INSERT INTO usuarios (username, senha) VALUES (%s, %s)', (usuario.username, hashed_password))
        self.conn.commit()

    def autenticar_usuario(self, username, senha):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE username = %s', (username,))
        user = cursor.fetchone()

        if user:
            hashed_password = hashlib.sha256(senha.encode()).hexdigest()

            if user[2] == hashed_password:
                return Usuario(user[0], user[1], user[2])

        return None

app = Flask(__name__) # Creates a Flask application instance.
app.config['CORS+HEADERS'] = 'Content-Type' # Sets up CORS headers to 'Content-Type'.
app.config['JWT_SECRET_KEY'] = 'ChAvEpEtVivE' # Sets the secret key for JWT encoding and decoding.
CORS(app) # Initializes CORS for the Flask app to allow cross-origin requests.
swagger = Swagger(app) #  Initializes Swagger for the Flask app to document the API.
dao = AnimalDAOImplPostgresql('APIPETVIVE', 'postgres', '1234', 'localhost') #  Initializes the AnimalDAO implementation with connection details to the PostgreSQL database.
usuario_dao = UsuarioDAOImplPostgresql('APIPETVIVE', 'postgres', '1234', 'localhost') #  Initializes the UserDAO implementation with connection details to the PostgreSQL database.

jwt = JWTManager(app) # Initializes the JWTManager with the Flask app to handle JWT operations.

@app.route('/registro', methods=['POST']) # Endpoint for user registration.
def registro():
    """
    Registra um novo usuário.
    ---
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: Nome de usuário.
      - name: senha
        in: formData
        type: string
        required: true
        description: Senha do usuário.
    responses:
      200:
        description: Usuário registrado com sucesso.
    """
    username = request.form['username']
    senha = request.form['senha']

    usuario = Usuario(None, username, senha)
    usuario_dao.adicionar_usuario(usuario)

    return 'Usuário registrado com sucesso.', 200

@app.route('/login', methods=['POST']) # Endpoint for user authentication and JWT token generation.
def login():
    """
    Autentica um usuário e retorna um token JWT válido.
    ---
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: Nome de usuário.
      - name: senha
        in: formData
        type: string
        required: true
        description: Senha do usuário.
    responses:
      200:
        description: Autenticado com sucesso. Retorna um token JWT.
      401:
        description: Credenciais inválidas.
    """
    username = request.form['username']
    senha = request.form['senha']

    usuario = usuario_dao.buscar_usuario_por_nome_de_usuario(username)

    if usuario:
        hashed_password = hashlib.sha256(senha.encode()).hexdigest()

        if usuario.senha == hashed_password:
            access_token = create_access_token(identity=usuario.username)
            return jsonify(access_token=access_token), 200

    return 'Credenciais inválidas', 401


@app.route('/animal', methods=['POST']) # Endpoint for adding an animal, protected by JWT authentication.
@jwt_required()
def adicionar_animal():
    """
    Adiciona um animal à lista (requer autenticação).
    ---
    parameters:
      - name: nome
        in: formData
        type: string
        required: true
        description: Nome do animal.
      - name: idade
        in: formData
        type: integer
        required: true
        description: Idade do animal.
      - name: raca
        in: formData
        type: string
        required: true
        description: Raça do animal.
      - name: tipo
        in: formData
        type: string
        required: true
        description: Tipo do animal.
      - name: observacoes
        in: formData
        type: string
        required: true
        description: Observações sobre o animal.
    responses:
      200:
        description: Animal adicionado com sucesso.
      401:
        description: Não autorizado (token inválido ou ausente).
    """
    current_user = get_jwt_identity()

    nome = request.form['nome']
    idade = int(request.form['idade'])
    raca = request.form['raca']
    tipo = request.form['tipo']
    observacoes = request.form['observacoes']

    animal = Animal(None, nome, idade, raca, tipo, observacoes)
    dao.adicionar_animal(animal)

    return 'Animal adicionado com sucesso.', 200

@app.route('/animais', methods=['GET']) # Endpoint for retrieving all animals, protected by JWT authentication.
@jwt_required()
def retornar_animais():
    """
    Retorna a lista de animais.
    ---
    responses:
      200:
        description: Lista de animais.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: ID do animal.
              nome:
                type: string
                description: Nome do animal.
              idade:
                type: integer
                description: Idade do animal.
              raca:
                type: string
                description: Raça do animal.
              tipo:
                type: string
                description: Tipo do animal.
              observacoes:
                type: string
                description: Observações sobre o animal.
    """

    animais = dao.retornar_animais()
    animais_dict = [{'id': animal.id, 'nome': animal.nome, 'idade': animal.idade, 'raca': animal.raca, 'tipo': animal.tipo, 'observacoes': animal.observacoes} for animal in animais]

    return jsonify(animais_dict), 200

@app.route('/animal/<int:id>', methods=['PUT']) # Endpoint for updating an animal's information, protected by JWT authentication.
@jwt_required()
def atualizar_animal(id):
    """
    Atualiza os dados de um animal existente.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do animal a ser atualizado.
      - name: nome
        in: formData
        type: string
        required: false
        description: Novo nome do animal.
      - name: idade
        in: formData
        type: integer
        required: false
        description: Nova idade do animal.
      - name: raca
        in: formData
        type: string
        required: false
        description: Nova raça do animal.
      - name: tipo
        in: formData
        type: string
        required: false
        description: Novo tipo do animal.
      - name: observacoes
        in: formData
        type: string
        required: false
        description: Novas observações sobre o animal.
    responses:
      200:
        description: Animal atualizado com sucesso.
      404:
        description: Animal não encontrado.
    """
    animal = dao.retornar_animais()
    if not animal:
        return 'Animal não encontrado', 404

    nome = request.form.get('nome', animal[0].nome) if 'nome' in request.form else animal[0].nome
    idade = int(request.form.get('idade', animal[0].idade)) if 'idade' in request.form else animal[0].idade
    raca = request.form.get('raca', animal[0].raca) if 'raca' in request.form else animal[0].raca
    tipo = request.form.get('tipo', animal[0].tipo) if 'tipo' in request.form else animal[0].tipo
    observacoes = request.form.get('observacoes', animal[0].observacoes) if 'observacoes' in request.form else animal[0].observacoes

    animal_atualizado = Animal(id, nome, idade, raca, tipo, observacoes)
    dao.atualizar_animal(animal_atualizado)

    return 'Animal atualizado com sucesso.', 200


@app.route('/deletar_animal/<int:id>', methods=['DELETE']) # Endpoint for deleting an animal, protected by JWT authentication.
@jwt_required()
def deletar_animal(id):
    """
    Deleta um animal existente.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do animal a ser deletado.
    responses:
      200:
        description: Animal deletado com sucesso.
      404:
        description: Animal não encontrado.
    """

    animal = dao.retornar_animais()
    if not animal:
        return 'Animal não encontrado', 404

    dao.deletar_animal(id)

    return 'Animal deletado com sucesso.', 200

# Checks if the script is the main program and not being imported into another module.
if __name__ == '__main__':
    app.run(debug=True, port=5001) # Runs the Flask application with debugging enabled on port 5001.