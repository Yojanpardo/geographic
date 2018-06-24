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
Con las class based view podemos utilizar un crud que nos permite crear, actualizar, listar y eliminar modelos por medio de un formulario utilizando las siguientes CBV por defecto:
  * Createview
  * updateview
  * Listview
  * Deleteview

 Más adelante veremos como funcionan ya que necesitamos tener nuestros modelos creados.

## Templates o plantillas
utiliza una sintaxis que nos permite convertir nuestros archivos estaticos de html en algo más dinámico. Maneja una sintaxis especial que nos permite hacer ciclos y condiciones, tambien nos permite reutilizar templates para no tener que escribir bloques de cógigo que se repiten, como por ejemplo los fotters.
### Template tags y template filters
nos permiten interactuar en nuestros templates. existen muchos tags que nos sirven para hacer diferentes cosas en nuestras plantillas, puedes encontrar mas información en la [documentación](https://docs.djangoproject.com/es/2.0/topics/templates/) de Django.
Es recomendable que toda la información sea procesada en el controlador y solo se muestre en la vista, no es recomendable que se procese informacion en las vistas.
### Context procesors
nos sirven por ejemplo para identificar al usuario que está utilizando la aplicación.
En ocaciones tenemos codigo que se repite muchas veces, para simplificar vamos a crear un context procesor que contenga la data que se repite, para poder utilizarlo entonces creamos un archivo que se llame context_processor.py en el cual declaramos una función, recibe request como parametro y retornamos la información, dentro de los settigns ponemos el nuevo procesador de contexto y listo.
podemos usar otro procesador de contexto que nos da informacion del usuario y se utiliza dentro del template con {{request.user}}
para usarlos debemos crear un procesaro de contexto
### Herencia e inclusión
Son dos formas de reutilizar nuestras plantillas y es usando extends e include con template tags, ésto nos va a ayudar a ahorrar tiempo reecribiendo maquetado de html.
## Rutas
Con Django podemos hacer varias cosas raras con las rutas, como por ejemplo hacer rutas dinamicas que nos permitan obtener una vista en detalle de un objeto en espesifico.
