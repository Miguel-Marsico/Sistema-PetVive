<h1>
    PetVive System 🐾
</h1>

https://github.com/Miguel-Marsico/SistemaPetVive/assets/158609724/cff43244-9fa9-445c-b671-1cb2bc768cb2

 ## 📋 Topics
<div>
 • <a href="#-about">About</a> </br>
 • <a href="#-tools">Tools</a> </br>
 • <a href="#-database-structure">Database structure</a> </br>
 • <a href="#-how-to-execute-the-project">How to execute the project</a> </br>
 • <a href="#-license">License</a></br>
</div>

## 📗 About

**PetVive** is a system designed with the purpose of improving Full Stack development skills in a web application. This platform was developed with the aim of providing veterinarians with a powerful tool for managing their patients' information efficiently and effectively.

## 🔧 Tools

### 💻 **Website** ( HTML + CSS + JavaScript )

- [Google Fonts](https://fonts.googleapis.com/css2?family=Gabarito:wght@400;500;600;700;800;900&display=swap)
- [Font Awesome](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.cs)

### 🔄 **API** ([Pyhton](https://www.python.org))

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Psycopg2](https://www.psycopg.org/docs/)
- [HashLib](https://docs.python.org/3/library/hashlib.html)

### 🛠️ **Utilities** ([PostgreSQL](https://www.postgresql.org/docs/))

- Database: **[PostgreSQL](https://www.postgresql.org/docs/)**
- Compilers: **[Pycharm Community](https://www.jetbrains.com/pt-br/pycharm/)** +**[Visual Studio Code](https://code.visualstudio.com/)** → Extensions: **[Live server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)** 

## 📂 Database structure

### Functionality of DAO (Data Access Object) in the Project:

The **DAO** is a crucial component of this project that manages interaction with the **PostgreSQL** database. It separates the database logic from the rest of the application, enabling database operations to be performed **independently**.

In this project, we have two main DAOs:

**AnimalDAO**: Manages operations related to animals, such as adding, retrieving, updating, and deleting records from the "animals" table in the database.

**UsuarioDAO**: Manages operations related to users, such as adding and authenticating users, using the "usuarios" table in the database.

### The project utilizes a PostgreSQL database with the following structure:

**1** - 🐾 Table "**animais**":

#### Fields: id, nome, idade, raca, tipo, observacoes, ativo.
```bash
Stores information about animals, including name, age, breed, type, observations, and active status.
```

**2** - 👤 Table "**usuarios**":

#### Fields: id, username, senha.

```bash
Stores information about users, including username and password (stored as a password hash).
```

## ▶ How to execute the project

### The project is divided into **2** parts:

 - 🌐 **Frontend** (WebSite HTML, CSS, JavaScript)
 - ⚙️ **Backend** (Python API, PostgreSQL DataBase)
 
 💡 The backend must be running for the frontend to work.

### ⚙️ Backend:

#### Installing libraries:

```bash
 $ pip install Flask
 $ pip install flask_jwt_extended
 $ pip install flasgger
 $ pip install flask_cors
```
```bash
 $ pip install psycopg2
``` 
```bash
 $ pip install hashlib
```

#### Library import:

```bash
 from flask import Flask, request, jsonify

 from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

 from flasgger import Swagger

 import psycopg2

 from abc import ABC, abstractmethod

 from flask_cors import CORS

 import hashlib
```

#### DataBase:

#### The database will be **automatically** configured by **Psycopg2**, just create it and add the necessary informations in the code:

```bash
 183: dao = AnimalDAOImplPostgresql('database-name', 'user', 'password', 'host')
 184: usuario_dao = UsuarioDAOImplPostgresql('database-name', 'user', 'password', 'host')
```

#### After that, just run the **API** and the **backend** should be working

### 🌐 Frontend:

#### With the **Backend running**, just open "**home-page.html**" on a **local server** and everything should work perfectly.

## 📜 License

### This project is under the MIT license. 
<br>
Developed by Miguel Marsico 👋🏻
