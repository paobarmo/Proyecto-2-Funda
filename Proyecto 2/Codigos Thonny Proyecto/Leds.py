import machine
from time import sleep

# Configuraciones de pines

pinEntradaAB= machine.Pin(18, machine.Pin.OUT)
pinClock= machine. Pin(19, machine.Pin.OUT)

#Secuencia que se envia al registro
pinEntradaAB.value(0)#1 prendido
pinClock.value(1)
sleep(1)
pinClock.value(0)

pinEntradaAB.value(0) #0 apagado
pinClock.value(1)
sleep(1)
pinClock.value(0)

pinEntradaAB.value(0) #0 apagado
pinClock.value(1)
sleep(1)
pinClock.value(0)


pinEntradaAB.value(1)#1 prendido
pinClock.value(1)
sleep(1)
pinClock.value(0)

pinEntradaAB.value(1)#1 prendido
pinClock.value(1)
sleep(1)
pinClock.value(0)

pinEntradaAB.value(0) #0 apagado
pinClock.value(1)
sleep(1)
pinClock.value(0)

pinEntradaAB.value(1)#1 prendido
pinClock.value(1)
sleep(1)
pinClock.value(0)

pinEntradaAB.value(0)
pinClock.value(1)
sleep(1)
