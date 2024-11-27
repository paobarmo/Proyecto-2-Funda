import network
import time

# Configura la conexión Wi-Fi
ssid = 'Fam Morales Calvo 2.4G'
password = '06081948'

# Activa la interfaz Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Conéctate a la red Wi-Fi
if not wlan.isconnected():
    print("Conectando a la red Wi-Fi...")
    wlan.connect(ssid, password)

    # Espera hasta que esté conectado
    while not wlan.isconnected():
        time.sleep(1)

# Imprime la información de la conexión
print("Conectado a la red Wi-Fi")
print("Dirección IP:", wlan.ifconfig()[0])

