# Data Engineer Programming Test

### Python 
(Para hacerlo interesante, usar Python 2.7)

Se deberá escribir un script que transforme el archivo datos_data_engineer.tsv en un archivo CSV que pueda ser insertado en una base de datos, y/o interpretado por cualquier parser estándar de archivos delimitados, de la manera más sencilla posible.

El archivo resultante debe tener las siguientes características:
* Cada row contiene la misma cantidad de campos
* Los campos se separan con un pipe |
* Se deben poder leer correctamente los caracteres especiales que estén presentes en los campos actuales del archivo. 
* El encoding del archivo final debe ser UTF-8 (datos_de_santander.tsv es un archivo UTF-16LE)

Preguntas
* 1) En qué requerimiento implementarías una cola de mensajes en una solución orientada a datos?  Que lenguaje utilizarías y porque?
En el caso de que se necesite trabajar con un modelo de comunicación asincrónico entre microservicios. Así se podría enviar, almacenar y recibir mensjaes de cualquier volumen entre los componentes. 
Se lograría mayor desempeño, fiabilidad y escalabilidad.
Utilizaría lenguajes orientados a objetos, como por ejemplo Python, Java,Scala,Ruby . 
* 2) Que experiencia posees sobre py spark o spark scala? Contar breves experiencias, en caso de contar experiencia con otro framework de procesamiento distribuido, dar detalles también.
No tengo experiencia con py spark ni con spark scala.

* 3) Qué funcionalidad podrías expandir desde el area de ingeniería de datos con una API y arquitectónicamente como lo modelarías?

	- Brindar un servicio de procesamiento de datos. Por ejemplo, un servicio de geolocalización de clientes, o de datos agregados de transacciones con el fin de luego explotar los datos y analizarlos categóricamente, según necesidad, podría ser por género, edad, zona geográfica. 
	- Para realizarla analizaría la necesidad que poseen los actores con la API, luego podría analizar en que arquitectura realizarla, el host en caso de ser necesario, los datos que necesito consumir, las politicas de datos, seguridad, en qué formato va a devolver los datos resultantes.
	
