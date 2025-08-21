
 Cotizador de Criptomonedas (Consola)
 Descripción

Este proyecto permite consultar precios en tiempo real de criptomonedas como Bitcoin, Ethereum, etc., usando la API pública de CoinGecko.

El script:

Consulta una o varias criptomonedas ingresadas por el usuario.

Muestra el precio actual, variación diaria y capitalización de mercado en consola.

Guarda automáticamente un historial de consultas en un archivo CSV (historial_criptos.csv).

Ideal para aprender a trabajar con APIs, procesar datos en Python y guardar información para análisis posterior.

 Tecnologías utilizadas

Python 3.x

requests → para hacer peticiones HTTP a la API

csv → para guardar historial de consultas

datetime → para registrar fecha y hora de cada consulta

 Instalación

Clonar el repositorio

Instalar dependencias:

pip install requests

Uso

Ejecutar el script:

python crypto_quotator_consola.py


Ingresar las criptomonedas separadas por coma:

Ingrese criptomonedas separadas por coma (ej: bitcoin, ethereum): bitcoin, ethereum
