# Curso de Python
Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.​ Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional


- [Curso de Python](#curso-de-python)
- [Temas generales](#temas-generales)
- [Python](#python)
    - [Estructura de un proyecto en python](#estructura-de-un-proyecto-en-python)
      - [Convenciones](#convenciones)
  - [Iniciar un nuevo proyecto](#iniciar-un-nuevo-proyecto)


## Temas generales

* Las listas en **Python** son un tipo contenedor, compuesto, que se usan para almacenar conjuntos de elementos relacionados del mismo tipo o de tipos distintos. Junto a las clases tuple, range y str, son uno de los tipos de secuencia en Python, con la particularidad de que son **mutables**.

* Un **Diccionario** es una estructura de datos y un tipo de dato en Python con características especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones. Estos diccionarios nos permiten además identificar cada elemento por una **clave** (Key).

* Las funciones **Lambda** se comportan como funciones normales declaradas con la palabra clave **def**. Resultan útiles cuando se desea definir una función pequeña de forma concisa. Pueden contener solo una expresión, por lo que no son las más adecuadas para funciones con instrucciones de flujo de control.


## Python

### Guía de estilo: [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
* Todos los proyectos en python deben seguir la [guía de estilo de Google](https://google.github.io/styleguide/pyguide.html) para nombrar variables, nombrar métodos, documentar módulos, escribir docstrings, etc.
* Ver [ejemplo completo](http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html#example-google) de un módulo en python según la guía de estilo de Google.

### Estructura de un proyecto en python

#### Convenciones

* **requirements.txt**: todos los proyectos llevan un archivo *requirements.txt* en la root folder del proyecto. Este contiene la lista de dependencias utilizadas por los módulos del proyecto.
    - Si el proyecto incluye un *setup.py*, estas dependencias se instalarán al correr el comando `pip install -e .`
    - Si el proyecto no incluye un *setup.py*, estas dependencias deben instalarse corriendo el comando `pip install -r requirements.txt`

* **Tests**: todos los módulos escritos en python (`module.py`) deben tener un espejo (`test_module.py`) donde se escriben los tests (ver [template](python/Project-Example-1/package_name/test_project_euler.py)).
    - Los tests se estructuran según la [documentación de unittest](https://docs.python.org/2/library/unittest.html) y se corren con [nose](http://pythontesting.net/framework/nose/nose-introduction/) (En la línea de comandos: `$ nosetests`)
    - Todos los métodos públicos de un módulo `module.py` deben tener al menos un test en `test_module.py`. Deben testearse los casos especiales, así como algunos errores de input esperables por parte del cliente del método.
    - Los métodos privados (cuyo nombre debe comenzar con un **_**, para distinguirlos de los públicos) pueden omitir su test bajo las siguientes condiciones:
        + Son privados (no se espera que el cliente del módulo los use, son de uso interno dentro del módulo)
        + Son muy sencillos de entender y tienen pocas líneas.
        + Su funcionalidad está siendo testeada como parte de algún método público.

* **setup.py**: la inclusión de un *setup.py* es opcional, pero recomendable para proyectos grandes/complejos. Permite instalar el proyecto en el *path* del entorno virtual utilizado y utilizar importaciones absolutas como cualquier otra librería descargada de **pip**.
    - El proyecto se instala en el entorno virtual con `pip install -e .` (modo edición, sin crear una distribución) para poder editarlo sin instalarlo nuevamente.
    - Debe tenerse en cuenta que al agregar un paquete nuevo (una carpeta con un __init__.py en el interior) debe agregarse a la lista de la variable *packages* del *setup.py* y correr el comando de instalación nuevamente.
    - Un proyecto simple puede omitir el *setup.py* y desarrollarse con importaciones relativas. Aunque esta decisión debe reveerse si el proyecto se torna complejo.


## Iniciar un nuevo proyecto

Algunos aspectos de la estructuración de un repositorio pueden cambiar dependiendo del stack -más adelante se proveen templates para cada caso- pero todos deben respetar las siguientes indicaciones desde el momento en que se inicia un nuevo proyecto:

* **README**: Donde se listan:
    - El *objetivo* del proyecto
    - Un *ejemplo rápido* de uso
    - Las instrucciones de *instalación*
    - El resto de la documentación pertinente.