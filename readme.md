# Geographic
Este repositorio es especial para un repaso breve del curso de Django de platzi.
## Creando un nuevo proyecto en Django
1. Debemos crear un entorno virtual para mantener nuestos proyectos aislados entre si y vamos a trabajar siempre dentro de nuestro entorno virtual.
2. una vez dentro de nuestro entorno virtual debemos instalar django con el gestor de paquetes pip.
3. creamos un proyecto nuevo con django-admin.
4. podemos crear 'mini-aplicaciones' dentro de django para mantener el proyecto organizado y entendible. Para ello utilizamos el manage.py.
5. configuramos nuestra nueva aplicación dentro de los settings de django.
## Function based view
Se crea una funcion que recibe un request, es procesado y se da como respuesta un http response, es una forma de arrojar vistas pero es algo limitado.
### Diferentes tipos de response
Dependiendo de lo que necesitemos que haga nuestra vista podemos darle diferentes ordenes para que las ejecute con algunos de las siguientes respuestas.
* HttpResponse
* JsonResponse
* HttpResponseRedirect
* HttpResponseBadRequest
* ...
## Class based view
