import RPi.GPIO as GPIO
import time

# Configuração dos pinos dos relés
pinos_rele = [17, 18, 22, 23, 24, 25]

# Configuração dos pinos de corrente
pino_corrente_5v = 5
pino_corrente_gnd = 6

# Configuração da GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinos_rele, GPIO.OUT)

# Liga todas as bombas
def ligar_bombas():
    GPIO.output(pinos_rele, GPIO.HIGH)
    print("Bombas ligadas")

# Desliga todas as bombas
def desligar_bombas():
    GPIO.output(pinos_rele, GPIO.LOW)
    print("Bombas desligadas")

# Configuração dos pinos de corrente
GPIO.setup(pino_corrente_5v, GPIO.OUT)
GPIO.setup(pino_corrente_gnd, GPIO.OUT)

# Liga a alimentação
GPIO.output(pino_corrente_5v, GPIO.HIGH)
GPIO.output(pino_corrente_gnd, GPIO.LOW)

# Exemplo de uso
try:
    ligar_bombas()
    time.sleep(5)  # Mantém as bombas ligadas por 5 segundos
    desligar_bombas()

finally:
    # Desliga a alimentação no final
    GPIO.output(pino_corrente_5v, GPIO.LOW)
    GPIO.cleanup()
