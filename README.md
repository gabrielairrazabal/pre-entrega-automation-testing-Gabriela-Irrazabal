# Proyecto de Automatización - Pre-Entrega

## Propósito del proyecto
El objetivo de este proyecto es desarrollar un conjunto de pruebas automatizadas utilizando **Selenium WebDriver** y **Pytest**, aplicando los conocimientos adquiridos sobre testing automatizado con Python.  
El propósito es validar el comportamiento de una aplicación web: https://www.saucedemo.com/, implementar buenas prácticas de organización de código y generar reportes de resultados.


## Tecnologías utilizadas
- **Python** → Lenguaje principal del proyecto.  
- **Pytest** → Framework para la ejecución y organización de pruebas.  
- **Selenium WebDriver** → Herramienta para la automatización de pruebas funcionales sobre navegadores.  
- **WebDriver Manager** → Para la gestión automática del driver de Chrome.  
- **Git & GitHub** → Control de versiones y publicación del código.

 ## Estructura del proyecto
 pre-entrega-automation-testing-Gabriela-Irrazabal
    tests/ # Casos de prueba automatizados
    utils/ # Funciones auxiliares o helpers
    reporte/ # Reportes HTML y capturas de ejecución
    README.md # Documentación del proyecto

## Dependencias del proyecto
pip install selenium pytest webdriver-manager pytest-html

## comando para ejecutar las pruebas
pytest -v --html=reporte/reportedepruebas.html