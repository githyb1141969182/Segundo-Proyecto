# archivo: crypto_quotator_consola.py

import requests
import csv
from datetime import datetime

# Función para obtener datos de una criptomoneda
def obtener_precio(crypto):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": crypto.lower(),
        "vs_currencies": "usd",
        "include_24hr_change": "true",
        "include_market_cap": "true"
    }
    try:
        data = requests.get(url, params=params).json()
        if crypto.lower() in data:
            precio = data[crypto.lower()]["usd"]
            cambio_24h = data[crypto.lower()]["usd_24h_change"]
            market_cap = data[crypto.lower()]["usd_market_cap"]
            return {
                "Criptomoneda": crypto,
                "Precio USD": precio,
                "Cambio 24h (%)": cambio_24h,
                "Market Cap USD": market_cap,
                "Fecha": datetime.now()
            }
        else:
            print(f"Criptomoneda '{crypto}' no encontrada.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al conectarse a la API: {e}")
        return None

# Función para guardar datos en CSV
def guardar_en_csv(datos):
    archivo = "historial_criptos.csv"
    try:
        with open(archivo, 'x', newline='') as f:  # crea archivo si no existe
            writer = csv.writer(f)
            writer.writerow(["Fecha", "Criptomoneda", "Precio USD", "Cambio 24h (%)", "Market Cap USD"])
    except FileExistsError:
        pass

    with open(archivo, 'a', newline='') as f:
        writer = csv.writer(f)
        for d in datos:
            writer.writerow([d["Fecha"], d["Criptomoneda"], d["Precio USD"], d["Cambio 24h (%)"], d["Market Cap USD"]])

# ---- Programa principal ----
def main():
    cryptos_input = input("Ingrese criptomonedas separadas por coma (ej: bitcoin, ethereum): ")
    cryptos = [c.strip() for c in cryptos_input.split(",")]

    resultados = []
    for crypto in cryptos:
        res = obtener_precio(crypto)
        if res:
            resultados.append(res)
            # Mostrar en consola
            print("\n==============================")
            print(f"Criptomoneda: {res['Criptomoneda']}")
            print(f"Precio actual: ${res['Precio USD']:.2f}")
            print(f"Variación diaria: {res['Cambio 24h (%)']:+.2f}%")
            print(f"Capitalización de mercado: ${res['Market Cap USD']:.2f}")
            print("==============================")

    if resultados:
        guardar_en_csv(resultados)
        print("\n✅ Datos guardados en historial_criptos.csv")

if __name__ == "__main__":
    main()
