<h1>Github-Profile-Cloner</h1>

<h3>Descripcion</h3>
<p><b>Github-Profile-Cloner</b> es una herramienta para clonar completamente un perfil de <b>Github</b> a otro en segundos. Repos completos, Commits, Readme del perfil etc..., clona cualquier perfil de <b>Github</b> a uno tuyo propio</p>

<hr>

<h3>Funciones actuales/futuras y Version del script</h3>

<b>Version actual: 0.5</b>

<br>

<b>Funciones Actuales</b>
<p>La herramienta, hasta ahora solo automatiza el clonamiento de <b>repositorios</b> y <b>commits</b> de un perfil a una carpeta local y atravez de un token de github (PAT) sube los repositorios y commits a el usuario deseado, tambien extrae y clona Nombre Completo, Bio, Blog, X-Account(Twitter), company, ubicacion y email.</p>

<br>

<b>Funciones Futuras</b>
<p>.</p>

<hr>

<h3>Instalacion y uso</h3>

<p>La instalacion es muy basica, vendria siendo la misma de la mayoria de scripts de python que seria bajarse el repo, instalar las dependencias y a usarlo</p>

```bash
git clone https://github.com/ropydev/Github-Profile-Cloner
cd Github-Profile-Cloner
pip install -r requirements.txt
```

<b>Uso</b>

<p>Para usarlo es necesario una <b>cuenta de github</b> unicamente</p>
<br>
<p>En tu cuenta presiona la foto de perfil (arriba a la derecha) y cuando se abra el menu presione la opcion de Settings (o tambien llamada configuracion), en el menu lateral izquierdo vaya a lo ultimo y presione el apartado de de Developer Settings, una vez alli presione en el menu lateral la opcion "Personal Access Token" y dentro la opcion "Tokens(Classic)" una vez ahi presione "Generate new token" y ahi elija la opcion "Generate new token (Classic)" los permisos necesarios son "repo", "user", "admin" y "delete_repo", en caso de no estar seguro o recibir errores es recomendable seleccionar todos los permisos, despues presione en el boton verde llamado "Generate Token", una vez generado copielo y guardelo en un lugar seguro.</p>

<br>
<p>La herramienta cuenta con una version tanto como de terminal como web (personalmente me gusta mas la de consola, mas estable, funcional y sencilla de usar.</p>
<br>
<b>Uso en consola (ubicado en Github-Profile-Cloner/)</b>

```bash
python -m src.console.main -o owner -t token -u user
```

<p>Para ejecutarlo correctamente ejecute ese codigo cambiando "owner" por el usuario que se va a clonar, "token" por el token ya copiado y "user" por el usuario al que se le va a enviar todo lo clonado. Importante el "user" tiene que ser el mismo al que pertenece el "token" y "owner" puede ser cualquier usuario deseado</p>

Ejemplo falso:

```bash
./src/main.py -o mouredev -t ghp_abcdefghijklmn1bcdefghi2c3d4e5f6g7h8i9j0 -u octocat
```

<b>Uso en web (ubicado en Github-Profile-Cloner/)</b>

```bash
python -m src.web.app
```

<p>Se necesita ejecutar exactamente ese codigo, se levantara un servidor web en el puerto 8000 (http://localhost:8000/), debe entrar en esa url local y en los campos owner, user y token introducir:
En el primero, el usuario original
En el segundo, el usuario a donde se va a clonar
En el tercero, el token previamente copiado
<br>
Recalco que la version web es menos precisa y menos estable</p>
<br>

<p>Importante ejecutarlo con el "python -m src." para su correcto funcionamiento</p>

<hr>

<h3>Funcionamiento</h3>

<b>Tree (Arbol del proyecto)</b>

```text
.
├── LICENSE
├── README.md
├── requirements.txt
└── src
    ├── console
    │   └── main.py
    ├── lib
    │   ├── GithubProfileCloner.py
    │   └── __init__.py
    └── web
        └── app.py

5 directories, 7 files
```

<p>El "proyecto" esta ordenado originalmente en 5 directorios y 7 archivos, en la raiz, LICENSE (la Licencia MIT), README.md (la documentacion, este archivo), requirements.txt (Las dependencias), src (Donde esta todo el codigo), src/console/main.py (el archivo que ejecuta la herramienta en consola), src/lib/GithubProfileCloner.py (La base de todo, la libreria donde funciona todas las peticiones, funciones y basicamente todo), src/lib/__init__.py (archivo que hace que la libreria sea interpretada como tal), src/web/app.py (La version web de la herramienta, poco estable)</p>

<br>

<h3>Que problema soluciona?</h3>
<p>El programa permite que una persona al perder acceso a su cuenta de github pueda clonarla automaticamente, la herramienta tambien puede clonar cualquier perfil asi que tambien funciona para "suplantar" una cuenta, no me hago cargo del uso indebido de esta herramienta.</p>

<hr>

<h3>Importante: La herramienta deja una marca de agua en la descripcion del perfil (marca de agua muy facil de eliminar  ;)</h3>

<hr>
<div align="center">
    <h1><code>Built with Love</code></h1>
</div>
