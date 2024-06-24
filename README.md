<h1>
    Sistema PetVive 🐾
</h1>

https://github.com/Miguel-Marsico/SistemaPetVive/assets/158609724/cff43244-9fa9-445c-b671-1cb2bc768cb2

 ## 📋 Tópicos
<div>
 • <a href="#-sobre">Sobre</a> </br>
 • <a href="#-ferramentas">Ferramentas</a> </br>
 • <a href="#-como-executar-esse-projeto">Como Executar esse projeto</a> </br>    
 • <a href="#-licença">Licença</a></br>
</div>

## 📗 Sobre

**PetVive** é um sistema desenvolvido com o objetivo de aprimorar as habilidades de desenvolvimento Full Stack em uma aplicação web. Esta plataforma foi desenvolvida com o objetivo de fornecer aos veterinários uma poderosa ferramenta para gerir a informação dos seus pacientes de forma eficiente e eficaz.

## 🔧 Ferramentas

### 💻 **Website** ( HTML + CSS + JavaScript )

- [Google Fonts](https://fonts.googleapis.com/css2?family=Gabarito:wght@400;500;600;700;800;900&display=swap)
- [Font Awesome](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.cs)

### 🔄 **API** ([Pyhton](https://www.python.org))

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Psycopg2](https://www.psycopg.org/docs/)
- [HashLib](https://docs.python.org/3/library/hashlib.html)

### 🛠️ **Utilitários** 

- Base de dados: **[PostgreSQL](https://www.postgresql.org/docs/)**
- Compiladores: **[Pycharm Community](https://www.jetbrains.com/pt-br/pycharm/)** +**[Visual Studio Code](https://code.visualstudio.com/)** → Extensions: **[Live server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)** 

## 📂 Estrutura do banco de dados

### Funcionalidade do DAO (Data Access Object) no Projeto:

O **DAO** é um componente crucial deste projeto que gerencia a interação com o banco de dados **PostgreSQL**. Ele separa a lógica do banco de dados do restante do aplicativo, permitindo que as operações do banco de dados sejam executadas **de forma independente**.

Neste projeto, temos dois DAOs principais:

**AnimalDAO**: Gerencia operações relacionadas a animais, como adição, recuperação, atualização e exclusão de registros da tabela “animais” do banco de dados.

**UsuarioDAO**: Gerencia operações relacionadas a usuários, como adição e autenticação de usuários, utilizando a tabela "usuários" do banco de dados.

### O projeto utiliza um banco de dados PostgreSQL com a seguinte estrutura:

**1** - 🐾 Tabela "**animais**":

#### Colunas: id, nome, idade, raça, tipo, observações, ativo.
```bash
Armazena informações sobre animais, incluindo nome, idade, raça, tipo, observações e status ativo.
```

**2** - 👤 Tabela "**usuarios**":

#### Colunas: id, nome de usuário, senha.

```bash
Armazena informações sobre usuários, incluindo nome de usuário e senha (armazenados como um hash de senha).
```

## ▶ Como executar o projeto

### O projeto está dividido em **2** partes:

 - 🌐 **Frontend** (WebSite HTML, CSS, JavaScript)
 - ⚙️ **Backend** (Python API, PostgreSQL DataBase)
 
 💡 O back-end deve estar em execução para que o front-end funcione.
 
 💡 Usar um ambiente virtual Python (venv) é essencial para isolar e gerenciar dependências do projeto de maneira segura e reproduzível.

### ⚙️ Backend:

#### Crie um ambiente virtual:

1 - Navegue até o diretório onde deseja criar o ambiente virtual:
```bash
 cd /path/to/your/project
```
2 - Crie um ambiente virtual:
```bash
 python3 -m venv name
```
3 - Ative o ambiente virtual:
```bash
 name\Scripts\activate
```

#### Instalações de bibliotecas:

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

#### Importação de bibliotecas:

```bash
 from flask import Flask, request, jsonify

 from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

 from flasgger import Swagger

 import psycopg2

 from abc import ABC, abstractmethod

 from flask_cors import CORS

 import hashlib
```

#### Banco de Dados:

#### O banco de dados será configurado **automaticamente** pelo **Psycopg2**, basta criá-lo e adicionar as informações necessárias no código:

```bash
 183: dao = AnimalDAOImplPostgresql('database-name', 'user', 'password', 'host')
 184: usuario_dao = UsuarioDAOImplPostgresql('database-name', 'user', 'password', 'host')
```

#### Depois disso, basta executar a **API** e o **backend** deverá estar funcionando

### 🌐 Frontend:

#### Com o **Backend em execução**, basta abrir "**home-page.html**" em um **servidor local** e tudo deverá funcionar perfeitamente.

## 📜 Licença

Com o **Backend em execução**, basta abrir "**home-page.html**" em um **servidor local** e tudo deverá funcionar perfeitamente.
<br>
Desenvolvido por Miguel Marsico 👋🏻
