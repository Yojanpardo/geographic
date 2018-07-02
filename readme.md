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
Con Django podemos hacer varias cosas raras con las rutas, como por ejemplo hacer rutas dinamicas que nos permitan obtener una vista en detalle de un objeto en espesifico. también existen diversas formas de declarar rutas en nuestra aplicación.
a cada ruta que creamos le podemos dar un nombre el cual podermos utilizar para hacer nuestro codigo mas facil de versionar y organizar.
entro de los templates debemos utilizar el tag {% url %} para poder acceder a las vistas en lugar de estar escribiendo la ruta en cada plantilla.

### Name, reverse
Name es un atributo que se asigna en las urls y nos permite nombrar una ruta de una forma especifica para poder llamarla más adelante, reverse nos permite asignar rutas de cada objeto almacenandola directamente en el mismo.

### Include y namespaces
nos permite incluir las rutas de otras aplicaciones para poder hacer cada aplicacion mas independiente y los namespaces son como preposiciones para cada una de las clases de nuestras aplicaciones, con esto podemos evitar colisiones de rutas.

## Modelos
son la capa intermedia entre la aplicacion y la base de datos. se tranforman en tablas en nuestra base de datos, es una fuente unica de informacion y con los campos adecuados podemos manipular la información.

### shell
con ./manage.py shell accedemos a una consola interactiva que nos permite modificar la base de datos directamente desde la cosola

### Relaciones entre modelos
Va a ser necesario durante la creacion de nuestros proyectos generar relaciones entre los diferentes modelos. para ello utilizamos unos campor especiales en django que nos permiten generar relaciones de uno a uno, uno a muchos o muchos a muchos. [aqui pueden encontrar toda la documentacion.](https://docs.djangoproject.com/en/2.0/topics/db/examples/)

### ListView y filtros
Podemos generar un listado de objetos utilizando el ListView y asi nos ahorramos todo el trabajo hecho con el context procesor y esas maricadas, existen filtros que nos ayudarán a ejecutar busquedas avanzadas y que por supuesto están en [documentacion de django](https://docs.djangoproject.com/en/2.0/topics/db/queries/)

### get
nos permite hacer una busqueda de forma mas eficiente.

### ordering
al ejecutar una consulta se puede ordenar por algun atributo utilizando el order_by

### Administradores personalizados
hasta el momento solo parece que sirven para 'eliminar cosas'
