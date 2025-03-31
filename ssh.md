# Generar clave SSH para autenticar con GIT en local

1. En el directorio del usuario, crear una carpeta oculta llamada ".ssh"
*** Nos movemos al directorio del usuario por consola ***
cd ~
*** Creamos en este directorio el directorio .ssh con el siguiente comando ***
mkdir .ssh

2. Crear par de llaves publica/privada
*** Primero nos movemos al directorio .ssh ***
cd ~/.ssh
*** En el directorio creado ".ssh", ejecutar el siguiente comando ***
ssh-keygen -t ed25519 -C "your_email@example.com"
*** Nota primero pide el nombre del archivo, se le puede poner "uader" ***
*** Cuando pida contraseña dejarlo vacio y solamente apretar enter ***
*** Para corroborar que se crearon las pares de llaves, ejecutar el comando siguiente ***
ls -la ~/.ssh

3. Crear archivo config en el directorio .ssh, para agregar hosts conocidos, ejecutando el siguiente comando
nano ~/.ssh/config

4. Pegar dentro del archivo el siguiente codigo

Host github.com
    Hostname ssh.github.com
    Port 443
    User git


# Agregar clave publica SSH en cuenta de github (remoto)
1. Iniciar sesion en git
2. Apretar en la fotito de usuario
3. Ir a ajustes
4. ir a Claves SSH y GPG
5. Apretar en Nueva clave SSH
6. Ponerle un nombre donde dice titulo, puede ser "uader" o lo que sea
7. Donde dice llave, pegar la clave publica (contenido del archivo) ~/.ssh/uader.pub
8. Si no sabes como leerlo, pega en consola el siguiente comando y copia lo que aparece en consola, posteriormente haces lo del  paso 7*

cat ~/.ssh/uader.pub

9. Iniciar ssh ejecutando el siguiente comando en consola
eval "$(ssh-agent -s)"

10. Agregar llave privada al ssh ejecutando los siguientes comandos
ssh-add ~/.ssh/uader

10. Ya esta todo listo para clonar el repositorio
git clone "url-que-copiaste-del-boton-clone-de-git"