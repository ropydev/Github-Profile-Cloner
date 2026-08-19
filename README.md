<h1>Github-Profile-Cloner</h1>

<div align="center">
    <img src="img/logo.png" width="200">
</div>

<div>
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green.svg">
    <img alt="Python" src="https://img.shields.io/badge/Python-3.9%2B-blue.svg">
    <img alt="Version" src="https://img.shields.io/badge/Version-v1.1-orange.svg">
    <img alt="Status" src="https://img.shields.io/badge/Status-Active-success.svg">
    <img alt="Contributions" src="https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg">
    <img alt="Stars" src="https://img.shields.io/github/stars/ropydev/Github-Profile-Cloner?style=social">
    <img alt="Forks" src="https://img.shields.io/github/forks/ropydev/Github-Profile-Cloner?style=social">
</div>

<p><b>Github-Profile-Cloner</b> es una herramienta creada en <b>Python</b> para clonar completamente un perfil de <b>Github</b> a otro en cuestion de segundos.</p>

<!-- TOC -->
- [Instalacion](#instalacion)
  - [Explicacion](#explicacion)
- [Uso](#uso)
  - [Requisitos](#requisitos)
    - [Crear cuenta](#crear-cuenta)
    - [Generar Token PAT (Classic)](#generar-token-pat-classic)
  - [Uso en Terminal](#uso-en-terminal)
    - [Explicacion](#explicacion-1)
  - [Uso en Navegador](#uso-en-navegador)
    - [Explicacion](#explicacion-2)
- [Funcionamiento](#funcionamiento)
  - [Tree (Arbol del proyecto)](#tree-arbol-del-proyecto)
  - [Explicacion del funcionamiento](#explicacion-del-funcionamiento)
- [Utilidad](#utilidad)
<!-- /TOC -->

<hr>

## Instalacion

Para instalar simplemente se necesia conexion a internet y ejecutar en la terminal los siguientes comandos

```bash
git clone https://github.com/ropydev/Github-Profile-Cloner
cd Github-Profile-Cloner
pip install -r requirements.txt
```

### Explicacion
```bash
git clone https://github.com/ropydev/Github-Profile-Cloner
```
Clona el repositorio en ./Github-Profile-Cloner/

```bash
cd Github-Profile-Cloner
```
Entra en la carpeta donde esta el codigo

```bash
pip install -r requirements.txt
```
Instala las dependencias (solo necesita requests que ya viene por defecto en algunas versiones de Python)

## Uso

### Requisitos
Se necesita:
- Cuenta de github
- Token PAT (classic)

#### Crear cuenta
Entra a github y en el boton arriba a la derecha que dice SignUp presionelo e introdusca sus datos, recuerde el usuario y el email

#### Generar Token PAT (Classic)
Estando dentro de tu cuenta:
- Ve a la esquina superior derecha y haz clic en tu avatar, selecciona **Settings**
- En el menu lateral izquierdo baja hasta el final y entra en **Developer settings**
- Selecciona **Personal access tokens** >> **Token (classic)**
- Haz clic en **Generate new token (classic)**, confirma el acceso con tu password de github
- Define nota (Github-Profile-Cloner), fecha de expiracion y marca los permisos necesarios (repo, user, delete_repo)
- Genere token y guardelo en un lugar seguro

### Uso en Terminal
Dentro de la carpeta Github-Profile-Cloner ejecute:
```bash
python -m src.console.main -o Usuario_Original -u Cuenta_Nueva -t Token -e email@cuenta.nueva
```
cambiando **Usuario_Original** por la cuenta que perdiste o cuenta que quieres clonar, **Cuenta_Nueva** por la cuenta que creaste, **Token** por el token copiado recientemente, **email@cuenta.nueva** por el email con el que registraste la cuenta nueva

#### Explicacion
El comando clona el perfil completo y cambia el autor de los commits por tu usuario, en caso de que quieras que eso no suceda para matener el usuario original, use --no-rewrite al final

### Uso en Navegador
Dentro de la carpeta Github-Profile-Cloner ejecute:
```bash
python -m src.web.app
```
Entre en el navegador a la url *http://localhost:8000/* y rellene los campos con los datos necesarios
- owner, el usuario original
- user, la cuenta nueva
- token, el token recientemente copiado
- email, el email con el que se registro la cuenta nueva

#### Explicacion
Ese procedimiento clona el perfil completo y cambia el autor de los commits por tu usuario, en caso de que quieras que eso no suceda seleccione el checkbox que aparece en la pagina

<hr>

## Funcionamiento

### Tree (Arbol del proyecto)

```text
.
├── examples
│   └── web.png
├── LICENSE
├── README.md
├── requirements.txt
└── src
    ├── console
    │   └── main.py
    ├── lib
    │   ├── GithubProfileCloner.py
    │   └── __init__.py
    └── web
        ├── app.py
        ├── img
        │   └── github-logo-G.png
        └── static
            └── index.html
```

<p>El "proyecto" esta ordenado originalmente en 8 directorios y 10 archivos, en la raiz, LICENSE (la Licencia MIT), README.md (la documentacion, este archivo), requirements.txt (Las dependencias), example (Donde se encuentran imagenes png de como se ve cada version), src (Donde esta todo el codigo), src/console/main.py (el archivo que ejecuta la herramienta en consola), src/lib/GithubProfileCloner.py (La base de todo, la libreria donde funciona todas las peticiones, funciones y basicamente todo), src/lib/__init__.py (archivo que hace que la libreria sea interpretada como tal), src/web/app.py (La version web de la herramienta), src/web/img/github-logo-G.png (Logo de github en un tono verde para decoracion de la web), src/web/static/index.html (HTML5 de la web)</p>

### Explicacion del funcionamiento
La herramienta, tanto la version de consola como la version web, dependen de la libreria local src/lib/GithubProfileCloner.py la cual hace todo el funcionamiento, esta libreria local creada desde cero por mi esta dividida en diferentes funciones, y la funcion cloneProfile(), la funcion principal que reune todas las demas y hace que se borren stars, followings y repos, agrega las stars, los followings y la info del otro usuario, descarga la imagen del perfil en una carpeta local, recorre todos los repositorios clonandolos, cambiando la historia y subiendo los repos

## Utilidad

El programa permite que una persona al perder acceso a su cuenta de github pueda clonarla automaticamente sin perder nada o sin estar horas y horas creando una nueva</p>

<div align="center">
    <h1><code>Built with Love (and Python)</code></h1>
</div>
