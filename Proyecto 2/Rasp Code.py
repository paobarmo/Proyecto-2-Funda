from machine import Pin
import time
import socket

# Configurar las zonas de anotación
zona_1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
zona_2 = Pin(0, Pin.IN, Pin.PULL_DOWN)
zona_3 = Pin(11, Pin.IN, Pin.PULL_DOWN)
zona_4 = Pin(14, Pin.IN, Pin.PULL_DOWN)
zona_5 = Pin(10, Pin.IN, Pin.PULL_DOWN)

# Dirección del servidor Python que recibirá los datos
HOST = '192.168.1.100'  # IP del servidor Python
PORT = 12345  # Puerto que utilizará el servidor

# Conectar al servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Función para enviar el puntaje a Python cuando se activa una zona
def send_score(zone):
    if zone == 1:
        s.send("score: 100".encode())
    elif zone == 2:
        s.send("score: 70".encode())
    elif zone == 3:
        s.send("score: 30".encode())
    elif zone == 4:
        s.send("score: 20".encode())
    elif zone == 5:
        s.send("score: 50".encode())

# Bucle principal para detectar las zonas
while True:
    if zona_1.value() == 1:
        send_score(1)
    if zona_2.value() == 1:
        send_score(2)
    if zona_3.value() == 1:
        send_score(3)
    if zona_4.value() == 1:
        send_score(4)
    if zona_5.value() == 1:
        send_score(5)

    time.sleep(0.1)  # Esperar un poco antes de comprobar de nuevo

