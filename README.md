<h1>Github-Profile-Cloner</h1>

<h3>Descripcion</h3>
<p><b>Github-Profile-Cloner</b> es una herramienta de consola para clonar completamente un perfil de <b>Github</b> a otro en segundos. Repos completos, Commits, Readme del perfil etc..., clona cualquier perfil de <b>Github</b> a uno tuyo propio</p>

<hr>

<h3>Funciones actuales/futuras y Version del script</h3>

<b>Version actual: 0.2</b>

<br>

<b>Funciones Actuales</b>
<p>El script es una base minima, hasta ahora solo automatiza el clonamiento de <b>repositorios</b> y <b>commits</b> de un perfil a una carpeta local y atravez de un token de github (PAT) sube los repositorios y commits a el usuario deseado, tambien extrae y clona Nombre Completo, Bio, Blog, X-Account(Twitter), company, ubicacion y email.</p>

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
chmod +x src/main.py
./src/main.py -v
```

<p>Si muestra la version del script (0.2) significa que se instalo correctamente.</p>

<b>Uso</b>

<p>Para usarlo es necesario una <b>cuenta de github</b> unicamente</p>
<br>
<p>En tu cuenta presiona la foto de perfil (arriba a la derecha) y cuando se abra el menu presione la opcion de Settings (o tambien llamada configuracion), en el menu lateral derecho vaya a lo ultimo y presione el apartado de de Developer Settings, una vez alli presione en el menu lateral la opcion "Personal Access Token" y dentro la opcion "Tokens(Classic)" una vez ahi presione "Generate new token" y ahi elija la opcion "Generate new token (Classic)" los permisos necesarios son "repo", "user" y "delete_repo", en caso de no estar seguro o recibir errores es recomendable seleccionar todos los permisos, despues precione en el boton verde llamado "Generate Token", una vez generado copielo y guardelo en un lugar seguro.</p>

```bash
./src/main.py -o owner -t token -u user
```

<p>Para ejecutarlo correctamente ejecute ese codigo cambiando "owner" por el usuario que se va a clonar, "token" por el token ya copiado y "user" por el usuario al que se le va a enviar todo lo clonado. Importante el "user" tiene que ser el mismo al que pertenece el "token" y "owner" puede ser cualquier usuario deseado</p>

Ejemplo falso:
```bash
./src/main.py -o mouredev -t a1b2c3d4e5f6g7h8i9j0 -u octocat
```

<hr>

<div align="center">
    <h1><code>Built with Love</code></h1>
</div>
