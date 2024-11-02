# Proyecto de Automatización de Solicitud de Taxi Comfort

Este proyecto se centra en la automatización del proceso de solicitar un taxi con la tarifa Comfort. Se incluye un conjunto de pruebas para verificar la correcta implementación de este proceso.

## Archivos del Proyecto

- **data.py**: Contiene los valores de prueba que se utilizan en las pruebas automatizadas.
- **locators.py**: Define los localizadores necesarios para la automatización.
- **method.py**: Proporciona los métodos auxiliares usados en las pruebas.

## Pruebas de Automatización

El proyecto se divide en un total de 8 pruebas automatizadas, cada una abordando diferentes aspectos del proceso:

1. `def test_set_route(self)`: Configura y verifica la configuración de la ruta.
2. `def test_pick_comfort(self)`: Selecciona y valida la selección de la tarifa Comfort.
3. `def test_set_phone_number(self)`: Ingresa y comprueba la introducción del número de teléfono.
4. `def test_set_payment(self)`: Ejecuta y revisa la configuración de los métodos de pago.
5. `def test_set_message(self)`: Ingresa y confirma la inclusión de un mensaje personalizado.
6. `def test_set_requirements(self)`: Setea y valida la configuración de los requisitos adicionales.
7. `def test_call_taxi(self)`: Realiza la llamada al taxi y se verifica que se haya ejecutado la orden.
8. `def test_wait_driver_details(self)`: Verifica la recepción de los detalles del conductor y que el viaje haya sido tomado.

## Ejecución de las Pruebas

1. Para ejecutar las pruebas, asegúrate de tener configurado Python 3
2. Tener instalado Selenium
3. Instalar y ejecutar las pruebas desde el framework `pytest`.
4. Las pruebas se realizan sobre GoogleChrom, asegurarse de tener la version adecuada de GoogleChromeDriver

## Instalación

1. Clona este repositorio.
2. Instalar Selenium
3. Instalar Pytest
3. Ejecuta las pruebas con el siguiente comando:
   ```bash
   pytest /sprint_8/test.py
