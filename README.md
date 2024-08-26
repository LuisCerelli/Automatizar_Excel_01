# ***Automatización de Archivos CSV con Python***

### Descripción del Proyecto
Este proyecto tiene como objetivo la automatización de tareas relacionadas con la lectura, filtrado y exportación de archivos CSV. Usando Python y la librería pandas, el script permite procesar datos de manera rápida y eficiente, aplicando filtros y exportando los resultados a un archivo listo para ser utilizado o analizado.

El propósito es reducir el tiempo dedicado a la manipulación manual de archivos, proporcionando una solución flexible y personalizable para adaptarse a diferentes necesidades de procesamiento de datos.

### Funcionalidades Principales
Lectura automatizada de archivos: El script permite cargar archivos CSV de forma automatizada desde una carpeta específica. Esto simplifica el manejo de múltiples archivos sin necesidad de abrirlos manualmente.

Filtrado de datos: Se aplican filtros a las columnas seleccionadas para aislar los datos de interés. En este caso, se filtran los registros de acuerdo con el método de pago (por ejemplo, "Cash").

Exportación del archivo procesado: Una vez aplicado el filtrado, los datos resultantes se exportan automáticamente a un nuevo archivo CSV. Esto agiliza el flujo de trabajo, evitando pasos adicionales de guardado manual.

Modularidad: El código está diseñado en módulos, lo que facilita la personalización y expansión del mismo. Nuevos filtros o visualizaciones de datos se pueden agregar fácilmente, adaptándose a diferentes escenarios.

### Ventajas de la Automatización
Ahorro de tiempo: La automatización elimina la necesidad de realizar tareas repetitivas de forma manual, como abrir archivos, filtrar datos y exportar resultados. Este flujo automatizado reduce considerablemente el tiempo de procesamiento.

Consistencia: Al usar scripts automatizados, se garantiza que los datos siempre se manipulan de la misma manera, evitando errores humanos que pueden ocurrir al realizar procesos manuales repetidos.

Flexibilidad: El script es altamente adaptable, permitiendo que cualquier usuario lo ajuste a sus necesidades simplemente cambiando los parámetros de entrada o añadiendo nuevas funcionalidades. Esto es especialmente útil en entornos en los que los datos cambian constantemente.

Escalabilidad: El proyecto puede manejar grandes volúmenes de datos sin dificultad. Esto es esencial para el análisis de datos o para proyectos que requieren procesamiento de archivos en lote.

Integración: El uso de librerías populares como pandas permite integrar fácilmente el código con otros proyectos o flujos de trabajo existentes en Python, haciéndolo adecuado para una amplia gama de aplicaciones.

### Diferencias entre Windows y Mac/Linux para la Automatización de Scripts
En este proyecto, se utiliza un archivo .sh en lugar de un archivo .bat para automatizar la ejecución del script Python. Esto se debe a las diferencias en los sistemas operativos:

Windows: En Windows, se suelen usar archivos .bat (batch) para automatizar tareas. Estos archivos contienen comandos que se ejecutan en el intérprete de comandos de Windows (CMD o PowerShell). Un archivo .bat podría ejecutar un script Python y realizar tareas como cambiar de directorio, abrir archivos, etc.

Mac/Linux: En sistemas basados en Unix, como Mac o Linux, se utilizan archivos .sh (shell script). Estos scripts contienen comandos que se ejecutan en la terminal Bash o Zsh. Un archivo .sh es similar a un .bat, pero está diseñado para entornos Unix.

### Diferencias clave:
Archivos .bat (Windows): Son específicos para la plataforma Windows y no funcionan en Mac/Linux sin un entorno compatible como Wine o Cygwin.

Archivos .sh (Mac/Linux): Están diseñados para sistemas basados en Unix y no son compatibles directamente con Windows, a menos que se use una herramienta como WSL (Windows Subsystem for Linux) o Git Bash.

### En resumen, los scripts .sh son la alternativa en Mac/Linux a los archivos .bat de Windows, permitiendo automatizar tareas similares de una manera compatible con el sistema operativo.

## Si necesitas un archivo .bat para este codigo, no tienes mas que solicitármelo a mi correo
