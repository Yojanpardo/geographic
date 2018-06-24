# Geographic
Este repositorio es especial para un repaso breve del curso de Django de platzi.
## Creando un nuevo proyecto en Django
1. Debemos crear un entorno virtual para mantener nuestos proyectos aislados entre si y vamos a trabajar siempre dentro de nuestro entorno virtual.
2. una vez dentro de nuestro entorno virtual debemos instalar django con el gestor de paquetes pip.
3. creamos un proyecto nuevo con django-admin.
4. podemos crear 'mini-aplicaciones' dentro de django para mantener el proyecto organizado y entendible. Para ello utilizamos el manage.py.
5. configuramos nuestra nueva aplicación dentro de los settings de django en el cual configuramos las aplicaciones, bases de datos, middleware, hosts, etc.
  * Configuramos los local settings para que solo actuen en nuestro entorno de desarrollo y de esta manera, por ejemplo, tener activo el debug en local pero no en producción.

## MVC y MVT
Django utiliza el modelo vista controlador pero no de la manera mas 'fiel' ya que django funciona diferentes archivos que son: models.py, views.py, urls.py y los templates .html que son renderizados a partir de las vistas, en este caso models seria nuestro modelo, views y urls serian el controlador y los templates son las vistas.

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
Es una clase que hereda de View, nos permite usar dispatch, get y post. nos permite manejar herencia, mixings, tener el codigo mas organizado y tener comportamiento por defecto.
